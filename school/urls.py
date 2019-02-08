
from django.urls import path
from .import views
urlpatterns = [
    path('', views.index, name='index'), 
    path('students/', views.StudentListView.as_view(), name='student-list'),   
    path('faculty/', views.FacultyListView.as_view(), name='faculty-list'), 
    path('student/create/', views.StudentCreate.as_view(), name='student_create'), 

    path('student/<int:pk>', views.StudentDetailView.as_view(), name='student-detail'),
]