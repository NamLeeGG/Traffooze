from core.models import TrafficJam
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

class DeleteTrafficJamTestCase(APITestCase):
    def test_delete_traffic_jam(self):
        # Create a traffic jam object
        traffic_jam = TrafficJam.objects.create(date='18/06/2023', time='22:47', message='Sample message')

        # Send a POST request to the delete_traffic_jam endpoint
        url = reverse('delete-traffic-jam')
        data = {'id': str(traffic_jam.id)}  # Convert the UUID to a string
        response = self.client.post(url, data)

        # Assert the response
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Verify that the traffic jam object is deleted
        with self.assertRaises(TrafficJam.DoesNotExist):
            TrafficJam.objects.get(id=traffic_jam.id)

        print("test delete traffic jam passed")
