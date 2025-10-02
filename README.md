# Api todo list with FastApi

API para gerenciamento de tarefas, construída com o framework [FastApi](https://fastapi.tiangolo.com/) e gerenciada com [Poetry](https://python-poetry.org/).

---
## Conceitos aplicados
- Authenticação (JWT, OAuth)
- Criptografia de senhas
- Testes unitários
- Paginação

## Tecnologias Usadas
- Fastapi
- Sqlalchemy
- Pydantic
- Sqlite
- Pytest
- Uvicorn


## Requisitos

- Python 3.12+
- Poetry instalado

Para instalar o Poetry no Windows (PowerShell):

```powershell
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | python -
```

Verifique a instalação:

```Bash
poetry --version
```

## Instalação e execução do projeto
1. clone o repositório:

```Bash
git clone https://github.com/filipehim/todolist_fastapi.git
cd todo_list_api
```

2. Instale as dependências:

```Bash
poetry install
```

3. Ative o ambiente virtual:
```Bash
poetry shell
```

4. Configure variáveis de ambiente:
```Env
SECRET_KEY=28hIJBUKULzM5WfQFZYoN5O6NiG1B3vm
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTE=30
```
5. Execute os testes:
```Bash
poetry run pytest
```

6. Inicie o servidor da Api:
```Bash
poetry run uvicorn src.todolist_fastapi.main:app --reload
```
7. Acesse a aplicação:

API: http://localhost:8000 <br>
Documentação Swagger: http://localhost:8000/docs

## Edpoints:

Here you can list the main routes of your API, and what are their expected request bodies.
​
| route                             | description                                          
|----------------------|-----------------------------------------------------
| <kbd>POST /register</kbd>      | Faz o cadastro de um usuário
| <kbd>POST /login</kbd>     | Faz a autenticação de um usuário
| <kbd>POST /todos</kbd>     | Cria uma tarefa
| <kbd>GET /todos</kbd>     | Visualiza as tarefas criadas com paginação
| <kbd>PUT /todos/{id_task}</kbd>     | Edita uma tarefa
| <kbd>DELETE /todos{id_task}</kbd>     | Exclui uma tarefa
