from django.shortcuts import HttpResponse
from django.shortcuts import render
from .models import Polls, User_Polls
#from .models import Peralta

def inicio_view(request,*args,**kwargs):
# print(request.user) 
 return render(request,'inicio.html',{
     
 })
 
def resultados_view(request,*args,**kwargs):
  return render(request,'resultados.html',{})

def encuestas_view(request,*args,**kwargs):
  #obj=Polls.objects.get(id=1)
  my_context = { 
               "my_text":"this is about Peralta.",
               "my_number":123,
               "my_list":[11,22,532,60,"GG"]
  #"obj_Encuesta": obj
    }
  return render(request,'encuestas.html',my_context)