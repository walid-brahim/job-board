from django.db import models

# Create your models here.
  # this for image place 
def imago(instance , filename):
     imagename , extension = filename.split(".")
     return "job/%s.%s"%(instance.id , extension)

   #this for choices 
JOB_CH= [
    ('Full-time', 'Full-time'),
    ('half time', 'half time'),
   
]     
  
  ##### class for job
class job (models.Model):

     title = models.CharField(max_length=20)
     description = models.TextField(max_length=250)  
     Vacancy = models.IntegerField(default=0)
     Salary = models.IntegerField(default=0)
     Job_Nature = models.CharField(max_length=15 ,choices=JOB_CH)
     category = models.ForeignKey('category', on_delete=models.CASCADE)
     Published_on = models.DateTimeField(auto_now=True)
     image = models.ImageField(upload_to =imago)


     def __str__(self):
         return self.title

######## class for category
class category (models.Model):
     name = models.CharField(max_length=20)


     def __str__(self):
         return self.name     

    