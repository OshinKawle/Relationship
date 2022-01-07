from django.http import HttpResponse
from django.shortcuts import render,redirect
from . forms import DeptForm,StudentForm,ProfForm
from . models import Student,Prof,Dept
def department(request):
    form = DeptForm()
    if request.method == 'POST':
        form = DeptForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_dept')
    template_name = 'add.html'
    context = {'form': form}
    return render(request, template_name, context)

def student(request):
    form = StudentForm()
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_stud')
    template_name = 'add.html'
    context = {'form': form}
    return render(request, template_name, context)

def prof(request):
    form = ProfForm()
    if request.method == 'POST':
        form = ProfForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_prof')
    template_name = 'add.html'
    context = {'form': form}
    return render(request, template_name, context)


def showstud(request):
    list=Student.objects.all()
    if request.method == 'POST':
        list = Student.objects.filter(name__icontains=request.POST['query'])
    template_name = 'showstud.html'
    context = {'list': list}
    return render(request, template_name, context)

def showprof(request):
    prof=Prof.objects.all()
    if request.method == 'POST':
        prof = Prof.objects.filter(prof_name__icontains=request.POST['query'])
    template_name = 'showprof.html'
    context = {'prof': prof}
    return render(request, template_name, context)

def showdep(request):
    dep=Dept.objects.all()
    if request.method == 'POST':
        dep=Dept.objects.filter(dep_name__icontains=request.POST['query'])
        prof = dep[0].dep_pro.all()
        list = dep[0].dep_stu.all()
        template_name = "overview.html"
        context = {'dep': dep, 'professor': prof, 'list':list}
        return render(request, template_name, context)

    template_name = 'showdep.html'
    context = {'dep': dep}
    return render(request, template_name, context)

def deletestud(request,i):
    student=Student.objects.get(id=i)
    student.delete()
    return redirect('show_stud')


def deleteprof(request, i):
    student = Prof.objects.get(id=i)
    student.delete()
    return redirect('show_prof')


def deletedep(request, i):
    student = Dept.objects.get(did=i)
    student.delete()
    return redirect('show_dept')

def updatestud(request,i):
    student=Student.objects.get(id=i)
    form=StudentForm(instance=student)
    if request.method == 'POST':
        form=StudentForm(request.POST,instance=student)
        if form.is_valid():
            form.save()
            return redirect('show_stud')
    template_name='add.html'
    context={'form':form}
    return render(request,template_name,context)

def updatepro(request,i):
    student=Prof.objects.get(id=i)
    form=ProfForm(instance=student)
    if request.method == 'POST':
        form=ProfForm(request.POST,instance=student)
        if form.is_valid():
            form.save()
            return redirect('show_prof')
    template_name='add.html'
    context={'form':form}
    return render(request,template_name,context)

def updatedep(request,i):
    student=Dept.objects.get(did=i)
    form=DeptForm(instance=student)
    if request.method == 'POST':
        form=DeptForm(request.POST,instance=student)
        if form.is_valid():
            form.save()
            return redirect('show_dept')
    template_name='add.html'
    context={'form':form}
    return render(request,template_name,context)

