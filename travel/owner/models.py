from django.db import models

# Create your models here.

class Detailm(models.Model):
    name=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
 
    startingrate=models.IntegerField()
    offer=models.CharField(max_length=100)
    link=models.URLField(max_length=100)
    image=models.ImageField(upload_to='productimage')


class Keraladm(models.Model):
    name=models.CharField(max_length=1000)
    description=models.CharField(max_length=1000)
 
    startingrate=models.IntegerField()
    offer=models.CharField(max_length=1000)
    image=models.ImageField(upload_to='productimage')



    
# class Orders(models.Model):
#     product=models.ForeignKey(ownerm,on_delete=models.CASCADE)
#     user=models.ForeignKey(User,on_delete=models.CASCADE)
#     quantity=models.IntegerField(default=1)
#     address=models.CharField(max_length=500)
#     phone=models.IntegerField()
#     date=models.DateField(auto_now_add=True)
#     options=(
#         ("order placed","order placed"),
#         ("shipped","shipped"),
#         ("out for delivery","out for delivery"),
#         ("cancel","cancel"),
#         ("deliverd","deliverd")


#     )
#     status=models.CharField(max_length=100,choices=options,default='order placed')

