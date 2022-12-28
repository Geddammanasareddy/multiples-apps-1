from django.shortcuts import render

# Create your views here.
def three(request):
    return render(request,'h1.html')
def four(request):
    return render(request,'h2.html')