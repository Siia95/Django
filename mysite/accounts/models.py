from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True)

    groups = models.ManyToManyField(Group, related_name='custom_users')
    user_permissions = models.ManyToManyField(Permission, related_name='custom_users')

    class Meta:
        permissions = [
            ("can_do_something", "Can do something"),
        ]





