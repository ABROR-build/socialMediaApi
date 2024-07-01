from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate, login, logout

# local
from . import serializers


class Registration(APIView):
    def post(self, request):
        register_serializer = serializers.RegisterSerializer(data=request.data)
        if register_serializer.is_valid():
            register_serializer.save()
            return Response(f"{register_serializer.data} successfully created", status=status.HTTP_201_CREATED)
        else:
            return Response(register_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Login(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return Response({"detail": "Logged in successfully"}, status=status.HTTP_200_OK)
        else:
            return Response({"detail": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)


class Logout(APIView):
    def post(self, request):
        logout(request)
        return Response({"detail": "Logged out successfully"}, status=status.HTTP_200_OK)
