
from django.urls import path
from .import views
from django.contrib.auth.views import LoginView,LogoutView
urlpatterns = [
    path('', views.index, name='index'), 
    path('students/', views.StudentListView.as_view(), name='student-list'), 
    path('register/',views.CreateProfile.as_view(),name='create-profile'),      
    path('login/',LoginView.as_view(template_name="school/login.html"),name="login"), 
    path('accounts/profile',views.profile,name='profile'),
    path('edit_profile',views.editprofile,name='edit-profile'),
    path('logout/',LogoutView.as_view(),name="logout"),
    path('faculty/', views.FacultyListView.as_view(), name='faculty-list'), 
    path('student/create/', views.StudentCreate.as_view(), name='student_create'), 
    path('student/<int:pk>', views.StudentDetailView.as_view(), name='student-detail'),
]