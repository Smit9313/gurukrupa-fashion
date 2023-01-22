from django.shortcuts import render
import json
from bson import json_util
from pymongo import MongoClient
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

@csrf_exempt
def my_view(request):
    if request.method == 'POST':
        client = MongoClient()
        db = client['appdb']
        data = json.loads(request.body)
        db.demo_demo.insert_one(data)
        return JsonResponse({"message":"Data inserted Successfully!"},status=201)
    else:
        client = MongoClient()
        db = client['appdb']
        data = list(db.demo_demo.find())
        data = json.loads(json_util.dumps(data))
        return JsonResponse(data, safe=False)