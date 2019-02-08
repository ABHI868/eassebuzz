from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user=models.OneToOneField(User ,on_delete=models.CASCADE)
    user_role=((1,'teacher'),(2,'student'))
    user_type=models.PositiveSmallIntegerField(choices=user_role,default=1)
    address=models.TextField(max_length=200, help_text="Enter current address")
    contact_no=models.IntegerField(help_text="Enter mobile number",default=0)
    
    def __str__(self):
        return self.user.username

class Student(models.Model):
    profile=models.OneToOneField(Profile,on_delete=models.CASCADE)
    category=((1,'Red'),
    (2,'Green'),
    (3,'Yellow'),
    (4,'Blue'))
    house=models.PositiveSmallIntegerField(choices=category,default=1)
    enrolement_date=models.DateTimeField(auto_now_add=True)
    age=models.IntegerField(blank=True,null=True)
   

    def __str__(self):
        return self.profile.user.username   

class Faculty(models.Model):
    profile=models.OneToOneField(Profile, on_delete=models.CASCADE)
    experience=models.IntegerField(help_text="How many years of experience",default=1)
    salary=models.FloatField(default=0)
    languages=((1,'C'), 
    (2,'C++'),
    (3,'Java'),
    (4,'Python'))
    expertise=models.PositiveSmallIntegerField(choices=languages,default=4)
    joining_date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.profile.user.username


class Classroom(models.Model):
    grade=models.IntegerField()
    student=models.ForeignKey(Student,on_delete=models.CASCADE)
    faculty=models.ManyToManyField(Faculty)

    def __str__(self):
        return str(self.grade)


# def update_faculty(sender, **kwargs):
#     if kwargs['created']:
#         faculty=Faculty.objects.create(profile=kwargs['instance'])
# post_save.connect(update_faculty,sender=Profile)


def update_student(sender, **kwargs):
    if kwargs['created']:
        student=Student.objects.create(profile=kwargs['instance'])
post_save.connect(update_student,sender=Profile)


