from core.models import RoadAccident
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

class CreateRoadAccidentTestCase(APITestCase):
    def test_create_road_accident(self):
        # Prepare the road accident data
        road_accident_data = {
            'date': '2023-06-18',
            'time': '08:15',
            'message': 'Sample message',
            'location': '1.30398068448214,103.919182834377'
        }

        # Send a POST request to the create_road_accident endpoint
        url = reverse('create-road-accident')
        response = self.client.post(url, road_accident_data)

        # Assert the response
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['message'], "Road accident created successfully")

        created_road_accident = RoadAccident.objects.get()
        self.assertEqual(str(created_road_accident.date), road_accident_data['date'])
        self.assertEqual(str(created_road_accident.time.strftime('%H:%M')), road_accident_data['time'])
        self.assertEqual(created_road_accident.message, road_accident_data['message'])
        self.assertEqual(created_road_accident.location, road_accident_data['location'])

        print("test create road accident passed")

    def test_create_road_accident_missing_fields(self):
        road_accident_data = {
            'date': '2023-06-18',
            'time': '08:15',
            'description': 'Sample description'
        }

        url = reverse('create-road-accident')

        response = self.client.post(url, road_accident_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data, {'error': 'Missing required fields'})

        print("test create road accident missing fields passed")

    def test_create_road_accident_invalid_date_format(self):
        road_accident_data = {
            'date': '2023/06/19',  # invalid date format
            'time': '08:15',
            'message': 'Sample message',
            'location': '1.30398068448214,103.919182834377'
        }

        url = reverse('create-road-accident')

        response = self.client.post(url, road_accident_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_500_INTERNAL_SERVER_ERROR)
        self.assertEqual(response.data['error'], "['“2023/06/19” value has an invalid date format. It must be in YYYY-MM-DD format.']")

        print("test create road accident invalid date format passed")
