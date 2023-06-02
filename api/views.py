from django.shortcuts import render

# Create your views here.
"""
class LoginView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]

    #LOGIN(username, pw) 
    @api_view(['POST'])
    def login(request):
        username = request.data.get('username')
        password = request.data.get('password')
        myuser = User()
        token = myuser.userauthenticate(request, username, password)
        if token is not None:
            response_data = {
                    'message': 'Login success',
                    'token': token.key
            }
            response = Response(response_data, status=status.HTTP_200_OK)
            response.set_cookie('token', token.key)  # add session cookie
            return response
        else:
            return Response({'message': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
"""
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