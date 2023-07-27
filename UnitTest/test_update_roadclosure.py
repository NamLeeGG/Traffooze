from core.models import RoadClosure
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

class UpdateRoadClosureTestCase(APITestCase):
    def test_update_road_closure(self):
        road_closure = RoadClosure.objects.create(date='2023-06-18', time='22:47', message='Sample message')

        payload = {
            'id': road_closure.id,
            'date': '2023-06-19',
            'time': '08:30',
            'message': 'Updated message'
        }

        url = reverse('update-road-closure')
        response = self.client.post(url, payload)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['message'], "Road closure updated successfully")

        updated_road_closure = RoadClosure.objects.get(id=road_closure.id)
        self.assertEqual(str(updated_road_closure.date), "2023-06-19")
        self.assertEqual(str(updated_road_closure.time.strftime('%H:%M')), '08:30')
        self.assertEqual(updated_road_closure.message, 'Updated message')

        print("test update road closure passed")

    def test_update_road_closure_invalid_date_format(self):
        road_closure = RoadClosure.objects.create(date='2023-06-18', time='22:47', message='Sample message')

        payload = {
            'id': road_closure.id,
            'date': '2023/06/19',  # Invalid date format
            'time': '8:30 AM',  # Invalid time format
            'message': 'Updated message'
        }

        url = reverse('update-road-closure')
        response = self.client.post(url, payload)

        self.assertEqual(response.status_code, status.HTTP_500_INTERNAL_SERVER_ERROR)
        self.assertEqual(response.data['error'], "['“2023/06/19” value has an invalid date format. It must be in YYYY-MM-DD format.']")

        #print(response.data)

        # Ensure the traffic jam remains unchanged
        unchanged_road_closure = RoadClosure.objects.get(id=road_closure.id)
        self.assertEqual(str(unchanged_road_closure.date), "2023-06-18")
        self.assertEqual(str(unchanged_road_closure.time.strftime('%H:%M')), '22:47')
        self.assertEqual(unchanged_road_closure.message, 'Sample message')

        print("test update road closure invalid date format passed")

    def test_update_road_closure_not_found(self):
        # Traffic jam ID that doesn't exist in the database
        invalid_road_closure_id = "adbf87df-f5c7-483f-99f1-d1aca81f135d"

        payload = {
            'id': invalid_road_closure_id,
            'date': '2023-06-19',
            'time': '08:30',
            'message': 'Updated message'
        }

        url = reverse('update-road-closure')
        response = self.client.post(url, payload)

        #print(response.data)

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.data['error'], "Road closure not found")

        print("test update road closure not found passed")