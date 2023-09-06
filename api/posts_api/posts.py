from fastapi import Body, UploadFile

from api import app
from database.photoservice import change_photo_db, add_photo_db
from database.postservice import delete_exact_post_db, get_all_or_exact_post_db, add_post_db


# получить все посты
@app.get('/api/post')
async def get_all_or_exact_post(post_id: int = 0):
    result = get_all_or_exact_post_db(post_id)

    return {'status': 1, 'message': result}


@app.post('/api/post')
async def new_post(photo_file: UploadFile = None,
                   user_id: int = Body(),
                   main_text: str = Body(),
                   ):
    post_id = add_post_db(main_text=main_text, user_id=user_id)

    if photo_file:
        photo_id = add_photo_db(post_id, photo_path=photo_file)
        # сохранить фото в папку
        with open(f'{photo_id}.jpg', 'wb') as photo:
            photo_to_save = await photo_file.read()
            photo.write(photo_to_save)

        change_photo_db(photo_id, f'/api/photo_api/photos/{photo_id}.jpg')

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




