from .models import ShortUrl


def get_user_urls(current_user, ):
    return ShortUrl.all_user_urls(current_user)
