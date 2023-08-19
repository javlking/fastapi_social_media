from main import app
from fastapi import Request, Body, UploadFile
from database.photoservice import change_photo_db, get_all_or_exact_photo_db, delete_photo_db, add_photo_db


# получить все фотографии
@app.get('/api/photo')
async def get_all_or_exact_photo(photo_id: int = 0, user_id: int = 0):
    photo = get_all_or_exact_photo_db(photo_id, user_id)

    return {'status': 1, 'message': photo}


# Изменить фото профиля
@app.put('/api/photo')
async def change_user_photo(photo_id: int = Body(...),
                            photo_file: UploadFile = Body(...)):
    if photo_file:
        # сохранить фото в папку
        with open(f'{photo_id}.jpg', 'wb') as photo:
            photo_to_save = await photo_file.read()
            photo.write(photo_to_save)

        change_photo_db(photo_id, f'/api/photo_api/photos/{photo_id}.jpg')

    return {'status': 1, 'message': 'Фото успешно изменено'}


# Удалить определенную фотографию
@app.delete('/api/photo')
async def delete_user_photo(photo_id: int = Body()):
    result = delete_photo_db(photo_id=photo_id)

    return {'status': 1, 'message': result}


# Загрузить изображение
@app.post('/api/add-photo')
async def add_user_photo(post_id: int = Body(...),
                        photo_file: UploadFile = Body(...)):
    if photo_file:
        photo_id = add_photo_db(post_id, photo_path=photo_file)
        # сохранить фото в папку
        with open(f'{photo_id}.jpg', 'wb') as photo:
            photo_to_save = await photo_file.read()
            photo.write(photo_to_save)

        change_photo_db(photo_id, f'/api/photo_api/photos/{photo_id}.jpg')

    return {'status': 1, 'message': 'Фото успешно добавлено'}


