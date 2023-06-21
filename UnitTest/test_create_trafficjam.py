from core.models import TrafficJam
from api.serializers import TrafficJamSerializer
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

class CreateTrafficJamTestCase(APITestCase):
    def test_create_traffic_jam(self):
        # Prepare the traffic jam data
        traffic_jam_data = {
            'date': '18/06/2023',
            'time': '22:47',
            'message': 'Sample message',
        }

        # Send a POST request to the create_traffic_jam endpoint
        url = reverse('create-traffic-jam')
        response = self.client.post(url, traffic_jam_data)

        # Assert the response
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn('date', response.data)
        self.assertIn('time', response.data)
        self.assertIn('message', response.data)

        created_traffic_jam = TrafficJam.objects.get(id=response.data['id'])
        self.assertEqual(created_traffic_jam.date, traffic_jam_data['date'])
        self.assertEqual(created_traffic_jam.time, traffic_jam_data['time'])

        serializer = TrafficJamSerializer(created_traffic_jam)
        self.assertEqual(response.data, serializer.data)
