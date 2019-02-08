from django.shortcuts import render
from school.models import Student,Classroom,Faculty
from django.views import generic

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

