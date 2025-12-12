# This is the one you should use – smaller, faster, 100% Linux
FROM postgres:16-alpine

# Auto-create database, user, password + our table
# ENV POSTGRES_DB=todoapp
# ENV POSTGRES_USER=todo_user
# ENV POSTGRES_PASSWORD=s3cr3t123

# Copy init script to create the task table
COPY init.sql /docker-entrypoint-initdb.d/