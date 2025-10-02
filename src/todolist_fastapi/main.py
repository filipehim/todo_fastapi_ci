from fastapi import FastAPI
from src.todolist_fastapi.routes.auth_routes import auth_router
from src.todolist_fastapi.routes.todo_routes import todo_router
from src.todolist_fastapi.models.models import Base, db

Base.metadata.create_all(bind=db)

app = FastAPI(title='Todo List')

app.include_router(auth_router)
app.include_router(todo_router)
