from django.shortcuts import render

def homepage(request):
    return render(request,'my_resume/index.html')