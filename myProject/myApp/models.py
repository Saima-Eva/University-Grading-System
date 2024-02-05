from django.db import models
from django.contrib.auth.models import AbstractUser



class customUser(AbstractUser):
    USER=[
        ('admin','Admin'),('teacher','Teacher')
    ]
    profile_pic=models.ImageField(upload_to='media/profile_pic',null=True)
    user_type=models.CharField(choices=USER,max_length=120,null=True)
    city=models.CharField(max_length=120,null=True)

    def __str__(self) -> str:
        return self.username

    
class SubjectModel(models.Model):
    SubjectName=models.CharField(max_length=120)
    SubjectCode=models.CharField(max_length=120)
    Credit=models.CharField(max_length=120)

    def __str__(self) -> str:
        return self.SubjectName+ " " +self.Credit
    
class studentModel(models.Model):

    GENDER=[
        ('male','MALE'),('female','FEMALE')
    ]
    StudentName=models.CharField(max_length=120,null=True)
    Age=models.FloatField()
    Gender=models.CharField(choices=GENDER,max_length=120,null=True)
    Subjects=models.ManyToManyField(SubjectModel)

    def __str__(self) -> str:
        return self.StudentName
    

class MarkModel(models.Model):
    student = models.ForeignKey(studentModel, on_delete=models.CASCADE)
    subject = models.ForeignKey(SubjectModel, on_delete=models.CASCADE)
    marks = models.FloatField()

    def __str__(self) -> str:
        return f"{self.student.StudentName} - {self.subject.SubjectName}: {self.marks}"

