from django.db import models



# Create your models here.
class employee(models.Model):
  firstname = models.CharField(max_length=200)
  
      
  def __str__(self):
    return self.firstname