import os

from django.shortcuts import render, redirect

from .models import Student
from django.contrib import messages


# Create your views here.

def firstOne(request):

    all_std = Student.objects.all()
    if request.method == 'POST':
        name = request.POST.get('name')
        roll = request.POST.get('roll')
        img = request.FILES['img']

        if name and roll and img:
            if Student.objects.filter(name=name).exists():
                messages.warning(request, "Name already taken!")
                return redirect('firstOne')
            stu = Student.objects.create(name=name,roll=roll,img=img)
    return render(request, 'index.html',locals())

def delete_stu(request, id):
    stu = Student.objects.get(id=id)
    if stu.img != 'def.png':
        os.remove(stu.img.path)
    stu.delete()
    return redirect('firstOne')

def update_stu(request,id):
    stu = Student.objects.get(id=id)
    if request.method == 'POST':
        name = request.POST.get('name')
        roll = request.POST.get('roll')
        img = request.FILES['img']


        stu.name = name
        stu.roll = roll
        stu.img = img
        stu.save()
        return redirect('/')
    return render(request, 'update.html', locals())