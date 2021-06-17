from django.db import models
class details(models.Model):
    sno=models.AutoField(primary_key=True)
    name=models.CharField(max_length=25,default="")
    city=models.CharField(max_length=30,default="")
    address=models.TextField(max_length=100 ,default="")
    dept=models.CharField(max_length=25,default="")
    image=models.ImageField(upload_to="app/images",default="")
    #date=models.DateField()
    #image = models.ImageField()
    def __str__(self):
        return self.name

