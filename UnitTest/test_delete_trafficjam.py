from core.models import TrafficJam
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

class DeleteTrafficJamTestCase(APITestCase):
    def test_delete_traffic_jam(self):
        # Create a traffic jam object
        traffic_jam = TrafficJam.objects.create(date='2023-06-18', time='22:47', message='Sample message')

        # Send a POST request to the delete_traffic_jam endpoint
        url = reverse('delete-traffic-jam')
        data = {'id': str(traffic_jam.id)}  # Convert the UUID to a string
        response = self.client.post(url, data)

        # Assert the response
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['message'], "Traffic jam deleted successfully")

        # Verify that the traffic jam object is deleted
        with self.assertRaises(TrafficJam.DoesNotExist):
            TrafficJam.objects.get(id=traffic_jam.id)

        print("test delete traffic jam passed")

    def test_delete_traffic_jam_not_found(self):
        # Traffic jam ID that doesn't exist in the database
        invalid_traffic_jam_id = "adbf87df-f5c7-483f-99f1-d1aca81f135d"

        data = {'id': invalid_traffic_jam_id}

        url = reverse('delete-traffic-jam')
        response = self.client.post(url, data)

        #print(response.data)

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.data['error'], "Traffic jam not found")

        print("test delete traffic jam not found passed")

    def test_delete_traffic_jam_invalid_format(self):
        # Create a traffic jam
        traffic_jam = TrafficJam.objects.create(date='2023-06-18', time='22:47', message='Sample message')

        # Set an invalid ID to simulate an error during deletion
        invalid_traffic_jam_id = 'invalid_id'

        payload = {
            'id': invalid_traffic_jam_id
        }

        url = reverse('delete-traffic-jam')
        response = self.client.post(url, payload)

        self.assertEqual(response.status_code, status.HTTP_500_INTERNAL_SERVER_ERROR)
        self.assertEqual(response.data['error'], "['“invalid_id” is not a valid UUID.']")

        #print(response.data)

        # Ensure the traffic jam still exists
        traffic_jam_exists = TrafficJam.objects.filter(id=traffic_jam.id).exists()
        self.assertTrue(traffic_jam_exists)

        print("test delete traffic jam invalid format passed")