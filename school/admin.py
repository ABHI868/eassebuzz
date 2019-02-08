from django.contrib import admin
from school.models import Student,Faculty,Classroom,Profile
# Register your models here.
admin.site.register(Faculty)
admin.site.register(Student)

admin.site.register(Profile)
admin.site.register(Classroom)