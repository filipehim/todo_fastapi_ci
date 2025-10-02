from pydantic import BaseModel, Field

class TodoSchema(BaseModel):
    title: str = Field(..., examples=["Futebol"])
    description: str = Field(..., examples=["O futebol é um esporte coletivo criado na inglaterra."])