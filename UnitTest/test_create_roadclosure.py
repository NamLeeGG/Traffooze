from core.models import RoadClosure
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

class CreateRoadClosureTestCase(APITestCase):
    def test_create_road_closure(self):
        # Prepare the road closure data
        road_closure_data = {
            'date': '2023-06-18',
            'time': '22:47',
            'message': 'Sample message',
            'location': '1.30398068448214,103.919182834377'
        }

        # Send a POST request to the create_traffic_jam endpoint
        url = reverse('create-road-closure')
        response = self.client.post(url, road_closure_data)

        #print(response.data)
        
        # Assert the response
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['message'], "Road closure created successfully")

        created_road_closure = RoadClosure.objects.get()
        self.assertEqual(str(created_road_closure.date), road_closure_data['date'])
        self.assertEqual(str(created_road_closure.time.strftime('%H:%M')), road_closure_data['time'])
        self.assertEqual(created_road_closure.message, road_closure_data['message'])
        self.assertEqual(created_road_closure.location, road_closure_data['location'])

        print("test create road closure passed")

    
    def test_create_road_closure_missing_fields(self):

        road_closure_data = {
            'date': '2023-06-18',
            'time': '22:47',
            'message': 'Sample message'
        }

        url = reverse('create-road-closure')

        response = self.client.post(url, road_closure_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data, {'error': 'Missing required fields'})
    
        print("test create road closure missing fields passed")
        
    def test_create_road_closure_invalid_date_format(self):

        road_closure_data = {
            'date': '2023/06/19', #invalid date format
            'time': '22:47',
            'message': 'Sample message',
            'location': '1.30398068448214,103.919182834377'
        }

        url = reverse('create-road-closure')

        response = self.client.post(url, road_closure_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_500_INTERNAL_SERVER_ERROR)
        self.assertEqual(response.data['error'], "['“2023/06/19” value has an invalid date format. It must be in YYYY-MM-DD format.']")

        print("test create road closure invalid date format passed")