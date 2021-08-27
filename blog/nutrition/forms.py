from django import forms
from django.db.models.fields import TextField
from django.forms.widgets import TextInput

from .models import *

class DishForm(forms.ModelForm):
    class Meta:
        model=Dish
        fields="__all__"
    
class RecipeForm(forms.ModelForm):
    name=forms.CharField(
        required=True,
        widget=forms.Textarea(
            attrs={
                'class':'new-class-two',
                'rows' :20,
                'placeholder':'Your description'
            }
        )
    ) 
    

    class Meta:
        model=Recipe
        fields='__all__'

class RecipeFind(forms.Form):
    key_words=forms.CharField(required=True,widget=forms.Textarea(attrs={'placeholder':'please enter the words you want to search for',"size":50}))
    calories=forms.DecimalField(max_digits=10,decimal_places=2, required=True)
    


    #  widgets={'name':forms.TextInput(attrs={'class':'form-control','placeholder':"Please enter name of the venue"}),
    #     'zip_code':forms.TextInput(attrs={'class':'form-control','placeholder':"Please enter venue address"}),
    #     'web_address':forms.TextInput(attrs={'class':'form-control','placeholder':"Please enter name the web address of the venue"}),
    #     'email_address':forms.EmailInput(attrs={'class':'form-control','placeholder':"Please enter email"}),
    #     'phone_number':forms.TextInput(attrs={'class':'form-control','placeholder':"Please enter phone contact for the venue"})}

    
        #widgets={'main_ingredient':forms.TextInput(attrs={"placeholder": 'Please seperate each ingredient by a space','size':'40'})}
  
