# ✅ Todo List API with FastAPI

API for task management, built with the [FastAPI](https://fastapi.tiangolo.com/) framework and managed using [Poetry](https://python-poetry.org/).

---

## 📚 Key Concepts
- Authentication (JWT, OAuth)
- Password encryption
- Unit testing
- Pagination

## 🛠️ Technologies Used
- Sqlalchemy
- Pydantic
- Sqlite
- Pytest
- Uvicorn


## 📦 Requirements

- Python 3.12+
- Poetry installed

To install Poetry on Windows (PowerShell):

```powershell
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | python -
```

Verify the installation:

```Bash
poetry --version
```

## 🚀 Project Setup and Execution

1. Clone the repository:

```Bash
git clone https://github.com/filipehim/todolist_fastapi.git
cd todo_list_api
```

2. Install dependencies:

```Bash
poetry install
```

3. Activate the virtual environment:

```Bash
poetry shell
```

4. Set environment variables:

```Env
SECRET_KEY=28hIJBUKULzM5WfQFZYoN5O6NiG1B3vm
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTE=30
```

5. Run tests:

```Bash
poetry run pytest
```

6. Start the API server:

```Bash
poetry run uvicorn src.todolist_fastapi.main:app --reload
```
7. Access the application:

API: http://localhost:8000 <br>
Swagger Documentation: http://localhost:8000/docs

## Edpoints:

Here you can list the main routes of your API, and what are their expected request bodies.
​
| route                             | description                                          
|----------------------|-----------------------------------------------------
| <kbd>POST /register</kbd>      | Registers a new user
| <kbd>POST /login</kbd>     | Authenticates a user
| <kbd>POST /todos</kbd>     | Creates a new task
| <kbd>GET /todos</kbd>     | Retrieves created tasks with pagination
| <kbd>PUT /todos/{id_task}</kbd>     | Updates a task
| <kbd>DELETE /todos{id_task}</kbd>     | Deletes a task
