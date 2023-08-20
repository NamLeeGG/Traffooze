from core.models import RoadAccident
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

class DeleteRoadAccidentTestCase(APITestCase):
    def test_delete_road_accident(self):
        # Create a road accident object
        road_accident = RoadAccident.objects.create(date='2023-06-18', time='08:15', message='Sample message', location='1.87927590237258,103.2984724618')

        # Send a POST request to the delete_road_accident endpoint
        url = reverse('delete-road-accident')
        data = {'id': str(road_accident.id)}  # Convert the UUID to a string
        response = self.client.post(url, data)

        # Assert the response
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['message'], "Road accident deleted successfully")

        # Verify that the road accident object is deleted
        with self.assertRaises(RoadAccident.DoesNotExist):
            RoadAccident.objects.get(id=road_accident.id)

        print("test delete road accident passed")

    def test_delete_road_accident_not_found(self):
        # Road accident ID that doesn't exist in the database
        invalid_road_accident_id = "adbf87df-f5c7-483f-99f1-d1aca81f135d"

        data = {'id': invalid_road_accident_id}

        url = reverse('delete-road-accident')
        response = self.client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.data['error'], "Road accident not found")

        print("test delete road accident not found passed")

    def test_delete_road_accident_invalid_format(self):
        # Create a road accident
        road_accident = RoadAccident.objects.create(date='2023-06-18', time='08:15', message='Sample message', location='1.87927590237258,103.2984724618')

        # Set an invalid ID to simulate an error during deletion
        invalid_road_accident_id = 'invalid_id'

        payload = {
            'id': invalid_road_accident_id
        }

        url = reverse('delete-road-accident')
        response = self.client.post(url, payload)

        self.assertEqual(response.status_code, status.HTTP_500_INTERNAL_SERVER_ERROR)
        self.assertEqual(response.data['error'], "['“invalid_id” is not a valid UUID.']")

        # Ensure the road accident still exists
        road_accident_exists = RoadAccident.objects.filter(id=road_accident.id).exists()
        self.assertTrue(road_accident_exists)

        print("test delete road accident invalid format passed")
