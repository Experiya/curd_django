from django.db import models
class details(models.Model):
    sno=models.AutoField(primary_key=True)
    name=models.CharField(max_length=25)
    city=models.CharField(max_length=30)
    dept=models.CharField(max_length=25)
    def __str__(self):
        return self.name

