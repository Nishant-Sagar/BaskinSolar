from django.db import models

# Create your models here.
class Details(models.Model):
    name = models.CharField(max_length=25)
    roof_age = models.IntegerField()
    email = models.EmailField()
    phone = models.IntegerField()
    address = models.TextField(max_length=100)
    monthly_bill = models.IntegerField()
    HOA = models.BooleanField(default=True)
    battery = models.BooleanField(default=True)
    foundation = models.BooleanField(default=True)
    roof_type = models.CharField(max_length=20)
    availability = models.DateTimeField()
    bill = models.FileField(upload_to='uploads/%d/%m/%y/')

    class Meta:
        verbose_name = 'details'
        verbose_name_plural = 'details'

    def __str__(self):
        return self.name 