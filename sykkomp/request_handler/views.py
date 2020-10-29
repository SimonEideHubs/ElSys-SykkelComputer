from django.shortcuts import render
from django.http import HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

@csrf_exempt
def index(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        return render(request, "request_handler/index.html", data)
    else:
        return HttpResponse("2. Get request")