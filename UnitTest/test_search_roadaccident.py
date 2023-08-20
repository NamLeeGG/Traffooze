from datetime import datetime
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from core.models import RoadAccident

class SearchRoadAccidentTestCase(APITestCase):
    
    def test_search_road_accident(self):
        # Road accident objects
        road_accident1 = RoadAccident.objects.create(date='2023-06-18', time='08:15', message='Sample Traffooze message 1', location='1.30398068448214,103.919182834377')
        road_accident2 = RoadAccident.objects.create(date='2023-06-19', time='09:30', message='Another message', location='1.30398068448214,103.919182834378')
        road_accident3 = RoadAccident.objects.create(date='2023-06-20', time='15:45', message='Sample Traffooze message 2', location='1.30398068448214,103.919182834100')

        # Send a POST request to the search_road_accident endpoint
        url = reverse('search-road-accident')
        data = {'keyword': 'Sample'}
        response = self.client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Verify the search results
        expected_data = [
            {
                'id': road_accident1.id,
                'date': datetime.strptime(road_accident1.date, '%Y-%m-%d').date(),
                'time': datetime.strptime(road_accident1.time, '%H:%M').time(),
                'message': 'Sample Traffooze message 1',
                'location': '1.30398068448214,103.919182834377'
            },
            {
                'id': road_accident3.id,
                'date': datetime.strptime(road_accident3.date, '%Y-%m-%d').date(),
                'time': datetime.strptime(road_accident3.time, '%H:%M').time(),
                'message': 'Sample Traffooze message 2',
                'location': '1.30398068448214,103.919182834100'
            }
        ]
        self.assertEqual(response.data, expected_data)

        print("test search road accident passed")
