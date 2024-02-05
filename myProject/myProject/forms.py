from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from myApp.models import customUser
from myApp.models import *


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = customUser
        fields = UserCreationForm.Meta.fields + ('city', 'user_type')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        for field_name in self.fields:
            self.fields[field_name].help_text = None

class CustomAuthenticationForm(AuthenticationForm):
    class Meta:
        model = customUser  
        fields = ['username', 'password']


class StudentCreationForm(forms.ModelForm):

    class Meta:

        model=studentModel
        fields=['StudentName','Age','Gender','Subjects']
        
class SubjectCreationForm(forms.ModelForm):

    class Meta:

        model=SubjectModel
        fields=['SubjectName','SubjectCode','Credit']

class MarkCreationForm(forms.ModelForm):
    class Meta:
        model = MarkModel
        fields = ['student', 'subject', 'marks']

        
        


    
