from django.shortcuts import render
from django.http import Http404
from django.views.decorators.csrf import csrf_exempt
from .models import CycleTimes

# Create your views here.

@csrf_exempt
def index(request):
    ct = CycleTimes()
    if request.method == 'POST':
        request_data = request.body
        ct = CycleTimes(last_data=request_data)
        ct.save()
    try:
        ct = CycleTimes.objects.order_by('id')[0]
    except CycleTimes.objects[0].DoesNotExist:
        raise Http404("No entry for cycle times were found")
    data = {"time": ct.last_data}
    print("Persistent Data: ", ct.last_data)
    return render(request, 'request_handler/index.html', data)
