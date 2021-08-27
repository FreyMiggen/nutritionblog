
from django.db import models

from ckeditor.fields import RichTextField
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
    name=models.CharField(blank=False,max_length=40)
    quantity=models.DecimalField(blank=False, max_digits=8,decimal_places=0,default=1)
    ingredient=models.ManyToManyField(Ingredient)
    kcal=models.DecimalField(blank=True,max_digits=8,decimal_places=2,default=0)

    def __str__(self):
        return self.name

    def calories(self):
        count=0
        for val in self.ingredient.all():
            count=count+val.calories
        return count

class Recipe(models.Model):
    name=models.CharField(blank=False,max_length=500)
    main_ingredient=models.CharField(blank=False,max_length=500)
    optional_ingredient=models.CharField(blank=True,max_length=500)
    spicies=models.CharField(blank=True,max_length=500)
    calories=models.DecimalField(max_digits=10,decimal_places=2,default=0)
    recipe=RichTextField(blank=True,null=True)

    def __str__(self):
        return self.name

 

    
