from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .signals import send_test_signal

def test_signal_view(request):
    send_test_signal()
    return HttpResponse("Signal test completed. Check your console output.")