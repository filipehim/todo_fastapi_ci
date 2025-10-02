from pydantic import BaseModel, Field

class UserSchema(BaseModel):
    name: str = Field(..., examples=["Luiz"])
    email: str = Field(..., examples=["luiz@test.com"])
    password: str = Field(..., examples=["12345ab"])

    class Config:
        from_attributes = True

class LoginSchema(BaseModel):
    email: str = Field(..., examples=["luiz@test.com"])
    password: str = Field(..., examples=["12345ab"])