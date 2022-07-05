import pytest

from utils import get_posts_all, get_posts_by_user


def test_get_posts_all():
    assert get_posts_all(None)

def test_get_posts_by_user():
    with pytest.raises(ValueError):
        get_posts_by_user(None)
