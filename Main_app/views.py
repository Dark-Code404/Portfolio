from django.shortcuts import redirect, render
from Main_app.models import About, Othercontact, ResumeAbout, Skills, ResumeEducation, ResumeTechnical, ResumeSoft

def home(request):
    if request.method == "POST":
        # Simplify form handling by creating the `Othercontact` instance directly
        Othercontact.objects.create(
            Name=request.POST.get('name'),
            Email=request.POST.get('email'),
            Subject=request.POST.get('subject'),
            Message=request.POST.get('message'),
        )

    # Use `.only()` or `.values()` to limit data fetched from the database
    about = About.objects.only('Name', 'Title', 'Phone', 'Email', 'Address', 'Degree', 'Age', 'myDiscription')
    resume_about = ResumeAbout.objects.select_related().prefetch_related('Language').only('Name', 'Post', 'Summary').first()
    skills = Skills.objects.only('skill')
    edu = ResumeEducation.objects.only('Course', 'College', 'Startdate', 'Enddate', 'Location')
    techskill = ResumeTechnical.objects.only('Name', 'Description')
    softskill = ResumeSoft.objects.only('Name')

    # Use a dictionary to pass data to the template
    context = {
        'about': about,
        'res': resume_about,
        'skills': skills,
        'edu': edu,
        'tsk': techskill,
        'ssk': softskill,
    }

    return render(request, 'index.html', context)
