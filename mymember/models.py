from django.db import models

GENDER_CHOICES = (
    ('male', 'ชาย'),
    ('female', 'หญิง'),
)

# Create your models here.
class alumni(models.Model):
    name=models.CharField(max_length=255)
    nickname=models.CharField(max_length=255, blank=True)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES,blank= True)
    year = models.CharField(max_length=6)
    faculty = models.CharField(max_length=255)
    employee_code = models.CharField(max_length=6, blank=True)

    #major
    #กอง ฝ่าย
    #email

    def __str__(self):
        return "{}-{}".format(self.year, self.name)

