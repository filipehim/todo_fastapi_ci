from fastapi import APIRouter, Depends, HTTPException
from todolist_fastapi.functions import get_session, create_token, authenticate_user
from src.todolist_fastapi.schemas.schema_auth import UserSchema, LoginSchema
from src.todolist_fastapi.models.models import ModelUser
from sqlalchemy.orm import Session
from src.todolist_fastapi.settings import bcrypt_context, ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTE, SECRET_KEY
from fastapi.security import OAuth2PasswordRequestForm

auth_router = APIRouter()

@auth_router.post('/register')
async def register_user(user: UserSchema, session: Session = Depends(get_session)):
    """
    Cria a conta de um usuário
    """
    user_f = session.query(ModelUser).filter(ModelUser.email==user.email).first()
    if user_f:
        # já existe um usuário com esse email
        raise HTTPException(status_code=400, detail='E-mail do usuário já cadastrado')
    else:
        encrypted_password = bcrypt_context.hash(user.password)
        new_user = ModelUser(user.name, user.email, encrypted_password)
        session.add(new_user)
        session.commit()
        access_token = create_token(new_user.id)
        return {'token':{access_token}}

@auth_router.post('/login')
async def login_user(dados_formulario: OAuth2PasswordRequestForm = Depends(), session: Session = Depends(get_session)):
    user = authenticate_user(dados_formulario.username, dados_formulario.password, session)
    if not user:
        raise HTTPException(status_code=404, detail="User not found.")  
    else:
        access_token = create_token(user.id)
        return {
       'access_token': access_token,
       'token_type': 'Bearer' }

