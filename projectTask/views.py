from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status 

from projectTask.models import Project, Task
from projectTask.ProjectSerializer import ProjectSerializer
from projectTask.TaskSerializer import TaskSerializer
from rest_framework.decorators import api_view


# Create your views here.
@api_view(['GET','POST','DELETE'])
def project_list(request):
    # GET list of projects, POST a new projects, DELETE all projects
    if request.method == 'GET':
        projects = Project.objects.all()
    elif request.method == 'POST':
        project_data = JSONParser().parse(request)
        project_serializer = ProjectSerializer(data=project_data)
        if project_serializer.is_valid():
            project_serializer.save()
            return JsonResponse(project_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(project_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        count = Project.objects.all().delete()
        return JsonResponse({'message': '{} Projects were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'PATCH', 'DELETE'])
def project_details(request, pk):
    # find projects by pk (id)
    try: 
        project = Project.objects.get(pk=pk) 
        if request.method == 'GET': 
            project_serializer = ProjectSerializer(project) 
            return JsonResponse(project_serializer.data) 
        elif request.method == 'PATCH':
            project_data = JSONParser().parse(request) 
            project_serializer = ProjectSerializer(project, data=project_data) 
            if project_serializer.is_valid(): 
                project_serializer.save() 
                return JsonResponse(project_serializer.data) 
            return JsonResponse(project_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
        elif request.method == 'DELETE': 
            project.delete() 
            return JsonResponse({'message': 'Tutorial was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)        
    except Project.DoesNotExist: 
        return JsonResponse({'message': 'The project does not exist'}, status=status.HTTP_404_NOT_FOUND) 

@api_view(['GET', 'POST', 'DELETE'])
def task_list(request,pk):
    #project = Project.objects.get(pk=pk) 
    if request.method == 'GET':
        tasks = Task.objects.filter(project__pk = pk)
        tasks_serializer = TaskSerializer(tasks, many=True)
        return JsonResponse(tasks_serializer.data, safe=False)
    elif request.method == 'POST':
        task_data = JSONParser().parse(request)
        task_data['project'] = pk
        task_serializer = TaskSerializer(data=task_data)
        if task_serializer.is_valid():
            task_serializer.save()
            return JsonResponse(task_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(task_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        count = Task.objects.all().delete()
        return JsonResponse({'message': '{} Projects were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
 
api_view(['GET', 'PATCH', 'DELETE'])
def task_details(request, pk, tk):
    # find tutorial by pk (id)
    try: 
        #project = Project.objects.get(pk=pk)
        task = Task.objects.get(pk = tk)
        if request.method == 'GET': 
            task_serializer = TaskSerializer(task) 
            return JsonResponse(task_serializer.data) 
        elif request.method == 'PATCH':
            task_data = JSONParser().parse(request) 
            task_serializer = TaskSerializer(project, data=task_data) 
            if task_serializer.is_valid(): 
                task_serializer.save() 
                return JsonResponse(task_serializer.data) 
            return JsonResponse(task_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
        elif request.method == 'DELETE': 
            task.delete() 
            return JsonResponse({'message': 'Task was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)    
    except Project.DoesNotExist: 
        return JsonResponse({'message': 'The Task does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    # GET / PUT / DELETE tutorial
