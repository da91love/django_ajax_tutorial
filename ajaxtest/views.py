from django.shortcuts import render
from django.http import HttpResponse
import json

# Create your views here.


def show_page(request):
    return render(request, 'ajaxtest/ajaxtest.html')

def respond_to_ajax(request):
    input_text = request.POST.get('data')

    return HttpResponse(
                json.dumps({'data':input_text}),
                content_type="application/json"
            )