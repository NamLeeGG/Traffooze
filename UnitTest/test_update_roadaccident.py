from core.models import RoadAccident
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

class UpdateRoadAccidentTestCase(APITestCase):
    def test_update_road_accident(self):
        road_accident = RoadAccident.objects.create(date='2023-06-18', time='08:15', message='Sample message', location='1.87927590237258,103.2984724618')

        payload = {
            'id': road_accident.id,
            'date': '2023-06-19',
            'time': '09:30',
            'message': 'Updated message',
            'location': '1.30398068448214,103.919182834100'
        }

        url = reverse('update-road-accident')
        response = self.client.post(url, payload)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['message'], "Road accident updated successfully")

        updated_road_accident = RoadAccident.objects.get(id=road_accident.id)
        self.assertEqual(str(updated_road_accident.date), "2023-06-19")
        self.assertEqual(str(updated_road_accident.time.strftime('%H:%M')), '09:30')
        self.assertEqual(updated_road_accident.message, 'Updated message')
        self.assertEqual(updated_road_accident.location, '1.30398068448214,103.919182834100')

        print("test update road accident passed")

    def test_update_road_accident_invalid_date_format(self):
        road_accident = RoadAccident.objects.create(date='2023-06-18', time='08:15', message='Sample message')

        payload = {
            'id': road_accident.id,
            'date': '2023/06/19',  # Invalid date format
            'time': '8:30 AM',  # Invalid time format
            'message': 'Updated message'
        }

        url = reverse('update-road-accident')
        response = self.client.post(url, payload)

        self.assertEqual(response.status_code, status.HTTP_500_INTERNAL_SERVER_ERROR)
        self.assertEqual(response.data['error'], "['“2023/06/19” value has an invalid date format. It must be in YYYY-MM-DD format.']")

        # Ensure the road accident remains unchanged
        unchanged_road_accident = RoadAccident.objects.get(id=road_accident.id)
        self.assertEqual(str(unchanged_road_accident.date), "2023-06-18")
        self.assertEqual(str(unchanged_road_accident.time.strftime('%H:%M')), '08:15')
        self.assertEqual(unchanged_road_accident.message, 'Sample message')

        print("test update road accident invalid date format passed")

    def test_update_road_accident_not_found(self):
        # Road accident ID that doesn't exist in the database
        invalid_road_accident_id = "adbf87df-f5c7-483f-99f1-d1aca81f135d"

        payload = {
            'id': invalid_road_accident_id,
            'date': '2023-06-19',
            'time': '09:30',
            'message': 'Updated message',
            'location':'1.87927590237258,103.2984724618'
        }

        url = reverse('update-road-accident')
        response = self.client.post(url, payload)

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.data['error'], "Road accident not found")

        print("test update road accident not found passed")
