# student/urls.py
from django.urls import path
from . import views
from .views import student_dashboard
from . import views
from .views import student_view, attendance_view
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('', views.welcome_page, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard/', student_dashboard, name='student_dashboard'),
   # path('student/', student_view, name='student_view'),
    path('student/', student_view, name='student_view'),
    path('attendance/', attendance_view, name='attendance_view'),
    path('student/', student_view, name='profile'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)