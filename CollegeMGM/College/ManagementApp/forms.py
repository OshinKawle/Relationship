from django import forms
from . models import Dept,Student,Prof

class DeptForm(forms.ModelForm):
    class Meta:
        model = Dept
        fields = '__all__'


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'

class ProfForm(forms.ModelForm):
    class Meta:
        model = Prof
        fields = '__all__'

