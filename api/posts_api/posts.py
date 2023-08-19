from fastapi import Body

from api import app
from database.postservice import delete_exact_post_db, get_all_or_exact_post_db, add_post_db


# получить все посты
@app.get('/api/post')
async def get_all_or_exact_post(post_id: int = 0):
    result = get_all_or_exact_post_db(post_id)

    return {'status': 1, 'message': result}


@app.post('/api/post')
async def new_post(user_id: int = Body(),
                   main_text: str = Body()):
    post_id = add_post_db(main_text=main_text, user_id=user_id)
    # result = get_all_or_exact_post_db(post_id)

    return {'status': 1, 'post_id': post_id}


# Изменить пост
@app.put('/api/post')
async def change_user_post():
    pass


# Удалить определенный пост
@app.delete('/api/post')
async def delete_user_post(post_id: int):
    result = delete_exact_post_db(post_id)

    return {'status': 1, 'message': result}




