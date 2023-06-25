from datetime import datetime
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from core.models import TrafficJam

class SearchTrafficJamTestCase(APITestCase):
    
    def test_search_traffic_jam(self):
        # Create traffic jam objects with different messages
        traffic_jam1 = TrafficJam.objects.create(date='2023-06-18', time='22:47', message='Sample message 1', location='1.30398068448214,103.919182834377')
        traffic_jam2 = TrafficJam.objects.create(date='2023-06-19', time='10:15', message='Another message', location='1.30398068448214,103.919182834378')
        traffic_jam3 = TrafficJam.objects.create(date='2023-06-20', time='16:30', message='Sample message 2', location='1.30398068448214,103.919182834100')

        # Send a POST request to the search_traffic_jam endpoint
        url = reverse('search-traffic-jam')
        data = {'keyword': 'Sample'}
        response = self.client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Verify the search results
        expected_data = [
            {
                'id': traffic_jam1.id,
                'date': datetime.strptime(traffic_jam1.date, '%Y-%m-%d').date(),
                'time': datetime.strptime(traffic_jam1.time, '%H:%M').time(),
                'message': 'Sample message 1',
                'location': '1.30398068448214,103.919182834377'
            },
            {
                'id': traffic_jam3.id,
                'date': datetime.strptime(traffic_jam3.date, '%Y-%m-%d').date(),
                'time': datetime.strptime(traffic_jam3.time, '%H:%M').time(),
                'message': 'Sample message 2',
                'location': '1.30398068448214,103.919182834100'
            }
        ]
        self.assertEqual(response.data, expected_data)

        print("test search traffic jam passed")
    
    '''
    def test_search_traffic_jam_with_keyword(self):
        url = reverse('search-traffic-jam')
        keyword = 'Sample'

        # Create some test TrafficJam instances with matching keyword
        traffic_jam1 = TrafficJam.objects.create(date='18/06/2023', time='22:47', message='Sample message')
        traffic_jam2 = TrafficJam.objects.create(date='19/06/2023', time='12:30', message='Another sample')

        response = self.client.post(url, {'keyword': keyword})

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)  # Assert that 1 traffic jam is returned

        # Assert the response data for the traffic jam
        self.assertEqual(response.data[0]['id'], traffic_jam1.id)
        self.assertEqual(response.data[0]['date'], traffic_jam1.date)
        self.assertEqual(response.data[0]['time'], traffic_jam1.time)
        self.assertEqual(response.data[0]['message'], traffic_jam1.message)
        print('\nUnit test search-traffic-jam passed')
    '''