from django.shortcuts import HttpResponse
from django.shortcuts import render

def inicio_view(request,*args,**kwargs):
 print(request.user)
 return render(request,'inicio.html',{})
 
def resultados_view(request,*args,**kwargs):
  return render(request,'resultados.html',{})

def encuestas_view(request,*args,**kwargs):
  my_context = { "my_text":"this is about us.",
               "my_number":123,
               "my_list":[11,22,532,60,"GG"]
  } 
  return render(request,'encuestas.html',my_context)