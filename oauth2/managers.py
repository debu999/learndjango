from django.contrib.auth import models


class OAuth2Manager(models.UserManager):
    def create_new_user(self, user):
        new_user = self.create(
            id=user.get("id"),
            avatar=user.get("avatar"),
            public_flags=user.get("public_flags"),
            flags=user.get("flags"),
            locale=user.get("locale"),
            mfa_enabled=user.get("mfa_enabled"),
            tag=f"{user.get('username')}#{user.get('discriminator')}",
            is_superuser=True,
            is_staff=True,
            username=user.get("username"),
            name=user.get("name"),
            email=user.get("email"),
            password="dummypwd"
        )
        return new_user


