from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.exceptions import PermissionDenied, AuthenticationFailed
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication, SessionAuthentication, BasicAuthentication
from django.db import DatabaseError
from django.http import JsonResponse
from django.utils import timezone
from datetime import datetime, timedelta
from uuid import UUID

from core.models import User, TrafficJam
from .serializers import UserSerializer, TrafficJamSerializer

# LOGIN 
from django.contrib.auth import authenticate, login
from rest_framework.views import APIView
from rest_framework import status
# LOGOUT
from django.contrib.auth import logout
from rest_framework.response import Response

# Create your views here.

###### ACCOUNT ######
#LOGIN
@api_view(['POST'])
@permission_classes([AllowAny])
@authentication_classes([SessionAuthentication, BasicAuthentication])
def login(request):
    username = request.data.get('username')
    password = request.data.get('password')

    # Authenticate the user
    user = authenticate(username=username, password=password)

    if user is not None:
        # Create or retrieve the token for the user
        token, _ = Token.objects.get_or_create(user=user)

        response_data = {
            'message': 'Login success',
            'token': token.key
        }
        response = Response(response_data, status=status.HTTP_200_OK)
        response.set_cookie('token', token.key)  # Add session cookie

        return response
    else:
        raise AuthenticationFailed('Invalid credentials')
    
#LOGOUT
@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def logout(request):
    if not request.user.is_authenticated:
        raise PermissionDenied()
    if request.user.is_authenticated:
        Token.objects.filter(user=request.user).delete()
    response = Response({'message': 'Logout success'}, status=status.HTTP_200_OK)
    response.delete_cookie('token')  # remove session cookie
    logout(request)  # Logout the user
    return response

#REGISTER
@api_view(['POST'])
def register_account(request):
    try:
        # Extract the necessary data from the request
        username = request.data.get('username')
        password = request.data.get('password')
        email = request.data.get('email')

        if not password:
            return Response({"error": "Password cannot be empty"}, status=400)

        # Create a new user instance
        user = User(
            username=username,
            email=email,
            is_active=True,
            is_staff=False,
            is_superuser=False
        )
        
        user.set_password(password)  # Set the password using the set_password method

        # Save the user instance
        user.save()

        return Response(status=status.HTTP_200_OK)
    except DatabaseError as e:
        return Response({"error": "Bad data"}, status=500)
    

###### TRAFFIC JAM ######    
@api_view(['POST'])
def create_traffic_jam(request):
    try:
        date = request.data.get('date')
        time = request.data.get('time')
        message = request.data.get('message')

        if not date or not time or not message:
            return Response({"error": "Missing required fields"}, status=status.HTTP_400_BAD_REQUEST)

        traffic_jam = TrafficJam()
        traffic_jam.create_traffic_jam(date=date, time=time, message=message)
        traffic_jam.save()

        return Response({"message": "Traffic jam created successfully"}, status=status.HTTP_201_CREATED)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


<<<<<<< HEAD
@api_view(['POST'])
def update_traffic_jam(request):
    trafficjam = TrafficJam()
    id = request.data.get('id')
    date = request.data.get('date')
    time = request.data.get('time')
    message = request.data.get('message')

    mytrafficjam = trafficjam.get_traffic_jam(id)
    if date == '' : date = None
    if time == '' : time = None
    if message == '' : message = None
    mytrafficjam.update_traffic_jam(date, time, message)
    return Response(status=status.HTTP_200_OK)

@api_view(['POST'])
def delete_traffic_jam(request):
    trafficjam = TrafficJam()
    id = request.data.get('id')
    mytrafficjam = trafficjam.get_traffic_jam(id)
    mytrafficjam.delete_traffic_jam()
    return Response(status=status.HTTP_200_OK)

@api_view(['POST'])
def search_traffic_jam(request):
    keyword = request.data.get('keyword', '')
    if not keyword:
        return JsonResponse({'error' : 'Please provide a keyword to search for'})

    result = TrafficJam.search_traffic_jam(keyword)
    trafficjams = [tj for tj in result]
    data = [{'id':tj.id, 'date':tj.date, 'time':tj.time, 'message':tj.message} for tj in trafficjams]
    return Response(data)

@api_view(['GET'])
def view_traffic_jam(request):
    result = TrafficJam.traffic_jam_all()
    trafficjams = [tj for tj in result]
    data = [{'id':tj.id, 'date':tj.date, 'time':tj.time, 'message':tj.message} for tj in trafficjams]
    return Response(data)

@api_view(['POST'])
def update_traffic_jam(request):
    trafficjam = TrafficJam()
    id = request.data.get('id')
    date = request.data.get('date')
    time = request.data.get('time')
    message = request.data.get('message')

    mytrafficjam = trafficjam.get_traffic_jam(id)
    if date == '' : date = None
    if time == '' : time = None
    if message == '' : message = None
    mytrafficjam.update_traffic_jam(date, time, message)
    return Response(status=status.HTTP_200_OK)

@api_view(['POST'])
def delete_traffic_jam(request):
    trafficjam = TrafficJam()
    id = request.data.get('id')
    mytrafficjam = trafficjam.get_traffic_jam(id)
    mytrafficjam.delete_traffic_jam()
    return Response(status=status.HTTP_200_OK)

@api_view(['POST'])
def search_traffic_jam(request):
    keyword = request.data.get('keyword', '')
    if not keyword:
        return JsonResponse({'error' : 'Please provide a keyword to search for'})

    result = TrafficJam.search_traffic_jam(keyword)
    trafficjams = [tj for tj in result]
    data = [{'id':tj.id, 'date':tj.date, 'time':tj.time, 'message':tj.message} for tj in trafficjams]
    return Response(data)

=======
    
>>>>>>> parent of e2a7b2e (Sprint 4: add read, update, delete and search functions in views.py)
'''
class ViewTrafficJam(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    @api_view(['GET'])   
    def getTrafficJam(request):
        
        #idk if this is required
        # Some authentication operations perhaps?
        #
        

        traffic_jams = TrafficJam.get_live_traffic_jam()

        data = []
        for traffic_jam in traffic_jams:
            data.append({
                'id': traffic_jam.id,
                'date': traffic_jam.date,
                'time': traffic_jam.time,
                'location': traffic_jam.location,
                'message': traffic_jam.message
            })

        return Response(data)
    
class ViewTrafficClosure(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    @api_view(['GET'])   
    def get_traffic_closure(request):
        
        #idk if this is required
        # Some authentication operations perhaps?
        

        traffic_closures = TrafficClosure.get_live_traffic_closure()

        data = []
        for traffic_closure in traffic_closures:
            data.append({
                'id': traffic_closure.id,
                'date': traffic_closure.date,
                'time': traffic_closure.time,
                #'location': traffic_closure.location,
                'message': traffic_closure.message
            })

        return Response(data)
    
class ViewTrafficAccident(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    @api_view(['GET'])   
    def get_traffic_accident(request):
        
        #idk if this is required
        # Some authentication operations perhaps?
        

        traffic_accidents = TrafficAccident.get_live_traffic_accident()

        data = []
        for traffic_accident in traffic_accidents:
            data.append({
                'id': traffic_accident.id,
                'date': traffic_accident.date,
                'time': traffic_accident.time,
                #'location': traffic_accident.location,
                'message': traffic_accident.message
            })

        return Response(data)

'''
    