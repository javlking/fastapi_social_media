from datetime import datetime

from database.models import Comment, UserPost, Hashtag, PostPhoto
from database import get_db


### USERPOST ###
# Функция получения определенного или всех постов function(post_id)
# проверка post_id
def get_all_or_exact_post_db(post_id):
    db = next(get_db())

    # проверка
    if post_id == 0:
        all_posts = db.query(UserPost).all()

        return [{
                  "main_text": i.main_text,
                  "user_id": i.user_id,
                  "id": i.id,
                  "reg_date": i.reg_date,
                  "user_fk": i.user_fk,
                  "photos": [{'photo_id': b.id,
                              'photo_url': b.photo_path} for b in i.photo_fk]
                  "comments": [comment.text for comment in i.comment_fk]
                } for i in all_posts]

    exact_post = db.query(UserPost).filter_by(id=post_id).first()
    return {
          "main_text": exact_post.main_text,
          "user_id": exact_post.user_id,
          "id": exact_post.id,
          "reg_date": exact_post.reg_date,
          "user_fk": exact_post.user_fk,
          "photos": [{'photo_id': b.id,
                      'photo_url': b.photo_path} for b in exact_post.photo_fk]
                }


def chang_user_post_db(post_id, new_text):
    db = next(get_db())
    exact_post = db.query(UserPost).filter_by(id=post_id).first()

    # проверка
    if exact_post:
        exact_post.main_text = new_text
        db.commit()
        return "Изменен"

    return False


def add_post_db(main_text, user_id):
    db = next(get_db())

    new_post = UserPost(main_text=main_text, user_id=user_id, reg_date=datetime.now())

    db.add(new_post)
    db.commit()

    return new_post.id

# функция изменения текста к посту function(post_id, new_text)
def change_comment_text_db(post_id, new_text):
    db = next(get_db())

    # Пробуем найти в базе такую запись
    exact_post = db.query(UserPost).filter_by(id=post_id).first()

    # проверка
    if exact_post:
        exact_post.main_text = new_text
        db.commit()

        return 'Успешно изменено'

    return 'Ошибка в данных'


# функция удаления определенного поста function(post_id)
def delete_exact_post_db(post_id):
    db = next(get_db())

    # Пробуем найти в базе такую запись
    exact_post = db.query(UserPost).filter_by(id=post_id).first()

    # проверка
    if exact_post:
        db.delete(exact_post)
        db.commit()

        return 'Успешно удален'

    return 'Ошибка в данных'


############


### COMMENT ###

# функция получения комментариев определенного поста function(post_id)
def get_exact_post_comments_db(post_id):
    db = next(get_db())

    # Пробуем найти в базе такую запись
    exact_post_comments = db.query(Comment).filter_by(id=post_id).first()

    # проверка
    if exact_post_comments:
        return exact_post_comments

    return []


# функция публикации комментария function(post_id, user_id, text, reg_date)
def public_comment_db(post_id, user_id, text, reg_date=datetime.now()):
    db = next(get_db())

    new_comment = Comment(post_id=post_id, user_id=user_id,
                          text=text, reg_date=reg_date)

    db.add(new_comment)
    db.commit()

    return "Комментарий опубликован"


# функция изменения определенного комментария function(comment_id, new_comment_text)
def change_exact_comment_db(comment_id, new_comment_text):
    db = next(get_db())

    # Пробуем найти в базе такую запись
    exact_comment = db.query(Comment).filter_by(id=comment_id).first()

    # проверка
    if exact_comment:
        exact_comment.text = new_comment_text
        db.commit()
        return "Успешно изменен"

    return 'Ошибка в данных'


# Удалить определенный комментарий function(comment_id)
def delete_exact_comment_db(comment_id):
    db = next(get_db())

    # Пробуем найти в базе такую запись
    exact_comment = db.query(Comment).filter_by(id=comment_id).first()

    # проверка
    if exact_comment:
        db.delete(exact_comment)
        db.commit()
        return "Успешно удален"

    return 'Ошибка в данных'


############

### HASHTAGS ###
# функция получения доступных в базе хештегов function(size) list[:size]
def get_some_hashtags_db(size):
    db = next(get_db())

    some_hashtags = db.query(Hashtag).all()

    return some_hashtags[:size]


# функция получения определенного хештега function(hashtag_name)
def get_exact_hashtag_db(hashtag_name):
    db = next(get_db())

    # Пробуем найти в базе такую запись
    exact_hashtag = db.query(Hashtag).filter_by(hashtag_name=hashtag_name).first()

    # проверка
    if exact_hashtag:
        return exact_hashtag

    return []

### Удаление ###
# exact_user = db.query(PostPhoto).filter_by(id=post_id).first()
# db.delete(exact_user)
# db.commit()

### Изменение ###
# exact_user = db.query(PostPhoto).filter_by(id=post_id).first()
# exact_user.text = new_data
# db.commit()
