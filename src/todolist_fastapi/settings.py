from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext
from dotenv import load_dotenv
from os import getenv

load_dotenv()

bcrypt_context = CryptContext(schemes=['bcrypt'], deprecated='auto')
SECRET_KEY = getenv('SECRET_KEY')
ALGORITHM = getenv('ALGORITHM')
ACCESS_TOKEN_EXPIRE_MINUTE = int(getenv('ACCESS_TOKEN_EXPIRE_MINUTE'))
oauth2_schema = OAuth2PasswordBearer(tokenUrl='/login')