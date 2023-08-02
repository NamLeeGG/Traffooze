from core.models import TrafficJam
from api.serializers import TrafficJamSerializer
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

class CreateTrafficJamTestCase(APITestCase):
    def test_create_traffic_jam(self):
        # Prepare the traffic jam data
        traffic_jam_data = {
            'date': '2023-06-18',
            'time': '22:47',
            'message': 'Sample message',
            'location': '1.30398068448214,103.919182834377'
        }

        # Send a POST request to the create_traffic_jam endpoint
        url = reverse('create-traffic-jam')
        response = self.client.post(url, traffic_jam_data)

        #print(response.data)
        
        # Assert the response
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['message'], "Traffic jam created successfully")

        created_traffic_jam = TrafficJam.objects.get()
        self.assertEqual(str(created_traffic_jam.date), traffic_jam_data['date'])
        self.assertEqual(str(created_traffic_jam.time.strftime('%H:%M')), traffic_jam_data['time'])
        self.assertEqual(created_traffic_jam.message, traffic_jam_data['message'])
        self.assertEqual(created_traffic_jam.location, traffic_jam_data['location'])

        print("test create traffic jam passed")

    
    def test_create_traffic_jam_missing_fields(self):

        traffic_jam_data = {
            'date': '2023-06-18',
            'time': '22:47',
            'message': 'Sample message'
        }

        url = reverse('create-traffic-jam')

        response = self.client.post(url, traffic_jam_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data, {'error': 'Missing required fields'})
    
        print("test create traffic jam missing fields passed")
        
    def test_create_traffic_jam_invalid_date_format(self):

        traffic_jam_data = {
            'date': '2023/06/19', #invalid date format
            'time': '22:47',
            'message': 'Sample message',
            'location': '1.30398068448214,103.919182834377'
        }

        url = reverse('create-traffic-jam')

        response = self.client.post(url, traffic_jam_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_500_INTERNAL_SERVER_ERROR)
        self.assertEqual(response.data['error'], "['“2023/06/19” value has an invalid date format. It must be in YYYY-MM-DD format.']")

        print("test create traffic jam invalid date format passed")