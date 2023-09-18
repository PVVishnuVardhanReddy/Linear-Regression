from django.shortcuts import render
from app1.linear import linearreg
def home(request):
    return render(request,"app1/index.html")

def fin(request):
    flag=1
    val1=request.GET["b1"] 
    val2=request.GET["b2"] 
    val3=request.GET["b3"]
    val4=request.GET["b4"] 
    n=int(linearreg(float(val1),float(val2),float(val4),float(val3)))
    return render(request,"app1/index.html",{"val":n,"flag":flag})
