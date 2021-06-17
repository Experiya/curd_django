from django.shortcuts import render
from django.contrib import messages
from .models import details
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse# Create your views here.
def home(request):
    data= details.objects.all()
    params = {'data':data}
    if request.method=='POST':
        name = request.POST['name']
        city = request.POST['city']
        address = request.POST['address']
        dept = request.POST['dept']
        image = request.FILES['image'] #request.POST['image']
        #fs = FileSystemStorage()
        #fs.save(image.name,image)
        temp = details(name=name,city=city,address=address,dept=dept,image=image)
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
        change.address = request.POST['address']
        change.dept = request.POST['dept']
        change.save()
        #if request.FILES['image']=='time.jpg':
          #  print("yes")
        #else:
          #  img = request.FILES['image']
          #  print("img")
      #  if (request.image['image']):
        #    print("yes")
        #else:
           # print("No")
        #img = request.FILES['image']
        return render(request,'app/update.html',params)
    else:
        return render(request,'app/update.html',params)
def delete(request,delete_id):
    delete_id = int(delete_id)
    data= details.objects.all()
    data2=details.objects.filter(sno=delete_id).first
    params = {'data':data,"delete_id":delete_id,'data2':data2}
    delete = details.objects.get(sno=delete_id)
    print(delete.image)
    delete.image.delete()
    delete.delete()
    return render(request,'app/delete.html',params)

def display(request):
    data= details.objects.all()
    params = {'data':data}
    return render(request,'app/display.html',params)

def preview(request,preview_id):
    preview_id = int(preview_id)
    data= details.objects.filter(sno=preview_id).first
    params={'data':data }
    return render(request,'app/preview.html',params)

def aboutUs(request):
    return render(request,'app/about.html')