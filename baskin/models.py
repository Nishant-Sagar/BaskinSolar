from django.db import models

# Create your models here.
class Details(models.Model):
    name = models.CharField(max_length=25)
    roof_age = models.IntegerField()
    email = models.EmailField()
    phone = models.IntegerField()
    address = models.CharField(max_length=300)
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


radio = (
    ('Yes','Yes'),
    ('No','No')
)
roof_choices = (
    ('Comp Shingle','Comp Shingle'), 
    ('Concrete','Concrete'),
    ('Metal','Metal'), 
    ('Spanish', 'Spanish'), 
    ('Clay','Clay'),
    ('Other','Other')
)

# Create your models here.
class Register(models.Model):
    name = models.CharField(max_length=25)
    roof_age = models.IntegerField()
    email = models.EmailField()
    phone = models.IntegerField()
    address = models.CharField(max_length=250)
    monthly_bill = models.IntegerField()
    HOA = models.CharField(max_length=10, choices= radio, default='Yes')
    battery = models.CharField(max_length=10, choices= radio, default='Yes')
    foundation = models.CharField(max_length=10, choices= radio, default='Yes')
    roof_type = models.CharField(max_length=20, choices=roof_choices, default='Comp Shingle')
    availability = models.DateTimeField()
    bill = models.FileField(upload_to='uploads/%d/%m/%y/')
    meter_picture = models.FileField(upload_to='uploads/%d/%m/%y/')
    company_name = models.CharField(max_length=200)
    questions = models.CharField(max_length=800)

    class Meta:
        verbose_name = 'register'
        verbose_name_plural = 'register'

    def __str__(self):
        return self.name 