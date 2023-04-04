from django import forms
from todo.models import Tasks,Vehicle
from django.contrib.auth.models import User

class TasksForm(forms.ModelForm):
    class Meta:
        model=Tasks
        exclude=("status",)

        widgets={
            "task_name":forms.TextInput(attrs={"class":"form-control"}),
            "user":forms.TextInput(attrs={"class":"form-control"}),
        }
        
        def __str__(self):
            return self.task_name

class RegistrationForm(forms.ModelForm):
    class Meta:#imp if we are using model form
        model=User
        fields=["first_name","last_name","username","password","email"]
        
        widgets={
            "first_name":forms.TextInput(attrs={"class":"form-control"}),
            "last_name":forms.TextInput(attrs={"class":"form-control"}),
            "username":forms.TextInput(attrs={"class":"form-control"}),
            "password":forms.TextInput(attrs={"class":"form-control"}),
            "email":forms.TextInput(attrs={"class":"form-control"}),
        }

class VehicleForm(forms.ModelForm):
    class Meta:
        model=Vehicle
        exclude=("",)
        widgets={
            "vehicle_name":forms.TextInput(attrs={"class":"form-control"}),
            "vehicle_number":forms.TextInput(attrs={"class":"form-control"}),
            "model":forms.TextInput(attrs={"class":"form-control"}),
            "owner":forms.TextInput(attrs={"class":"form-control"}),
            "km_driven":forms.NumberInput(attrs={"class":"form-control"}),
            "purchase_date":forms.DateInput(attrs={"class":"form-control","type":"date"}),
            "fuel_type":forms.Select(attrs={"class":"form-select"}),
        }


class LoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField()