import json
from json import JSONDecodeError

from bp_posts.dao.comment import Comment
from exceptions.data_exceptions import DataSourceError


class CommentDAO:
    """Загружает, ищет, получает данные"""

    def __init__(self, path):
        """Указываем путь к файлу"""
        self.path = path

    def _load_data(self):
        """Загружает данные из JSON и возвращает список из словарей"""

        try:
            with open(self.path, 'r', encoding="utf-8") as file:
                posts_data = json.load(file)
        except (FileNotFoundError, JSONDecodeError):
            raise DataSourceError(f"Не удается получить данные из файла {self.path}")

        return posts_data

    def _load_comments(self):
        """Возвращает список элементов Comment"""

        comments_data = self._load_data()
        list_of_comments = [Comment(**comment_data) for comment_data in comments_data]

        return list_of_comments

    def get_comments_by_post_pk(self, post_id):
        """ Получает все комментарии к определенному посту по его pk"""
        if type(post_id) != int:
            raise TypeError("Пост должен быть int")

        comments = self._load_comments()
        post_comment = []
        for p_comment in comments:
            if p_comment.post_id == post_id:
                if len(p_comment.comment) > 0:
                    post_comment.append(p_comment)

        return post_comment
