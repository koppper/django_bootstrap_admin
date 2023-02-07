from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        """
        Create and save a user with the given email and password.
        """
        if not email:
            raise ValueError(_("The Email must be set"))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_author(self, email, password, **extra_fields):
        """
        Create and save an Author with the given email and password.
        """
        extra_fields.setdefault("is_author", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_author") is not True:
            raise ValueError(_("Author must have is_author=True."))
        return self.create_user(email, password, **extra_fields)

    def create_editor(self, email, password, **extra_fields):
        """
        Create and save an Editor with the given email and password.
        """
        extra_fields.setdefault("is_editor", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_editor") is not True:
            raise ValueError(_("Editor must have is_editor=True."))
        return self.create_user(email, password, **extra_fields)

    def create_reviewer(self, email, password, **extra_fields):
        """
        Create and save a Reviewer with the given email and password.
        """
        extra_fields.setdefault("is_reviewer", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_reviewer") is not True:
            raise ValueError(_("Reviewer must have is_reviewer=True."))
        return self.create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save an Admin with the given email and password.
        """
        extra_fields.setdefault("is_admin", True)
        extra_fields.setdefault("is_editor", True)
        extra_fields.setdefault("is_author", True)

        if extra_fields.get("is_admin") is not True:
            raise ValueError(_("Superuser must have is_admin=True."))
        if extra_fields.get("is_author") is not True:
            raise ValueError(_("Superuser must have is_author=True."))
        if extra_fields.get("is_editor") is not True:
            raise ValueError(_("Superuser must have is_editor=True."))
        return self.create_user(email, password, **extra_fields)
