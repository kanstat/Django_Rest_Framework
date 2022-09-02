import json
from django.shortcuts import render
import io

from rest_framework.parsers import JSONParser
from .serializers import UserSerializer
from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer
from django.views.decorators.csrf import csrf_exempt
# Create your views here.


@csrf_exempt
def UserCreate(request):
    if request.method == "POST":
        jsondata = request.body
        print(jsondata)
        # coverting into string...
        stream = io.BytesIO(jsondata)
        # converting it into python data
        pythondata = JSONParser().parse(stream)
        # converting it into complex data
        serializer = UserSerializer(data=pythondata)
        if serializer.is_valid():
            serializer.save()
            res = {"msg": "Data Added Sucessfully"}
            jsondata = JSONRenderer().render(res)
            return HttpResponse(jsondata, content_type='application\json')
        jsondata = JSONRenderer().render(serializer.errors)
