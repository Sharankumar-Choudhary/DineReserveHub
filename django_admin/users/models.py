from django.db import models


class User(models.Model):

    ROLE_CHOICES = (
        ('DINER', 'Diner'),
        ('ADMIN_STAFF', 'Admin Staff'),
    )

    name = models.CharField(max_length=100)

    email = models.EmailField(unique=True)

    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default='DINER'
    )

    password_hash = models.CharField(max_length=255)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name