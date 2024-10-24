from fastapi import FastAPI, Path, status, HTTPException, Request
from fastapi.responses import HTMLResponse
from typing import Annotated, List
from pydantic import BaseModel
from fastapi.templating import Jinja2Templates
import uvicorn
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

app = FastAPI()
templates = Jinja2Templates(directory='templates')

class User(BaseModel):
    id: int
    username: str
    age: int


users: list[User] = [
    User(id=1, username='UrbanUser', age=24),
    User(id=2, username='UrbanTest', age=22),
    User(id=3, username='Capybara', age=60)
]


@app.get('/')
async def get_users(request: Request) -> HTMLResponse:
    return templates.TemplateResponse(
        "users.html", {"request" : request, "users" : users}
    )


@app.get('/users/{user_id}')
async def get_user(request: Request, user_id: int) -> HTMLResponse:
    user = next(user for user in users if user.id == user_id)
    return templates.TemplateResponse(
        "users.html", {"request" : request, "user" : user}
    )


@app.post('/user/{username}/{age}')
async def add_user(
        username: Annotated[str, Path(min_length=5, max_length=20, description='Enter username', example='SomeUser')],
        age: Annotated[int, Path(ge=1, le=100, description='Enter user age', example=25)]
) -> User:
    user = User(id=len(users) + 1 if users else 1, username=username, age=age)
    users.append(user)
    return user


@app.put('/user/{user_id}/{username}/{age}')
async def update_user(
        user_id: Annotated[int, Path(ge=1, lt=1000, description='Enter user id', example=111)],
        username: Annotated[str, Path(min_length=5, max_length=20, description='Enter username', example='SomeUser')],
        age: Annotated[int, Path(ge=1, le=100, description='Enter user age', example=25)]
) -> User:
    try:
        user = next(user for user in users if user.id == user_id)
        user.username = username
        user.age = age
        return user
    except StopIteration:
        raise HTTPException(status_code=404, detail=f"User with user_id {user_id} was not found")


@app.delete('/user/{user_id}')
async def delete_user(
        user_id: Annotated[int, Path(ge=1, lt=1000, description='Enter user id', example=111)]
) -> User:
    try:
        user = next(user for user in users if user.id == user_id)
        return users.pop(users.index(user))
    except StopIteration:
        raise HTTPException(status_code=404, detail="User was not found")




if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
