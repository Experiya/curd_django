from django.shortcuts import render
from django.contrib import messages
from .models import details
from django.http import HttpResponse# Create your views here.
def home(request):
    data= details.objects.all()
    params = {'data':data}
    if request.method=='POST':
        name = request.POST['name']
        city = request.POST['city']
        dept = request.POST['dept']
        #print(name,city,dept)
        temp = details(name=name,city=city,dept=dept)
        temp.save()
        messages.success(request, "Your Details has been successfully submite")
        return render(request,'app/home.html',params)
    else:
        return render(request,'app/home.html',params)
def update(request,edit_id):
    edit_id = int(edit_id)
    data= details.objects.all()
    data2=details.objects.filter(sno=edit_id).first
    params = {'data':data,"edit_id":edit_id,'data2':data2}
    if request.method=="POST":
        change = details.objects.get(sno=edit_id)
        change.name = request.POST['name']
        change.city = request.POST['city']
        change.dept = request.POST['dept']
        change.save()
        return render(request,'app/update.html',params)
    else:
        return render(request,'app/update.html',params)
def delete(request,delete_id):
    delete_id = int(delete_id)
    data= details.objects.all()
    data2=details.objects.filter(sno=delete_id).first
    params = {'data':data,"delete_id":delete_id,'data2':data2}
    delete = details.objects.get(sno=delete_id)
    delete.delete()
    return render(request,'app/display.html',params)

def display(request):
    return render(request,'app/display.html')