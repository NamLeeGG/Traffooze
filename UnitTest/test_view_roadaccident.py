from core.models import RoadAccident
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

class ViewRoadAccidentTestCase(APITestCase):
    def test_retrieve_ra_authorized(self):
        url = reverse('view-road-accident')

        # Create some test RoadAccident instances with matching keyword
        RA1 = RoadAccident.objects.create(date='2023-06-18', time='08:15', message='Sample message 1', location='1.30398068448214,103.919182834377')
        RA2 = RoadAccident.objects.create(date='2023-06-19', time='09:30', message='Sample message 2', location='1.30398068448214,103.919182834100')

        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

        self.assertEqual(response.data[0]['id'], RA1.id)
        self.assertEqual(str(response.data[0]['date']), RA1.date)
        self.assertEqual(str(response.data[0]['time'].strftime('%H:%M')), RA1.time)
        self.assertEqual(response.data[0]['message'], RA1.message)
        self.assertEqual(response.data[0]['location'], RA1.location)

        self.assertEqual(response.data[1]['id'], RA2.id)
        self.assertEqual(str(response.data[1]['date']), RA2.date)
        self.assertEqual(str(response.data[1]['time'].strftime('%H:%M')), RA2.time)
        self.assertEqual(response.data[1]['message'], RA2.message)
        self.assertEqual(response.data[1]['location'], RA2.location)

        print('test view road accident passed')
