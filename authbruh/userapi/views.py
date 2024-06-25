from django.contrib.auth import get_user_model, login, logout
from rest_framework.authentication import SessionAuthentication
from rest_framework.views import APIView
from rest_framework import permissions, status
from .serializers import userloginserializer, userregisterserializer, userserializer
from rest_framework.response import Response


class UserRegister(APIView):
    permission_classes = (permissions.AllowAny,)
    def post(self, request):
        serializer = userregisterserializer(request.data)
        if serializer.is_valid(raise_exception = True):
            user = serializer.create(request)
            if user: 
                return Response({"message": "Done."}, status=status.HTTP_201_CREATED) 
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

class UserLogin(APIView):
    permission_classes = (permissions.AllowAny,)
    authentication_classes = (SessionAuthentication,)
    def post(self, request):
        data = request.data
        serializers = userloginserializer(data)
        if serializers.is_valid(raise_exceptions = True):
            user = serializers.check_user(data)
            login(request, user)
            return Response(serializers.data, status=status.HTTP_200_OK)

class UserLogOut(APIView):
    def post(self, request):
        logout(request)
        return Response(status=status.HTTP_200_OK)

class UserView(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = (SessionAuthentication,)
    def get(self, request):
        result = userserializer(request.user)
        return Response({'user':result.data}, status= status.HTTP_200_OK)