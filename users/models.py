from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class User(AbstractUser):
   
    # Add any other custom fields you need

    def __str__(self):
        return self.username
    class Meta:
        permissions = [
            ("can_publish", "Can publish content"),
            ("can_edit", "Can edit content"),
        ]
        
    # Add related_name attributes to avoid clashes
    groups = models.ManyToManyField(Group, blank=True, related_name='custom_users')
    user_permissions = models.ManyToManyField(Permission, blank=True, related_name='custom_users')
