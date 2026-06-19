from django.db import models


class RestaurantBranch(models.Model):

    branch_name = models.CharField(max_length=100)

    address = models.TextField()

    contact_number = models.CharField(max_length=20)

    open_time = models.TimeField()

    close_time = models.TimeField()

    def __str__(self):
        return self.branch_name


class TableModel(models.Model):

    branch = models.ForeignKey(
        RestaurantBranch,
        on_delete=models.CASCADE
    )

    table_number = models.CharField(max_length=20)

    seating_capacity = models.IntegerField()

    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.branch.branch_name} - Table {self.table_number}"