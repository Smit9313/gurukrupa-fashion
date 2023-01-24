from django.shortcuts import render
import json
from bson import json_util
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# Create your views here.
from pymongo import MongoClient
from .serializers import MyModelSerializer
from rest_framework import viewsets

client = MongoClient()
db = client.appdb

@csrf_exempt
def my_view(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        db.demo_demo.insert_one(data)
        return JsonResponse({"message":"Data inserted Successfully!"},status=201)
    else:
        data = list(db.demo_demo.find())
        data = json.loads(json_util.dumps(data))
        return JsonResponse(data, safe=False)


class MyModelViewSet(viewsets.ModelViewSet):
    serializer_class = MyModelSerializer

    def get_queryset(self):
        return db.demo_demo.find()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        validated_data = serializer.validated_data
        db.demo_demo.insert_one(validated_data)
        return Response(status=status.HTTP_201_CREATED)