from django.db import models
# Create your models here.

class itemmodel(models.Model) :

    userid = models.CharField(max_length = 100)
    name = models.CharField(max_length=300)
    quantity = models.CharField(max_length=400)
    date = models.DateField(default="04-09-2021")
    status = models.IntegerField(default = 0)
    def __str__(self):
        return self.userid
