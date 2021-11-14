from django.db import models

# Create your models here.


class Ingredient(models.Model):
    MEASUREMENT=[('ml','ml'),
                 ('gram','gram')]
    name=models.CharField(blank=False, max_length=200)
    quantity=models.DecimalField(blank=False, max_digits=8,decimal_places=0,default=100)
    measure=models.CharField(blank=False,max_length=4,choices=MEASUREMENT,default='gram')
    calories=models.DecimalField(blank=False,null=False,decimal_places=2,max_digits=8,default=0)


    def __str__(self):
        return self.name

class Dish(models.Model):
    name=models.CharField(blank=False,max_length=120)
    ingredient=models.ManyToManyField(Ingredient)
    #calories=models.DecimalField(blank=False,max_digits=12,null=False,decimal_places=2)


    # def __init__(self):
    #     count=float(0)
    #     for val in self.ingredient:
    #         count=count+val.calories

    #     self.calories=count
            
    #     return count
    def __str__(self):
        return self.name


