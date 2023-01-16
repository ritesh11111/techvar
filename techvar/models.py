from django.db import models

# Create your models here.
class Intern(models.Model):
    student_name=models.CharField(max_length=500)
    student_email=models.CharField(max_length=500)
    phone_no=models.IntegerField(default=0000000000)

class Company(models.Model):
    intern=models.ForeignKey(Intern,on_delete=models.CASCADE)
    company_name=models.CharField(max_length=500)