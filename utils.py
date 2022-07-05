import json


def get_posts_all():
    """Возвращает посты"""
    with open('./data/data.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
        return data
# print(get_posts_all())


def get_posts_by_user(user_name):
    """Возвращает посты определенного пользователя."""
    result = []
    for post in get_posts_all():
        if user_name.lower() in post['poster_name'].lower():
            result.append(post)
    return result
# print(get_posts_by_user('leo'))

def get_comments_by_post_id(post_id):
    """Возвращает комментарии определенного поста."""





def search_for_posts(query):
    """Возвращает список постов по ключевому слову"""
    pass

def get_post_by_pk(pk):
    """Возвращает один пост по его идентификатору."""
    pass

