from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserSerializer
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

@api_view(['POST'])
def login(request):
    user = get_object_or_404(User, username = request.data['username']) #returns 404 if user not there
    if not user.check_password(request.data['password']): #if password not there. 
        return Response({'details': 'the password is not correct'}, status= status.HTTP_400_BAD_REQUEST)
    token, created = Token.objects.get_or_create(user = user)
    serializer = UserSerializer(instance=user)
    return Response({"Token": token.key, "User": serializer.data})

@api_view(['POST'])
def signin(request):
    serializer = UserSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save() #Creates the user
        user = User.objects.get(username = request.data['username']) #Fetches that username
        user.set_password(request.data['password']) #this will hash it. 
        user.save() 
        token = Token.objects.create(user = user) #creates an token for that user
        return Response({"Token": token.key, "User": serializer.data}, status = status.HTTP_200_OK) #and returns their data. 
    return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated

@api_view(['GET'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def test(request):
    return Response('Passed for' + str(request.user) + str(request.user.id))

@api_view(['POST'])
@authentication_classes([TokenAuthentication])
def logout(request):
    try: 
        request.user.auth_token.delete()
    except AttributeError:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    return Response({"Details": "Deleted"} , status=status.HTTP_200_OK)

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def fetch_user_data(request):
    user = request.user
    serializer = UserSerializer(user)
    return Response(serializer.data)
