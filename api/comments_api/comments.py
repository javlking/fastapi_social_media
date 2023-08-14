from api import app
from fastapi import Request, Body

from database.postservice import get_exact_post_comments_db, \
    public_comment_db, change_exact_comment_db, delete_exact_comment_db


# Получить комментарии определенного поста
@app.get('/api/comment')
async def get_exact_post_comments(post_id: int = Body()):
    # Получить JSON со всеми данными которые пришли из front
    # data = await request.json() # {'post_id': 12}

    # Получить ключ post_id из data
    # post_id = data.get('post_id')

    if post_id:
        # Получаем данные из базы
        exact_post_comments = get_exact_post_comments_db(post_id)

        return {'status': 1, 'message': exact_post_comments}

    return {'status': 0, 'message': 'неверный ввод данных'}


# Опубликовать комментарий к посту
@app.post('/api/comment')
async def public_comment(post_id: int = Body(), user_id: int = Body(), text: str = Body()):
    try:
        new = public_comment_db(post_id=post_id,
                                user_id=user_id,
                                text=text)

        return {'status': 1, 'message': new}
    except Exception as e:
        return {'status': 0, 'message': str(e)}


# Изменить текст комментария
@app.put('/api/comment')
async def change_exact_user_comment(comment_id: int = Body(), new_comment_text: str = Body()):
    changed = change_exact_comment_db(comment_id=comment_id,
                                      new_comment_text=new_comment_text)

    return {'status': 1, 'message': changed}


# Удалить комментарий
@app.delete('/api/comment')
async def delete_exact_user_comment(comment_id):
    to_delete = delete_exact_comment_db(comment_id)

    return {'status': 1, 'message': to_delete}


