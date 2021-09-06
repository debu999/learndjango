import logging

from django.contrib.auth.backends import BaseBackend

from oauth2.models import User

logger = logging.getLogger(__name__)


class OAuthAuthenticationBackend(BaseBackend):
    def authenticate(self, request, user) -> User:
        find_user = User.objects.filter(id=user.get("id"))
        if len(find_user) == 0:
            logger.error("User was not found. Saving...")
            new_user = User.objects.create_new_user(user=user)
            logger.info(f"User created {repr(new_user)}")
            return new_user
        return find_user

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
