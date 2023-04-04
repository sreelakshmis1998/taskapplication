"""TaskApplication URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from rest_framework.authtoken.views import ObtainAuthToken
from todo import views
from api import views as api_views
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
router=DefaultRouter()
router.register("api/users",api_views.UserView,basename="users")
router.register("api/tasks",api_views.TasksView,basename="tasks")
router.register("api/todo",api_views.TasksView,basename="todo")



urlpatterns = [
    path('admin/', admin.site.urls),
    path("todo/add",views.TaskCreateView.as_view(),name="task-add"),
    path("",views.IndexView.as_view(),name="home"),
    path("tasks/all",views.TaskListView.as_view(),name="task-list"),
    path("tasks/<int:pk>",views.TaskDetailView.as_view(),name="task-detail"),
    path("tasks/remove/<int:pk>",views.TaskDeleteView.as_view(),name="task-delete"),
    path("tasks/change/<int:pk>",views.TaskEditView.as_view(),name="task-edit"),
    path("registration/",views.RegistrationView.as_view(),name="registration"),
    path("signin",views.SignInView.as_view(),name="signin"),
    path("signout",views.SignInView.as_view(),name="signout"),
    path("taskhome",views.TaskHomeView.as_view(),name="taskhome"),
    path("vehicle/add",views.VehicleCreateView.as_view(),name="vehicle-add"),
    path("vehicle/all",views.VehicleListView.as_view(),name="vehicle-list"),
    path("vehicle/<int:pk>",views.VehicleDetailView.as_view(),name="vehicle-detail"),
    path("vehicle/remove/<int:pk>",views.vehicle_delete_view,name="vehicle-delete"),
    path("vehicle/change/<int:pk>",views.VehicleEditView.as_view(),name="vehicle-edit"),
    path("vehiclehome",views.VehicleHomeView.as_view(),name="vehiclehome"),
    path("api/token/",ObtainAuthToken.as_view())


]+router.urls
