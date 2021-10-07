from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.serializers import Serializer
from .serializers import RegistrationSerializer, \
    ActivationSerializer, LoginSerializer
from rest_framework.views import APIView
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from .permissions import IsActivePermission

class RegistrationView(APIView):

    def post(self, request):
        data = request.data
        serializer = RegistrationSerializer(
            data=data
        )
        if serializer.is_valid(raise_exception=True):
            serializer.create(serializer.validated_data)
            return Response(
                "Account creation success", status=201
            )


class ActivationView(APIView):

    def post(self, request):
        serializer = ActivationSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.activate()
            return Response(
                "Account successfully activated", status=200
            )
            

class LoginView(ObtainAuthToken):
    serializer_class = LoginSerializer
    
#! если вам нужно передать request в serializers, то можно переопределить get_serializer_context & get_serializer

class LogoutView(APIView):
    permission_classes = [IsActivePermission]
    
    def post(self, request):
        user = request.user
        Token.objects.filter(user=user).delete()
        return Response("Logged out")