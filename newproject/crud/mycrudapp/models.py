from django.db import models
from django.utils import timezone

# Create your models here.
class stu(models.Model):
    STU_CORS_TYPE = [
        ('BCA', 'BCA'),
        ('BCOM', 'S')
    ]
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    date_added = models.DateTimeField(default=timezone.now)
    stu_cors = models.CharField(max_length=4, choices=STU_CORS_TYPE)
    