from fastapi import FastAPI, HTTPException, status
from fastapi.responses import JSONResponse
from typing import List, Optional
from sqlmodel import SQLModel, Field, Session, select, create_engine
from datetime import datetime
from sqlalchemy.sql import func
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Todo API with SQLModel")

origins = [
    "http://localhost",
    "http://localhost:5173",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Database Configuration
DATABASE_URL = "postgresql://user:pass@localhost:5432/todo"  # Change in production!
engine = create_engine(DATABASE_URL, echo=False)  # echo=True for debugging

# SQLModel Tables
class Task(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    created_at: Optional[datetime] = Field(
        default=None,
        sa_column_kwargs={"server_default": func.now()}
    )
    title: str = Field(max_length=255, index=True)
    description: Optional[str] = Field(default=None, nullable=True)
    completed: bool = Field(default=False)
    completed_at: Optional[datetime] = Field(default=None, nullable=True)


# Create tables on startup (only for dev; use migrations in production)
@app.on_event("startup")
def on_startup():
    SQLModel.metadata.create_all(engine)


# Pydantic Models for Request/Response
class TaskCreate(SQLModel):
    title: str
    description: Optional[str] = None


class TaskUpdate(SQLModel):
    title: Optional[str] = None
    description: Optional[str] = None
    completed: Optional[bool] = None


class TaskResponse(SQLModel):
    id: int
    title: str
    description: Optional[str]
    completed: bool
    created_at: datetime
    completed_at: Optional[datetime]

    class Config:
        from_attributes = True  # Important for SQLModel → Pydantic conversion


# CRUD Endpoints

@app.post("/tasks", response_model=TaskResponse, status_code=status.HTTP_201_CREATED)
async def add_new_task(task_in: TaskCreate):
    """Create a new task"""
    with Session(engine) as session:
        task = Task(**task_in.dict())
        session.add(task)
        session.commit()
        session.refresh(task)
        return task

@app.get("/tasks/get", response_model=List[TaskResponse])
async def get_all_tasks(completed: Optional[bool] = None):
    """Get the 5 latest tasks. Optional filter: ?completed=true|false"""
    with Session(engine) as session:
        statement = select(Task)
        if completed is not None:
            statement = statement.where(Task.completed == completed)
        statement = statement.order_by(Task.created_at.desc())
        statement = statement.limit(5)
        tasks = session.exec(statement).all()
        return tasks


@app.get("/tasks/get/{task_id}", response_model=TaskResponse)
async def get_task_by_id(task_id: int):
    """Get a single task by ID"""
    with Session(engine) as session:
        task = session.get(Task, task_id)
        if not task:
            raise HTTPException(
                status_code=404,
                detail="Task not found"
            )
        return task


@app.patch("/tasks/update/{task_id}", response_model=TaskResponse)
async def update_task(task_id: int, task_update: TaskUpdate):
    """Update task (partial updates allowed)"""
    with Session(engine) as session:
        task = session.get(Task, task_id)
        if not task:
            raise HTTPException(status_code=404, detail="Task not found")

        update_data = task_update.dict(exclude_unset=True)  # Only fields that were sent
        for key, value in update_data.items():
            # if key == "completed" and value is True and task.completed_at is None:
            #     setattr(task, "completed_at", True)
            #     setattr(task, "completed_at", datetime.utcnow())
            # else:
            setattr(task, key, value)

        session.add(task)
        session.commit()
        session.refresh(task)
        return task


@app.delete("/tasks/remove/{task_id}")
async def remove_task(task_id: int):
    """Delete a task"""
    with Session(engine) as session:
        task = session.get(Task, task_id)
        if not task:
            raise HTTPException(status_code=404, detail="Task not found")
        session.delete(task)
        session.commit()
        return JSONResponse(status_code=200, content={'message' : 'deleted'} )
