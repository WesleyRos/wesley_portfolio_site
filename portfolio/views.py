from django.shortcuts import render,get_object_or_404
from .models import Profile,Tool,Case,Experience,Education,Certificate
def context():return {'profile':Profile.objects.first() or Profile(),'tools':Tool.objects.all(),'cases':Case.objects.filter(published=True),'experiences':Experience.objects.all(),'education':Education.objects.all(),'certificates':Certificate.objects.all()}
def home(request):return render(request,'home.html',context())

def case_detail(request,slug):
 data=context();data['case']=get_object_or_404(Case,published=True,slug=slug)
 return render(request,'case.html',data)
