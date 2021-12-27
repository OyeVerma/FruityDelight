from django.db import models

# Create your models here.
class Order(models.Model):
    name = models.CharField(max_length=50)
    item = models.CharField(max_length=50)

    completed = models.BooleanField()

    order_date_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.item + ', ' + self.name

class Complaint(models.Model):
    name = models.CharField(max_length=50)
    complaint = models.TextField()