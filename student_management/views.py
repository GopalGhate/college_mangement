from django.shortcuts import render
from django.template import Context,loader
from django.http import HttpResponse,JsonResponse
from .models  import User_master
from .models import Teacher,Department,Institute, Course, Subject, Student, Parent
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.

def admin_login(request):
    template = loader.get_template('admin_login.html')
    return HttpResponse(template.render({},request))

def validateUser(request):
    #template = loader.get_template('super_admin_next.html')
    username1=request.POST.get('user')
    password1=request.POST.get('pwd')


    try:
        umaster = User_master.objects.get(user_name=username1,password=password1)
        if  umaster.type=="super":
            template = loader.get_template('super_admin_next.html')
            return HttpResponse(template.render({}, request))
        elif umaster.type=="Teacher":
            template = loader.get_template('teacher_next.html')
            return HttpResponse(template.render({}, request))

    except ObjectDoesNotExist:
       return HttpResponse("NOK");


def sign_up_student(request):
    template = loader.get_template('student_transaction.html')
    return HttpResponse(template.render({},request))

def sign_up_parent(request):
    template = loader.get_template('parent_master.html')
    return HttpResponse(template.render({},request))

# Add Teacher into database
def addteacher(request):
    name = request.POST.get('teacherName')
    type = "Teacher"
    user_name = request.POST.get('userName')
    password = request.POST.get('password')
    user = User_master()
    user.name = name
    user.user_name = user_name
    user.password = password
    user.type = type
    teacher = Teacher()
    teacher.Teacher_name = name
    teacher.user_name = user_name
    teacher.password = password
    department = request.POST.get('DepartmentName')
    deapartmentInstance = Department.objects.get(Department_name=department)
    teacher.department = deapartmentInstance;
    teacher.institute = Institute.objects.get(Institute_Code=6006)
    user.save()
    teacher.user = user
    teacher.save()
    return HttpResponse("Added")

def adddepartment(request):
    department =Department()
    department.Department_name = request.POST.get('departmentName')
    department.Department_type = request.POST.get('departmentType')
    department.Department_hod = request.POST.get('departmentHod')
    department.institute = Institute.objects.get(Institute_Code=6006)
    department.save()
    return HttpResponse("Department Added")

def addcourse(request):
    course = Course()
    course.course_name = request.POST.get('courseName')
    course.course_code = request.POST.get('courseCode')
    department = request.POST.get('CourseDepartmentName')
    deapartmentInstance = Department.objects.get(Department_name = department)
    course.department = deapartmentInstance;
    course.save()
    return HttpResponse("Course Added")

def addsubject(request):
    subject = Subject()
    subject.subject_name = request.POST.get('subjectName')
    subject.subject_code = request.POST.get('subjectCode')
    subject.min_passing = request.POST.get('minMarks')
    subject.total_marks = request.POST.get('totalMarks')
    subject.save()
    return HttpResponse("Subject Added")

def addStudent(request):
    try:

        student = Student()
        parent = Parent()
        parent.name = request.POST.get('parentName')
        parent.user_name = request.POST.get('parentuserName')
        parent.password = request.POST.get('parentPassword')
        parent.Contact_no = request.POST.get('contactInfo')
        parent.parent_code = request.POST.get('parentCode')
        parent.save()
        student.parent = parent
        student.name = request.POST.get('StudentName')
        student.user_name = request.POST.get('userName')
        student.password = request.POST.get('password')
        student.Roll_no = request.POST.get('rollNo')
        instancedept = request.POST.get('DepartmentName')
        DeptInstance = Department.objects.get(Department_name = instancedept)
        student.department= DeptInstance
        instanceCourse = request.POST.get('CourseName')
        CourseInstance = Course.objects.get(course_name = instanceCourse)
        student.course = CourseInstance
        student.save()
        return HttpResponse("OK")
    except Exception as e:
     return HttpResponse(str(e))





