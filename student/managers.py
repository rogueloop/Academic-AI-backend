from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _


class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """
    def create_user(self, clg_id, password, **extra_fields):
        """
        Create and save a user with the given clg_id and password.
        """
        if not clg_id:
            raise ValueError(_("The clg must be set"))
        
        # Use clg_id passed as argument
        extra_fields.setdefault("clg_id", clg_id)
        user = self.model(**extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, clg_id, password, **extra_fields):
        """
        Create and save a SuperUser with the given clg_id and password.
        """
     

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff=True."))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True."))
        
        return self.create_user(clg_id, password, **extra_fields)
