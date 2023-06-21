from core.models import TrafficJam
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
#from operator import attrgetter


class ViewTrafficJamTestCase(APITestCase):
    def test_retrieve_cr_authorized(self):
        url = reverse('view-traffic-jam')

        # Create some test CinemaRoom instances with matching keyword
        TJ1 = TrafficJam.objects.create(date= '18/06/2023', time= '22:47', message= 'Sample message 1')
        TJ2 = TrafficJam.objects.create(date= '19/06/2023', time= '08:30', message= 'Sample message 2')

        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

        self.assertEqual(response.data[0]['id'], TJ1.id)
        self.assertEqual(response.data[0]['date'], TJ1.date)
        self.assertEqual(response.data[0]['time'], TJ1.time)
        self.assertEqual(response.data[0]['message'], TJ1.message)

        self.assertEqual(response.data[1]['id'], TJ2.id)
        self.assertEqual(response.data[1]['date'], TJ2.date)
        self.assertEqual(response.data[1]['time'], TJ2.time)
        self.assertEqual(response.data[1]['message'], TJ2.message)
        print('test view traffic jam passed')
'''
    def test_view_traffic_jam(self):

        traffic_jam_data = [
            {'date': '18/06/2023', 'time': '22:47', 'message': 'Sample message 1'},
            {'date': '19/06/2023', 'time': '08:30', 'message': 'Sample message 2'}
        ]
        for data in traffic_jam_data:
            TrafficJam.objects.create(**data)

        # Send a GET request to the view_traffic_jam endpoint
        url = reverse('view-traffic-jam') 
        response = self.client.get(url)

        # Assert the response
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, list)
        self.assertEqual(len(response.data), len(traffic_jam_data))

        # Verify the response data
        traffic_jams = TrafficJam.objects.order_by('id')
        sorted_traffic_jams = sorted(traffic_jams, key=attrgetter('id'))  # Sort traffic jams by id
        for i, tj_data in enumerate(response.data):
            traffic_jam = sorted_traffic_jams[i]
            self.assertEqual(tj_data['id'], str(traffic_jam.id))  # Convert UUID to string for comparison
            self.assertEqual(tj_data['date'], traffic_jam.date)
            self.assertEqual(tj_data['time'], traffic_jam.time)
            self.assertEqual(tj_data['message'], traffic_jam.message)

'''
    
