from django.shortcuts import render,redirect
from myProject.forms import *
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required



def signupPage(request):

    if request.method=='POST':
        form=CustomUserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            return redirect('loginPage')
    else:
        form = CustomUserCreationForm()

    return render(request,'signupPage.html',{'form': form})


def loginPage(request):
    
    if request.method == 'POST':
        
        form = CustomAuthenticationForm(request, data=request.POST)
        
        if form.is_valid():
            
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            
            user = authenticate(request, username=username, password=password)

            if user is not None:
                
                login(request, user)
                
                return redirect('dashboardPage')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'loginPage.html', {'form': form})



def logoutPage(request):

    logout(request)

    return redirect('loginPage')

@login_required
def dashboardPage(request):


    return render(request,'dashboard.html')

def createStudenPage(request):

    if request.method=='POST':
        form=StudentCreationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("viewStudentPage")
    else:
        form=StudentCreationForm()
    return render(request,'createStudenPage.html',{'form':form})


def viewStudentPage(request):
    students = studentModel.objects.all()
    return render(request, 'viewStudentPage.html', {'students': students})

def createSubjectPage(request):
    if request.method=='POST':
        form=SubjectCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("viewSubjectPage")
    else:
        form=SubjectCreationForm()

    return render(request,'createSubjectPage.html',{'form':form})

def viewSubjectPage(request):
    subjects = SubjectModel.objects.all()
    return render(request, 'viewSubjectPage.html', {'subjects': subjects})

def inputMarksPage(request, student_id):
    student = studentModel.objects.get(id=student_id)
    subjects = SubjectModel.objects.all() 

    if request.method == 'POST':
        form = MarkCreationForm(request.POST)
        if form.is_valid():
            form.instance.student = student
            form.save()
            return redirect('viewMarksPage', student_id=student_id)
    else:
        form = MarkCreationForm(initial={'student': student, 'subjects': subjects})

    return render(request, 'inputMarksPage.html', {'form': form, 'student': student, 'subjects': subjects})

def viewMarksPage(request, student_id):
    student = studentModel.objects.get(id=student_id)
    marks = MarkModel.objects.filter(student=student)
    total_credit = 0
    total_grade_point = 0

    for mark in marks:
        subject_credit = int(mark.subject.Credit) 

        if mark.marks >= 40:
            if mark.marks >= 80:
                grade_point = 4.00
            elif mark.marks >= 75:
                grade_point = 3.75
            elif mark.marks >= 70:
                grade_point = 3.50
            elif mark.marks >= 65:
                grade_point = 3.25
            elif mark.marks >= 60:
                grade_point = 3.00
            elif mark.marks >= 55:
                grade_point = 2.75
            elif mark.marks >= 50:
                grade_point = 2.50
            elif mark.marks >= 45:
                grade_point = 2.25
            else:
                grade_point = 2.00
            total_credit += subject_credit
            total_grade_point += subject_credit * grade_point
            cgpa=total_grade_point/total_credit
            rounded_cgpa = round(cgpa, 2)

    context = {
        'student': student,
        'marks': marks,
        'total_credit': total_credit,
        'total_grade_point': total_grade_point,
        'cgpa':rounded_cgpa
    }

    return render(request, 'viewMarksPage.html', context)

def edit_student(request,student_id):
    student = studentModel.objects.get(id=student_id)
    form=StudentCreationForm(instance=student)
    
    if request.method=='POST':
        form=StudentCreationForm(request.POST,instance=student)
        form.save()
        return redirect("viewStudentPage")
    else:
        form=StudentCreationForm()
    return render (request, 'EditPage.html', {'form': form})

def delete_student(request,student_id):
    student = studentModel.objects.get(id=student_id)
    student.delete()
    return redirect("viewStudentPage")
    
def edit_Subject(request,subjects_id):
    subjects = SubjectModel.objects.get(id=subjects_id)
    form=StudentCreationForm(instance=subjects)
    
    if request.method=='POST':
        form=SubjectCreationForm(request.POST,instance=subjects)
        form.save()
        return redirect("viewSubjectPage")
    else:
        form=SubjectCreationForm()
    return render (request, 'EditsubjectsPage.html', {'form': form})

def delete_Subject(request,subjects_id):
    subjects = SubjectModel.objects.get(id=subjects_id)
    subjects.delete()
    return redirect("viewSubjectPage")
        


