from django.shortcuts import render
from .models import job
# Create your views here.


def job_list(request):
     job_list = job.objects.all()
     context = {'job' : job_list}
     return render(request,'job/job_list.html',context)




def job_details(request):
     job_details = job.objects.get(id=id)
     context = {'job' : job_details}
     return render(request,'job/job_details.html',context)
     
