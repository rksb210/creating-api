from django.shortcuts import render
from .models import Task
from .serializer import TaskSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def tasklist(request):
    task = Task.objects.all()
    serializer = TaskSerializer(task, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def taskdetail(request,pk):
    task = Task.objects.get(id=pk)
    serializer = TaskSerializer(task, many=False)
    return Response(serializer.data)



@api_view(['POST'])
def taskcreate(request):   
    serializer = TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def taskupdate(request,pk):
    task = Task.objects.get(id=pk)   
    serializer = TaskSerializer(instance=task,data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
# Create your views here.



@api_view(['DELETE'])
def taskdelete(request,pk):
    task = Task.objects.get(id=pk)   
    task.delete()
    return Response('item deleted')





@api_view(['GET'])
def imageupload(request):
    task = Task.objects.all()
    serializer = TaskSerializer(task, many=True)
    return Response(serializer.data)


@api_view(['PUT'])
def imageupdate(request,pk):
    task = Task.objects.get(id=pk)
    task.photo = request.data['photo']
    task.save()
    serializer = TaskSerializer(task)
    
    return Response(serializer.data)