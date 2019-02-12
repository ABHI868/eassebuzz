from django.shortcuts import render
from school.models import Student,Classroom,Faculty,Profile
from django.views import generic
from django.views.generic.edit import CreateView,DeleteView
from django.urls import reverse_lazy
from .forms import editProfileForm
from django.contrib.auth.decorators import login_required

@login_required
def editprofile(request):
    if request.method == 'POST':
        form = editProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect ("/login/")
    else:
        form=editProfileForm(instance=request.user)
        args={'form':form}
        return render(request,'school/editprofile.html',args)
        
def profile(request):
    args={'user':request.user}
    print(request.user.first_name)
    return render(request,"school/profile.html",args)

class CreateProfile(CreateView):
    model=Profile
    fields='__all__'

class StudentCreate(CreateView):
    model=Student
    fields="__all__"
    template_name='school/student_form.html'

class StudentDeleteView(DeleteView):
    model=Student
    template_name='school/student_detail.html'
    

def index(request):
    num_students=Student.objects.count()
    num_faculty=Faculty.objects.count()
    num_classroom=Classroom.objects.count()

    context = {
    'num_students': num_students,
    'num_faculty': num_faculty,
    'num_classroom': num_classroom,
   
    }
    return render(request,'school/index.html',context=context)

class StudentListView(generic.ListView):
    model=Student
    context_object_name="student_list"
    queryset=Student.objects.all()[:10]
    template_name="school/student_list.html"

class StudentDetailView(generic.DetailView):
    model=Student
    template_name="school/student_detail.html"

class FacultyListView(generic.ListView):
    model=Student
    context_object_name="faculty_list"
    queryset=Faculty.objects.all()[:10]
    template_name="school/faculty_list.html"

