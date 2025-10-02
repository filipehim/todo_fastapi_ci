from sqlalchemy.orm import sessionmaker, Session
from fastapi import Depends, HTTPException
from jose import jwt, JWTError
from src.todolist_fastapi.settings import bcrypt_context, ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTE, SECRET_KEY, oauth2_schema
from src.todolist_fastapi.models.models import ModelUser, db
from datetime import datetime, timedelta, timezone

def get_session():
    try:
        Session = sessionmaker(bind=db)
        session = Session()
        yield session
    finally:
        session.close()


def create_token(id_user, duration_token=timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTE)):
    exp_date = datetime.now(timezone.utc) + duration_token
    dic_info = {'sub': str(id_user), 'exp': exp_date}
    jwt_encoded = jwt.encode(dic_info, SECRET_KEY, ALGORITHM)
    return jwt_encoded


def verify_token(token: str = Depends(oauth2_schema), session: Session = Depends(get_session)):
    try:
        dic_info = jwt.decode(token, SECRET_KEY, ALGORITHM)
        id_user = int(dic_info.get('sub'))
    except JWTError as err:
        print(err)
        raise HTTPException(status_code=401, detail='Unauthorized')

    # Verificar se o token é válido
    # extrair o id do usuário
    user = session.query(ModelUser).filter(ModelUser.id==id_user).first()
    if not user:
        raise HTTPException(status_code=401, detail='Acesso Inválido')
    return user

def authenticate_user(email, password, session: Session):
    user = session.query(ModelUser).filter(ModelUser.email==email).first()
    if not user:
        return False
    elif not bcrypt_context.verify(password, user.password):
        return False
    return user

