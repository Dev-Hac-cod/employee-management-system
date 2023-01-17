from cProfile import label
from dataclasses import field
from statistics import mode
from django import forms
from .models import Employee

class EmployeeFrom(forms.ModelForm):

    class Meta:
        model = Employee
        fields = ('fullname','Email','Address','mobile','emp_code','position')
        labels = {
            'fullname':'Full Name',
            'emp_code':'Sex',
            'position':'HighestQualification'
        }

    def __init__(self,*args,**kwargs):
        super(EmployeeFrom,self).__init__(*args,**kwargs)
        self.fields['position'].empty_label= "Select"
        self.fields['emp_code'].required = False
        self.fields['position'].required = False
