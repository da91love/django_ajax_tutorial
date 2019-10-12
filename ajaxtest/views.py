from django.shortcuts import render
from django.http import HttpResponse
import json

# Create your views here.


def show_page(request):
    return render(request, 'ajaxtest/ajaxtest.html')

def respond_to_ajax(request):
    try:
        if request.is_ajax():
            if request.method == 'POST':
                data = json.loads(request.body) #request.body is byte
        return HttpResponse(json.dumps(data), content_type="application/json")

    except Exception as e:
        return e
