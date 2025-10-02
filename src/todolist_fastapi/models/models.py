from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine

db = create_engine('sqlite:///banco.db')
Base = declarative_base()

class ModelUser(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    password = Column(String, nullable=False)

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

class ModelTodo(Base):
    __tablename__ = 'tasks'

    id = Column(Integer,primary_key=True, autoincrement=True)
    title = Column(String, nullable=False)
    description = Column(String(200), nullable=False)

    def __init__(self, title, description):
        self.title = title
        self.description = description

