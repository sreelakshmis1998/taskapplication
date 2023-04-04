from django.shortcuts import render,redirect
from django.views.generic import View,TemplateView,CreateView,ListView,DetailView,UpdateView
from todo.forms import TasksForm,RegistrationForm,LoginForm,VehicleForm
from todo.models import Tasks,Vehicle
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse_lazy

# Create your views here.

from django import forms

class IndexView(TemplateView):
    template_name="index.html"

class TaskCreateView(View):
    def get(self,request,*args,**kwargs):
        form=TasksForm()
        return render(request,"task-add.html",{"form":form})    
    def post(self,request,*args,**kwargs):
        form=TasksForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"task has been added")
            print("record saved")
            return redirect("task-list")
        else:
            messages.error(request,"failed")
            return render(request,"task-add.html",{"form":form})


class TaskListView(View):
    def get(self,request,*args,**kwargs):
        qs=Tasks.objects.all()
        return render(request,"task-list.html",{"tasks":qs})


class TaskDetailView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        qs=Tasks.objects.get(id=id)
        return render(request,"task-detail.html",{"task":qs})

class TaskDeleteView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        Tasks.objects.get(id=id).delete()
        messages.success(request,"task has been removed")
        return redirect ("task-list")


class TaskEditView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        obj=Tasks.objects.get(id=id)
        form=TasksForm(instance=obj)
        return render(request,"task-edit.html",{"form":form})
    def post(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        obj=Tasks.objects.get(id=id)
        form=TasksForm(request.POST,instance=obj,files=request.FILES)
        if form.is_valid():
            form.save()
            # Employees.objects.filter(id=id).update(**form.cleaned_data)
            print("record saved")
            return redirect("task-list")
        else:
            return render(request,"task-edit.html",{"form":form})

class TaskHomeView(TemplateView):
    template_name="taskhome.html"




class RegistrationView(View):
    def get(self,request,*args,**kwargs):
        form=RegistrationForm()
        return render(request,"registration.html",{"form":form})
    def post(self,request,*args,**kwargs):
        form=RegistrationForm(request.POST)
        if form.is_valid():
            #form.save()
            User.objects.create_user(**form.cleaned_data)
            messages.success(request,"sucessfully registered")
            return redirect("home")
        else:
            messages.error(request,"registration failed")
            return render(request,"registration.html",{"form":form})



class SignInView(View):
    def get(self,request,*args,**kwargs):
        form=LoginForm()
        return render(request,"login.html",{"form":form})
    def post(self,request,*args,**kwargs):
        form=LoginForm(request.POST)
        if form.is_valid():
            #form.save()
            uname=form.cleaned_data.get("username")
            pwd=form.cleaned_data.get("password")
            usr=authenticate(request,username=uname,password=pwd)
            if usr:
                login(request,usr)
                print(request.user)
                messages.success(request,"logined successfully")
                return redirect("home")
            else:
                messages.error(request,"invalid credentials")
                return render(request,"login.html",{"form":form})


class SignOutView(View):
      def get(self,request,*args,**kwargs):
        logout(request)
        return redirect("signin")


class VehicleCreateView(CreateView):
    model=Vehicle
    form_class=VehicleForm
    template_name="vehicle-add.html"
    success_url=reverse_lazy("vehicle-list")

class VehicleListView(ListView):
    model=Vehicle
    context_object_name="vehicle"
    template_name="vehicle-list.html"


class VehicleDetailView(DetailView):
    model=Vehicle
    context_object_name="vehicle"
    template_name="vehicle-detail.html"

def vehicle_delete_view(request,*args,**kwargs):
    id=kwargs.get("pk")
    Vehicle.objects.get(id=id).delete()
    return redirect ("vehicle-list")

class VehicleEditView(UpdateView):
    model=Vehicle
    form_class=VehicleForm
    template_name="vehicle-edit.html"
    success_url=reverse_lazy("vehicle-list")


class VehicleHomeView(TemplateView):
    template_name="vehiclehome.html"