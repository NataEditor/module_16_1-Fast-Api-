from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def welcome() -> dict:
    return "Главная страница"


@app.get("/user/admin")
async def welcome() -> str:
    return "Вы вошли как администратор"


@app.get("/user/{user_id}")
async def usid(user_id: str) -> str:
    return f"Вы вошли как пользователь № {user_id}"


@app.get("/user/{user_name}/{age}")
async def usinf(user_name: str, age: str) -> str:
    return f"Информация о пользователе. Имя: {user_name}, Возраст: {age}"
