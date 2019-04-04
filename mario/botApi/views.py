from django.shortcuts import render
from mario.botApi.serializers import BotSerializer
from rest_framework import viewsets
from .models import Bot
from rest_framework.decorators import api_view
from django.utils import timezone
from rest_framework.response import Response
from rest_framework import status
import requests

# Create your views here.
class BotViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Bot.objects.all()
    serializer_class = BotSerializer


@api_view(['POST'])
def create_bot(request):
    # ----- YAML below for Swagger -----
    """
    description: This API deletes/uninstalls a device.
    parameters:
      - name: name
        type: string
        required: true
        location: form
      - name: language
        type: string
        required: true
        location: form
      - name: icon
        type: string
        required: true
        location: form
    """
    name = request.POST.get('name')
    language = request.POST.get('language')
    icon = request.POST.get('icon')
    try:
        Bot.objects.create(name=name, language=language, icon=icon)
        return Response("Data Saved!", status=status.HTTP_201_CREATED)
    except Exception as ex:
        return Response(ex, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_bot(request):
    return Response(Bot.objects.all().values(), status=status.HTTP_200_OK)



"""
driver_firstname = request.POST['driver_firstname']
driver_lastname = request.POST['driver_lastname']
driver_email = request.POST['driver_email']

payload = {'driver.driver_firstname': driver_firstname,
           'driver.driver_lastname': driver_lastname,
           'driver.driver_email': driver_email
           }

r = requests.post("http://your-url.org/post", data=payload)

"""