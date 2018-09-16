from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('admin_login/', views.admin_login),
    path('validateUser', views.validateUser),
    path('student', views.sign_up_student),
    path('parent', views.sign_up_parent),
    path('addTeacher',views.addteacher),
    path('addDepartment',views.adddepartment),
    path('addSubject',views.addsubject),
    path('addCourse',views.addcourse),
    path('addStudent',views.addStudent),

    #path('super_operations',views.super_operations)

]
