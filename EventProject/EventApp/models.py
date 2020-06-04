from django.db import models

# Create your models here.

class ChildDetail(models.Model):
    FirstName=models.CharField(max_length=50)
    FatherName=models.CharField(max_length=50)
    LastName=models.CharField(max_length=50)
    Age=models.IntegerField()
    Location_Where_You_Find=models.CharField(max_length=50)
    Picture=models.ImageField(upload_to='picture',max_length=100,null=True)
    def __str__(self):
        return 'self.FirstName'


class VolDetail(models.Model):
    FirstName=models.CharField(max_length=50)
    FatherName=models.CharField(max_length=50)
    LastName=models.CharField(max_length=50)
    Age=models.IntegerField()
    AdharCard_Detail=models.CharField(max_length=50)
    Mobile_No=models.IntegerField()
    Picture=models.ImageField(upload_to='picture',max_length=100,null=True)
    Reason=models.CharField(max_length=500)
    def __str__(self):
        return 'self.FirstName'



class DonDetail(models.Model):
    Name=models.CharField(max_length=50)
    AdharCard_Detail=models.CharField(max_length=50)
    Mobile_No=models.IntegerField()
    def __str__(self):
        return 'self.FirstName'
