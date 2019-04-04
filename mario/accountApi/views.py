from django.shortcuts import render
from mario.accountApi.serializers import UserSerializer
from django.contrib.auth.models import User
from rest_framework import viewsets, status
from rest_framework.decorators import api_view

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.

    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    # authentication_classes = (TokenAuthentication, SessionAuthentication)
    # permission_classes = (IsAuthenticated,)

