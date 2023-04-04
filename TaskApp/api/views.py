
from django.shortcuts import render
from rest_framework.response import Response
from api.serializers import UserSerializer,TaskSerizlizer
from django.contrib.auth.models import User
from rest_framework.viewsets import ModelViewSet,ViewSet
from todo.models import Tasks
from rest_framework import authentication,permissions


class UserView(ModelViewSet):
    serializer_class=UserSerializer
    queryset=User.objects.all()

class TasksView(ModelViewSet):
    serializer_class=TaskSerizlizer
    queryset=Tasks.objects.all()
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]
    http_method_names=["get","post"]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    
    def list(self,request,*args,**kwargs):
        qs=Tasks.objects.filter(user=request.user)
        serializer=TaskSerizlizer(qs,many=True)
        return Response(data=serializer.data)
    
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet



class IsOwnerOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user == obj.user

class TaskDetailView(GenericViewSet,mixins.DestroyModelMixin):
    serializer_class=TaskSerizlizer
    queryset=Tasks.objects.all()
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[IsOwnerOrReadOnly]

    http_method_names=["delete","put"] 

    
    # def destroy(self, request, *args, **kwargs):
    #     id=kwargs.get("pk") 
    #     obj=Tasks.objects.get(id=id)
    #     if obj.user == request.user:
    #         return super().destroy(request, *args, **kwargs)
    #     else:
    #         return Response(data="not able to perform this operation")

    # def retrieve(self,request,*args,**kwargs):
        # id=kwargs.get("pk")
        # obj=Tasks.objects.get(id=id)
        # serializer=TaskSerizlizer(obj,many=False)
        # return Response(data=serializer.data)
    
    # def update(self,request,*args,**kwargs):
    #     id=kwargs.get("pk")
    #     obj=Tasks.objects.get(id=id)
    #     serializer=TaskSerizlizer(instance=obj,data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(data=serializer.data)
    #     else:
    #         return Response(data=serializer.errors)
        
    # def destroy(self,request,*args,**kwargs):
    #     id=kwargs.get("pk")
    #     Tasks.objects.get(id=id).delete()
    #     return Response(data="deleted")

class UserView(ModelViewSet):
    serializer_class=UserSerializer
    model=User
    queryset=User.objects.all()