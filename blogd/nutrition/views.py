from django.shortcuts import render
from django.http.response import HttpResponseRedirect, HttpResponse
from .models import Ingredient
from .forms import IngredientForm
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







