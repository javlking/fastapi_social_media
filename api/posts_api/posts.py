from fastapi import Body, UploadFile, APIRouter

from database.photoservice import change_photo_db, add_photo_db
from database.postservice import delete_exact_post_db, get_all_or_exact_post_db, add_post_db, chang_user_post_db

app = APIRouter()


# получить все посты
@app.get('/api/post')
async def get_all_or_exact_post(post_id: int = None):
    try:
        result = get_all_or_exact_post_db(post_id)
        return {'status': 1, 'message': result}
    except Exception as e:
        return {'status': 1, 'message': str(e)}




@app.post('/api/post')
async def new_post(
                   user_id: int = Body(),
                   main_text: str = Body(),
                   ):
    post_id = add_post_db(main_text=main_text, user_id=user_id)

    return {'status': 1, 'post_id': post_id}


# Изменить пост
@app.put('/api/post')
async def change_user_post(post_id: int = Body(),
                           new_text: str = Body()):

    checker = chang_user_post_db(post_id, new_text)

    if checker:
        return {'status': 1, 'message': checker}
    else:
        return {'status': 0, 'message': checker}


# Удалить определенный пост
@app.delete('/api/post')
async def delete_user_post(post_id: int):
    result = delete_exact_post_db(post_id)

    return {'status': 1, 'message': result}




