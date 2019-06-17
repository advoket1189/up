from django.db import models

# Create your models here.
class main(models.Model):
    Name = models.CharField(max_length=120)
    description = models.TextField(default='description default text')

    def __unicode__(self):
         return self.Name