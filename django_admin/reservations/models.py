from django.db import models
from users.models import User
from restaurants.models import TableModel


class Reservation(models.Model):

    STATUS_CHOICES = (
        ('CONFIRMED', 'Confirmed'),
        ('CANCELLED', 'Cancelled'),
        ('COMPLETED', 'Completed'),
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    table = models.ForeignKey(
        TableModel,
        on_delete=models.CASCADE
    )

    reservation_time = models.DateTimeField()

    party_size = models.IntegerField()

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='CONFIRMED'
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Reservation {self.id}"