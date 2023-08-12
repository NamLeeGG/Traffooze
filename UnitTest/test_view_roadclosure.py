from core.models import RoadClosure
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

class ViewRoadClosureTestCase(APITestCase):
    def test_view_road_closure(self):
        url = reverse('view-road-closure')
        
        RC1 = RoadClosure.objects.create(
            date= '2023-06-18', 
            time= '22:47', 
            message= 'Sample message 1', 
            location='1.30398068448214,103.919182834377'
        )
        RC2 = RoadClosure.objects.create(
            date= '2023-06-19', 
            time= '08:30', 
            message= 'Sample message 2', 
            location='1.30398068448214,103.919182834100'
        )

        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

        self.assertEqual(response.data[0]['id'], RC1.id)
        self.assertEqual(str(response.data[0]['date']), RC1.date)
        self.assertEqual(str(response.data[0]['time'].strftime('%H:%M')), RC1.time)
        self.assertEqual(response.data[0]['message'], RC1.message)
        self.assertEqual(response.data[0]['location'], RC1.location)

        self.assertEqual(response.data[1]['id'], RC2.id)
        self.assertEqual(str(response.data[1]['date']), RC2.date)
        self.assertEqual(str(response.data[1]['time'].strftime('%H:%M')), RC2.time)
        self.assertEqual(response.data[1]['message'], RC2.message)
        self.assertEqual(response.data[1]['location'], RC2.location)

        print('test view road closure passed')

    
