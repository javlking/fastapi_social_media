from fastapi import FastAPI
from starlette.staticfiles import StaticFiles

from database import Base, engine

from api.comments_api import comments
# from api.hashtag_api import hashtags
from api.posts_api import posts
from api.photo_api import photos
from api.users_api import users

# создание таблиц в базе данных
Base.metadata.create_all(bind=engine)

app = FastAPI()
app.mount('/api/photo_api/photos', StaticFiles(directory='./api/photo_api/photos'), name='images')

app.include_router(users.app, tags=['user'])
app.include_router(posts.app, tags=['user_post'])
app.include_router(comments.app, tags=['comments'])
app.include_router(photos.app, tags=['photos'])


# @app.get('/hello')
# async def hello():
#     return {'hello': 'Fastapi'}
#
#
# @app.post('/hello')
# async def post_home(name: str):
#     return {'message': f'Hello {name}'}

