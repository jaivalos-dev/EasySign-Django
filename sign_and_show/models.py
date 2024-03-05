from django.db import models

# Create your models here.
class document(models.Model):
    docfile = models.FileField(upload_to='documents/%Y/%m/%d')
    def __str__(self):
        return self.docfile.name