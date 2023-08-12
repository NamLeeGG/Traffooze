from core.models import RoadClosure
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

class DeleteRoadClosureTestCase(APITestCase):
    def test_delete_traffic_jam(self):
        # Create a road closure object
        road_closure = RoadClosure.objects.create(date='2023-06-18', time='22:47', message='Sample message')

        # Send a POST request to the delete_traffic_jam endpoint
        url = reverse('delete-road-closure')
        data = {'id': str(road_closure.id)}  # Convert the UUID to a string
        response = self.client.post(url, data)

        # Assert the response
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['message'], "Road closure deleted successfully")

        # Verify that the road closure object is deleted
        with self.assertRaises(RoadClosure.DoesNotExist):
            RoadClosure.objects.get(id=road_closure.id)

        print("test delete road closure passed")

    def test_delete_traffic_jam_not_found(self):
        # Road closure ID that doesn't exist in the database
        invalid_road_closure_id = "adbf87df-f5c7-483f-99f1-d1aca81f135d"

        data = {'id': invalid_road_closure_id}

        url = reverse('delete-road-closure')
        response = self.client.post(url, data)

        #print(response.data)

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.data['error'], "Road closure not found")

        print("test delete road closure not found passed")

    def test_delete_road_closure_invalid_format(self):
        # Create a road closure
        road_closure = RoadClosure.objects.create(date='2023-06-18', time='22:47', message='Sample message')

        # Set an invalid ID to simulate an error during deletion
        invalid_road_closure_id = 'invalid_id'

        payload = {
            'id': invalid_road_closure_id
        }

        url = reverse('delete-road-closure')
        response = self.client.post(url, payload)

        self.assertEqual(response.status_code, status.HTTP_500_INTERNAL_SERVER_ERROR)
        self.assertEqual(response.data['error'], "['“invalid_id” is not a valid UUID.']")

        #print(response.data)

        # Ensure the road closure still exists
        road_closure_exists = RoadClosure.objects.filter(id=road_closure.id).exists()
        self.assertTrue(road_closure_exists)

        print("test delete road closure invalid format passed")