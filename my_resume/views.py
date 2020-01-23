from django.shortcuts import render

# Create your views here.
def project1(request):
    return render(request,'my_resume/project1.html')

def project2(request):
    return render(request,'my_resume/project2.html')
