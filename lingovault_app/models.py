from django.db import models

# Create your models here.
class Language(models.Model):
  name = models.CharField(max_length=20)
  date_added = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.name


    
     








