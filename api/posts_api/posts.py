from api import app


# получить все посты
@app.get('/api/post')
async def get_all_or_exact_post(post_id: int = 0):
    pass


# Изменить пост
@app.put('/api/post')
async def change_user_post():
    pass


# Удалить определенный пост
@app.delete('/api/post')
async def delete_user_post():
    pass





