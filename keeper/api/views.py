from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django.core import serializers
from rest_framework.views import APIView
from django.db.models import Sum

from keeper.api.serializers import KeeperListSerializer, KeeperCreateSerializer, ProjectListSerializer, ProjectCreateSerializer, UserListSerializer
from keeper.models import Keeper, Project, User, ProjectIncome


class TaskAPIView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        query = Keeper.objects.all()
        serializer = KeeperListSerializer(query, many=True) 

        resp = {
            'status': 'true',
            'message': 'successful',
            'payload': serializer.data         
        }
        response = Response(data=resp, status=status.HTTP_200_OK)
        return response
    
    def post(self, request, *args, **kwargs):
        serializer = KeeperCreateSerializer(data=request.data)
        serializer.initial_data['assignee'] = User.objects.get(username=serializer.initial_data['assignee']).id
        print(serializer.initial_data['assignee'])

        if serializer.is_valid():
            # serializer.data['assignee'] = User.objects.get(username=serializer.initial_data['assignee'])
            #print(serializer.data['assignee'])
            serializer.save()
            resp = {
                'status': 'true',
                'message': 'successful',
                'payload': serializer.data         
            }
            response = Response(data=resp, status=status.HTTP_201_CREATED)
            return response
        resp = {
                'status': 'false',
                'message': 'error',
                'payload': serializer.errors    
        }
        return Response(data=resp, status=status.HTTP_400_BAD_REQUEST)

class MyTaskAPIView(APIView):
    permission_classes = [AllowAny]
    
    def post(self, request, *args, **kwargs):
        query = Keeper.objects.filter(assignee=request.data['username'], status=False)
        serializer = KeeperListSerializer(query, many=True) 

        resp = {
            'status': 'true',
            'message': 'successful',
            'payload': serializer.data         
        }
        response = Response(data=resp, status=status.HTTP_200_OK)
        return response


class ProjectAPIView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        query = Project.objects.all().order_by('name')  
        serializer = ProjectListSerializer(query, many=True)

        resp = {
            'status': 'true',
            'message': 'successful',
            'payload': serializer.data         
        }
        response = Response(data=resp, status=status.HTTP_200_OK)
        return response
    
    def post(self, request, *args, **kwargs):
        serializer = ProjectCreateSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            resp = {
                'status': 'true',
                'message': 'successful',
                'payload': serializer.data         
            }
            response = Response(data=resp, status=status.HTTP_201_CREATED)
            return response
        resp = {
                'status': 'false',
                'message': 'error',
                'payload': serializer.errors    
        }
        return Response(data=resp, status=status.HTTP_400_BAD_REQUEST)
    

class UserAPIView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        query = User.objects.all()
        serializer = UserListSerializer(query, many=True)

        resp = {
            'status': 'true',
            'message': 'successful',
            'payload': serializer.data         
        }
        response = Response(data=resp, status=status.HTTP_200_OK)
        return response
    

class DashboardAPIView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        user_count = User.objects.count()
        project_count = Project.objects.count()
        task_count = Keeper.objects.count()
        task_count_completed = Keeper.objects.filter(status=True).count()

        projects = Project.objects.all().order_by('-created_at')[:5]
        project_query = ProjectListSerializer(projects, many=True)

        tasks = Keeper.objects.all().order_by('-created_at')[:5]
        task_query = KeeperListSerializer(tasks, many=True)

        users = User.objects.all().order_by('-date_joined')[:5]
        user_query = UserListSerializer(users, many=True)

        incomes = ProjectIncome.objects.all()
        income = incomes.aggregate(total=Sum('amount'))['total'] or 0

        payload = {
            'usersCount': user_count,
            'projectsCount': project_count,
            'tasksCount': task_count,
            'tasksCountCompleted': task_count_completed,
            'projects': project_query.data,
            'tasks': task_query.data,
            'users': user_query.data,
            'income': income
        }

        resp = {
            'status': 'true',
            'message': 'successful',
            'payload': payload         
        }
        response = Response(data=resp, status=status.HTTP_200_OK)
        return response
    