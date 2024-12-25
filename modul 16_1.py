from fastapi import FastAPI

app = FastAPI()


@app.get('/')
async def main_page():
    return 'Главная страница'


@app.get('/user/admin')
async def admin_page():
    return 'Вы вошли как администратор'


@app.get('/user/{user_id}')
async def user_page_id(user_id: str)
    return f'Вы вошли как пользователь № {user_id}'


@app.get('/user/{user_name}/{age}')
async def user_page(user_name: str, age: str)
    return f'Информация о пользователе. Имя: {username}, Возраст: {age}'
