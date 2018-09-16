from django.db import models

# Create your models here.
from django.db import models

class Institute(models.Model):
    Institute_name = models.CharField(max_length=200)
    Contact_info = models.CharField(max_length=200)
    Institute_Code=models.IntegerField();
class Department(models.Model):


    institute= models.ForeignKey(Institute,on_delete=models.CASCADE)
    Department_name = models.CharField(max_length=200)
    Department_type = models.CharField(max_length=200)
    Department_hod = models.CharField(max_length=200)


class User_master(models.Model):
    name = models.CharField(max_length=200)
    type = models.CharField(max_length=200)
    user_name = models.CharField(max_length=200)
    password = models.CharField(max_length=200)

class Teacher(models.Model):

    user_name = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    institute = models.ForeignKey(Institute,on_delete=models.CASCADE)
    department = models.ForeignKey(Department,on_delete=models.CASCADE)
    Teacher_name = models.CharField(max_length=200)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    user = models.ForeignKey(User_master,on_delete=models.CASCADE)

class Course(models.Model):
    course_code = models.IntegerField()
    course_name = models.CharField(max_length=200)
    department = models.ForeignKey(Department,on_delete=models.CASCADE)

class Subject(models.Model):
    subject_name = models.CharField(max_length=200)
    subject_code = models.CharField(max_length=200)
    min_passing = models.IntegerField()
    total_marks = models.IntegerField()

class Parent(models.Model):
    name = models.CharField(max_length=200)
    Contact_no = models.CharField(max_length=200)
    parent_code = models.CharField(max_length=200)
    user_name = models.CharField(max_length=200)
    password = models.CharField(max_length=200)

class Student(models.Model):
    name = models.CharField(max_length=200)
    Roll_no = models.IntegerField()
    parent = models.ForeignKey(Parent,on_delete=models.CASCADE)
    user_name = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    course = models.ForeignKey(Course,on_delete=models.CASCADE)
   # subject = models.ForeignKey(Subject, on_delete=models.CASCADE)



