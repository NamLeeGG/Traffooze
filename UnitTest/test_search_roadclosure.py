from datetime import datetime
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from core.models import RoadClosure

class SearchRoadClosureTestCase(APITestCase):
    
    def test_search_road_closure(self):
        # Create road closure objects with different messages
        road_closure1 = RoadClosure.objects.create(date='2023-06-18', time='22:47', message='Sample message 1', location='1.30398068448214,103.919182834377')
        road_closure2 = RoadClosure.objects.create(date='2023-06-19', time='10:15', message='Another message', location='1.30398068448214,103.919182834378')
        road_closure3 = RoadClosure.objects.create(date='2023-06-20', time='16:30', message='Sample message 2', location='1.30398068448214,103.919182834100')

        # Send a POST request to the search_road_closure endpoint
        url = reverse('search-road-closure')
        data = {'keyword': 'Sample'}
        response = self.client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Verify the search results
        expected_data = [
            {
                'id': road_closure1.id,
                'date': datetime.strptime(road_closure1.date, '%Y-%m-%d').date(),
                'time': datetime.strptime(road_closure1.time, '%H:%M').time(),
                'message': 'Sample message 1',
                'location': '1.30398068448214,103.919182834377'
            },
            {
                'id': road_closure3.id,
                'date': datetime.strptime(road_closure3.date, '%Y-%m-%d').date(),
                'time': datetime.strptime(road_closure3.time, '%H:%M').time(),
                'message': 'Sample message 2',
                'location': '1.30398068448214,103.919182834100'
            }
        ]
        self.assertEqual(response.data, expected_data)

        print("test search road closure passed")
    
    '''
    def test_search_traffic_jam_with_keyword(self):
        url = reverse('search-traffic-jam')
        keyword = 'Sample'

        # Create some test RoadClosure instances with matching keyword
        traffic_jam1 = RoadClosure.objects.create(date='18/06/2023', time='22:47', message='Sample message')
        traffic_jam2 = RoadClosure.objects.create(date='19/06/2023', time='12:30', message='Another sample')

        response = self.client.post(url, {'keyword': keyword})

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)  # Assert that 1 road closure is returned

        # Assert the response data for the road closure
        self.assertEqual(response.data[0]['id'], traffic_jam1.id)
        self.assertEqual(response.data[0]['date'], traffic_jam1.date)
        self.assertEqual(response.data[0]['time'], traffic_jam1.time)
        self.assertEqual(response.data[0]['message'], traffic_jam1.message)
        print('\nUnit test search-traffic-jam passed')
    '''