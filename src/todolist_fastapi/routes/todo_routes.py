from fastapi import APIRouter, Depends, Response, HTTPException, Query
from src.todolist_fastapi.schemas.schema_todo import TodoSchema
from todolist_fastapi.functions import get_session, verify_token
from sqlalchemy.orm import Session
from src.todolist_fastapi.models.models import ModelTodo, ModelUser

todo_router = APIRouter(dependencies=[Depends(verify_token)])

# CREATE
@todo_router.post('/todos')
async def post_task(task: TodoSchema, user: ModelUser = Depends(verify_token), session: Session = Depends(get_session)):
    user_filter = session.query(ModelUser).filter(ModelUser.id==user.id).first()
    if not user_filter:
        raise HTTPException(status_code=400, detail='Usuário não encontrado ou credenciai inválidas')
    else:
        new_iten = ModelTodo(task.title, task.description)
        session.add(new_iten)
        session.commit()
        return {'id': new_iten.id,
                'title': new_iten.title,
                'description': new_iten.description}

# READ Paginação offset-based
@todo_router.get('/todos')
def get_todos(page: int = Query(1, ge=1), limit: int = Query(10, ge=1, le=100), session: Session = Depends(get_session)): 
    offset = (page - 1) * limit
    tasks = session.query(ModelTodo).offset(offset).limit(limit).all()
    if len(tasks) == 0:
        return {"message": "Lista vazia"}
    total = session.query(ModelTodo).count()
    return {
        "page": page,
        "limit": limit,
        "total": total,
        "total_pages": (total + limit - 1) // limit,
        "data": tasks}

# UPDATE
@todo_router.put('/todos/{id_task}')
async def put_task(id_task: int, task: TodoSchema, session: Session = Depends(get_session)):
    task_filter = session.query(ModelTodo).filter(ModelTodo.id==id_task).first()
    if task_filter:
        task_filter.title = task.title
        task_filter.description = task.description
        session.commit()
        return {'id': task_filter.id,
        'title': task_filter.title,
        'description': task_filter.description}
    else:
        return {'mensagem': 'task not found'}

# DELETE
@todo_router.delete('/todos/{id_task}')
async def delete_task(id_task: int, session: Session = Depends(get_session)):
    task_filter = session.query(ModelTodo).filter(ModelTodo.id==id_task).first()
    if task_filter:
        session.delete(task_filter)
        session.commit()
        return Response(status_code=204)
    else:
        raise HTTPException(status_code=404, detail="Task not found.") 
