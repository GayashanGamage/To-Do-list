# Simple To-Do Application

A basic full-stack To-Do application built with **FastAPI** (backend), **Vue.js** (frontend), and **PostgreSQL** (database). The project is fully containerized using Docker, with separate Dockerfiles for each component and a `docker-compose.yml` file to orchestrate everything.

## Project Structure

```
.
├── backend/          # FastAPI backend
│   ├── Dockerfile
│   └── ...           # app code, requirements.txt, etc.
├── frontend/         # Vue.js frontend
│   ├── Dockerfile
│   └── ...           # Vue app code, package.json, etc.
├── database/         # Optional PostgreSQL config (if any)
│   └── ...           
├── docker-compose.yml
└── README.md         # This file
```

## Technologies Used

- **Backend**: FastAPI (Python) - Handles API endpoints for CRUD operations on to-do items.
- **Frontend**: Vue.js - Provides a responsive UI for managing to-do tasks.
- **Database**: PostgreSQL - Persistent storage for to-do items.
- **Containerization**: Docker & Docker Compose

## Prerequisites

- Docker
- Docker Compose

## How to Run

1. Clone the repository (or extract the project files).
2. Navigate to the project root directory (where `docker-compose.yml` is located).
3. Build and start the containers:

   ```bash
   docker-compose up --build
   ```

4. The application will be available at:
   - Frontend: http://localhost:8080 (or the port defined for Vue)
   - Backend API: http://localhost:8000 (or the port defined for FastAPI)
   - API docs (Swagger): http://localhost:8000/docs

5. To stop the application:

   ```bash
   docker-compose down
   ```

## Development

- Backend: Edit files in `backend/`, then rebuild the image or use volume mounts for live reload.
- Frontend: Edit files in `frontend/`, Vue typically supports hot-reload if configured.

## Notes

- Ensure PostgreSQL credentials in `docker-compose.yml` match those used in the FastAPI configuration.
- Initial database setup/migration may be required (e.g., via Alembic if used).

Feel free to extend the features, such as user authentication or task categories! 

If you encounter any issues, check the Docker logs:

```bash
docker-compose logs
```
