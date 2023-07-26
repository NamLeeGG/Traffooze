from core.models import TrafficJam
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

class UpdateTrafficJamTestCase(APITestCase):
    def test_update_traffic_jam(self):
        traffic_jam = TrafficJam.objects.create(date='2023-06-18', time='22:47', message='Sample message')

        payload = {
            'id': traffic_jam.id,
            'date': '2023-06-19',
            'time': '08:30',
            'message': 'Updated message'
        }

        url = reverse('update-traffic-jam')
        response = self.client.post(url, payload)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['message'], "Traffic jam updated successfully")

        updated_traffic_jam = TrafficJam.objects.get(id=traffic_jam.id)
        self.assertEqual(str(updated_traffic_jam.date), "2023-06-19")
        self.assertEqual(str(updated_traffic_jam.time.strftime('%H:%M')), '08:30')
        self.assertEqual(updated_traffic_jam.message, 'Updated message')

        print("test update traffic jam passed")

    def test_update_traffic_jam_invalid_date_format(self):
        traffic_jam = TrafficJam.objects.create(date='2023-06-18', time='22:47', message='Sample message')

        payload = {
            'id': traffic_jam.id,
            'date': '2023/06/19',  # Invalid date format
            'time': '8:30 AM',  # Invalid time format
            'message': 'Updated message'
        }

        url = reverse('update-traffic-jam')
        response = self.client.post(url, payload)

        self.assertEqual(response.status_code, status.HTTP_500_INTERNAL_SERVER_ERROR)
        self.assertEqual(response.data['error'], "['“2023/06/19” value has an invalid date format. It must be in YYYY-MM-DD format.']")

        #print(response.data)

        # Ensure the traffic jam remains unchanged
        unchanged_traffic_jam = TrafficJam.objects.get(id=traffic_jam.id)
        self.assertEqual(str(unchanged_traffic_jam.date), "2023-06-18")
        self.assertEqual(str(unchanged_traffic_jam.time.strftime('%H:%M')), '22:47')
        self.assertEqual(unchanged_traffic_jam.message, 'Sample message')

        print("test update traffic jam invalid date format passed")

    def test_update_traffic_jam_not_found(self):
        # Traffic jam ID that doesn't exist in the database
        invalid_traffic_jam_id = "adbf87df-f5c7-483f-99f1-d1aca81f135d"

        payload = {
            'id': invalid_traffic_jam_id,
            'date': '2023-06-19',
            'time': '08:30',
            'message': 'Updated message'
        }

        url = reverse('update-traffic-jam')
        response = self.client.post(url, payload)

        #print(response.data)

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.data['error'], "Traffic jam not found")

        print("test update traffic jam not found passed")