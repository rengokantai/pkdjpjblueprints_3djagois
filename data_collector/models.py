from django.db import models

# Create your models here.

class DataPoint(models.Model):
    node_name = models.CharField(max_length=250)
    datetime = models.DateTimeField(auto_now_add=True)
    data_type = models.CharField(max_length=100)
    data_value=models.FloatField()

    def __str__(self):
        return 'DataPoint fot {}. {} ={}'.format(self.node_name,self.data_type,self.data_value)


class Alert(models.Model):
    data_type = models.CharField(max_length=100)
    min_value=models.FloatField(null=True,blank=True)
    max_value=models.FloatField(null=True,blank=True)
    node_name=models.CharField(max_length=200,blank=True)
    is_active = models.BooleanField(default=True)
    def save(self,*args,**kwargs):
        if self.min_value is None and self.max_value is None:
            raise models.exceptions.ValidationError("validation error")
        super(Alert,self).save(*args,**kwargs)