
from django.contrib import admin
from django.urls import include,path

urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'admin_login/', include('student_management.urls')),
    path(r'validate/', include('student_management.urls')),
    path(r'sign_up_student/', include('student_management.urls')),
    path(r'sign_up_parent/', include('student_management.urls')),
    path(r'add/',include('student_management.urls')),
    #path(r'super_next/', include('student_management.urls')),
]
