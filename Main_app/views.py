from django.contrib import messages
from django.shortcuts import  redirect, render

from Main_app.models import *
from django.views.decorators.clickjacking import xframe_options_exempt



# Create your views here.

def home(request):

    if request.method=="POST":
        getName=request.POST.get('name')
        getEmail=request.POST.get('email')
        getSubject=request.POST.get('subject')
        getMessage=request.POST.get('message')
        
        othercontact=Othercontact()
        othercontact.Name=getName
        othercontact.Email=getEmail
        othercontact.Subject=getSubject
        othercontact.Message=getMessage
        
      

       
       
        othercontact.save()
       
        


    about=About.objects.all()
    mycontact=Mycontact.objects.all()
    
    resume_about=ResumeAbout.objects.first()
    skills=Skills.objects.all()
    edu=ResumeEducation.objects.all()
    techskill=ResumeTechnical.objects.all()
    softskill=ResumeSoft.objects.all()
    lists={'about':about,'myc':mycontact,'res':resume_about,
            'skills':skills,'edu':edu,'tsk':techskill,'ssk':softskill}

    return render(request,'index.html',lists)
