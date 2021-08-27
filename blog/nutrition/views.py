from nutrition.forms import DishForm, RecipeFind, RecipeForm
from django.shortcuts import render
from django.http.response import HttpResponseRedirect, HttpResponse
from .models import Ingredient,Dish,Recipe
#from .forms import IngredientForm
import requests, json
import requests
import json

api_url = 'https://api.calorieninjas.com/v1/nutrition?query='
# query = '1 slice of beef'
# response = requests.get(api_url + query, headers={'X-Api-Key': 'ZwDpQLeGgrYKVgNd7UE7/Q==ZwxlN5PK4cfBMhua'})
#
# if response.status_code == requests.codes.ok:
#     data = response.json()
#     # print(json.dumps(data,indent=4))
#     # print(len(data['items']))
#     print(data['items'][0]['calories'])
#
# else:
#     print("Error:", response.status_code, response.text)
# Create your views here.


def ingredient_form(request):
    add=False
    kcal=0
    if request.method == 'POST':
        name=str(request.POST.get('name'))
        if Ingredient.objects.filter(name=name).exists():
            track=Ingredient.objects.filter(name=name)
            add=True
            for val in track:
                if val.measure==str(request.POST.get('measure')):
                    add=False
                    amount=float(request.POST.get('quantity'))
                    kcal=(amount/float(val.quantity))*float(val.calories)
                    break
            if add==True:
                query = str(request.POST.get('quantity')) + ' '+str(request.POST.get('measure'))+' ' + str(request.POST.get('name'))
                response = requests.get(api_url + query, headers={'X-Api-Key': 'ZwDpQLeGgrYKVgNd7UE7/Q==ZwxlN5PK4cfBMhua'})
                data = response.json()
                if len(data['items'])==0:
                    return HttpResponse('Does not exits')
                else:
                    kcal = float(data['items'][0]['calories'])

                
        else:
            add=True
            query = str(request.POST.get('quantity')) + ' '+str(request.POST.get('measure'))+' ' + str(request.POST.get('name'))
            response = requests.get(api_url + query, headers={'X-Api-Key': 'ZwDpQLeGgrYKVgNd7UE7/Q==ZwxlN5PK4cfBMhua'})
            data = response.json()
            if len(data['items'])==0:
                 return HttpResponse('Does not exits')
            else:
                kcal = float(data['items'][0]['calories'])
    if add==True and request.POST.get('subject') == 'yes':
        k=kcal/float(request.POST.get('quantity'))*100
        form=Ingredient(name=str(request.POST.get('name')),measure=request.POST.get('measure'),calories=k)
        form.save()       

        return render(request, 'nutrition/ingredient.html',{'kcal':kcal,'add':add})
    else:
        return render(request, 'nutrition/ingredient.html',{'kcal':kcal,'add':add})




def dish_form(request):
    form=DishForm()
    if request.method=='POST':
        form=DishForm(request.POST)
        if form.is_valid():
            form.save()
    
    return render(request,'nutrition/dish_form.html',{'form':form})
        



def recipe_form(request):
    form=RecipeForm
    if request.method=='POST':
        form=RecipeForm(request.POST)
        if form.is_valid():
            form.save()
    
    return render(request,'nutrition/recipe_form.html',{"form":form})


# a support function for the recipe_find

def support(arr1,arr2):
    m=len(arr1)
    #n=len(arr2)
    count=0
    for i in range(m):
        if arr1[i] in arr2:
            count+=1
        else:
            count=count
    if count==m:
        return True
    else:
        return False

def recipe_find(request):
    form=RecipeFind
    exist=False
    result=[]
    if request.method=='POST':
        form=RecipeFind(request.POST)
        if form.is_valid():
            searched=str(form.cleaned_data['key_words'])
            kcal=float(form.cleaned_data['calories'])
            search=searched.split(" ")
            data=Recipe.objects.all()
            for re in data:
                name=str(re.name).split(" ")
                calories=float(re.calories)
                m_ingre=str(re.main_ingredient)
                ingre=m_ingre.split("/")
                if support(search,name)==True or support(ingre,search)==True and calories<=kcal:
                    result.append(re)
    
    if len(result)>0:
        exist=True    

    return render(request,'nutrition/recipe_find.html',{"form":form,"exist":exist,"result":result})   


def recipe_detail(request,re_id):
    recipe=Recipe.objects.get(id=re_id)

    return render(request,'nutrition/recipe_detail.html',{"recipe":recipe})

            
            
            
        




