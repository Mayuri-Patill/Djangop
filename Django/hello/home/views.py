from django.shortcuts import render,HttpResponse
from home.models import Feedback

# Create your views here.
def index(request):
    return render(request,'index.html')
    # return HttpResponse("this is home page")
def contact(request):
    return render(request,'contact.html')
def apti(request):
    return render(request,'apti.html')
def pythond(request):
    return render(request,'pythond.html')
def pythonmt(request):
    return render(request,'pythonmt.html')
def pythonat(request):
    return render(request,'pythonat.html')
def verbal(request):
    return render(request,'verbal.html')
def feedback(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        pno=request.POST.get('pno')
        desc=request.POST.get('desc')
        feedback=Feedback(name=name,pno=pno,email=email,desc=desc)
        feedback.save()
    return render(request,'feedback.html')