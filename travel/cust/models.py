from django.db import models
from owner.models import Keraladm
from django.contrib.auth.models import User


# Create your models here.



# Create your models here.




class Orders(models.Model):
    product=models.ForeignKey(Keraladm,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    address=models.CharField(max_length=500)
    phone=models.IntegerField()
    date=models.DateField(auto_now_add=True)
