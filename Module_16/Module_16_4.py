from fastapi import FastAPI, Path
from typing import Annotated, List
from pydantic import BaseModel
import uvicorn

app = FastAPI()

class User(BaseModel):
    id: int
    username: str
    age: int

users = []
@app.get('/users')
async def get_users() -> List[User]:
    return users

@app.post('/user/{username}/{age}')
async def add_user(
        username: Annotated[str, Path(min_length=5, max_length=20, description='Enter username', example='SomeUser')],
        age: Annotated[int, Path(ge=1, le=100, description='Enter user age', example='25')]
    ) -> User:
    user = User()
    user.id = len(users) + 1 if users else 1
    user.username = username
    user.age = age
    users.append(user)
    return user

@app.put('/user/{user_id}/{username}/{age}')
async def update_user(
        user_id:  Annotated[str, Path(min_length=1, max_length=3, description='Enter user id', example='111')],
        username: Annotated[str, Path(min_length=5, max_length=20, description='Enter username', example='SomeUser')],
        age: Annotated[str, Path(min_length=1, max_length=3, description='Enter user age', example='25')]
    ) -> str:
    users[user_id] = f'Имя: {username}, возраст: {age}'
    return f'User {user_id} is updated'

@app.delete('/user/{user_id}')
async def delete_user(
        user_id:  Annotated[str, Path(min_length=1, max_length=3, description='Enter user id', example='111')]
    ) -> str:
    del users[user_id]
    return f'User {user_id} is deleted'

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)