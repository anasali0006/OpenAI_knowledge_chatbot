from django.shortcuts import render
from rest_framework.views import APIView
from django.http import HttpResponse

# Create your views here.


class ChatbotHealthCheck(APIView):
    def get(cls, request):
        return HttpResponse("Request Arrived in Django Successfully", content_type="text/plain")


class ChatbotRequestHandler(APIView):

    @classmethod
    def get(cls, request):
        print("Sanity Check")
        pass

