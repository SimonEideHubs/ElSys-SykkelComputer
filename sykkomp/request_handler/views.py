from django.shortcuts import render
from django.http import HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt
from .models import CycleTimes

# Create your views here.

@csrf_exempt
def index(request):
    if request.method == 'POST':
        request_data = json.loads(request.body)
        ct = CycleTimes(last_data=request_data["time"])
        data = {"time": ct.last_data}
        print("Request Data:", request_data)
        print("Persistent Data: ", data)
    else:
        ct = CycleTimes()
        data = {"time": ct.last_data}
    return HttpResponse(data)
