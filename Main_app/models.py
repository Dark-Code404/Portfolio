from django.db import models
from django.core.validators import FileExtensionValidator
from django.db import models

class About(models.Model):
    Name = models.CharField(max_length=200)
    Title = models.CharField(max_length=200)
    Birthdate = models.DateField(auto_now=False, auto_now_add=False)
    Phone = models.CharField(max_length=200)
    Address = models.CharField(max_length=200)
    Email = models.EmailField(max_length=200)
    Degree = models.CharField(max_length=200)
    Website = models.CharField(max_length=200,blank=True)
    Age=models.IntegerField(default=0)
    myDiscription = models.TextField()
    





    def __str__(self):
        return self.Name
    


class Othercontact(models.Model):
        Name=models.CharField(max_length=200)
        Email = models.EmailField(max_length=200)
        Subject=models.CharField(max_length=200)
        Message = models.CharField(max_length=500)

        def __str__(self):
          return self.Name



class Mycontact(models.Model):
        Location=models.CharField(max_length=200)
        Email = models.EmailField(max_length=200)
        Number = models.CharField(max_length=500)

        def __str__(self):
          return self.Location





class Language(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class ResumeAbout(models.Model):
    Name = models.CharField(max_length=200, blank=True)
    Post = models.CharField(max_length=200)
    Phone = models.CharField(max_length=200, blank=True)
    Email = models.EmailField(max_length=200, blank=True)
    Location = models.CharField(max_length=200, blank=True)
    Summary = models.TextField()
    Language = models.ManyToManyField(Language, blank=True)

    def __str__(self):
        return self.Name



# skill  technical field
class ResumeTechnical(models.Model):
     Name=models.CharField(max_length=200)
     Description=models.CharField(max_length=200)
     def __str__(self):
      return self.Name


# skill soft field
class ResumeSoft(models.Model):
     Name=models.CharField(max_length=200)     
     def __str__(self):
      return self.Name




class ResumeEducation(models.Model):
     Course=models.CharField(max_length=200)     
     College=models.CharField(max_length=200)   
     Startdate=models.CharField(max_length=250)   
     Enddate=models.CharField(max_length=250)
     Location=models.CharField(max_length=200)
     def __str__(self):
      return self.Course




class ResumeCerti(models.Model):
     Certification=models.CharField(max_length=200)   
     year = models.PositiveSmallIntegerField()  
     From=models.CharField(max_length=200)   

     def __str__(self):
      return self.Certification
     



class Skills(models.Model):
     skill=models.CharField(max_length=200)   
     

     def __str__(self):
      return self.skill     
     







          
     




