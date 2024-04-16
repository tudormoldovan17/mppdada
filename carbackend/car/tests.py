from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Car


class CarTests(APITestCase):
    def setUp(self):
        self.car1 = Car.objects.create(name='TestCar1', horsepower=100, color='Red', year=2020, country='USA')
        self.car2 = Car.objects.create(name='TestCar2', horsepower=150, color='Blue', year=2021, country='Germany')

    def test_get_all_cars(self):
        url = reverse('car-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 2)
        self.assertEqual(response.data['results'][0]['name'], 'TestCar1');
        self.assertEqual(response.data['results'][1]['name'], 'TestCar2');

    def test_get_single_car(self):
        url = reverse('car-detail', args=[self.car1.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'TestCar1')

    def test_get_horsepowers(self):
        url = reverse('horsepowers')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_get_cars_by_horsepower(self):
        url = reverse('get_cars_by_horsepower', args=[100])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_create_car(self):
        url = reverse('car-list')
        data = {'name': 'NewCar', 'horsepower': 200, 'color': 'Black', 'year': 2022, 'country': 'Japan'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Car.objects.count(), 3)

    def test_update_car(self):
        url = reverse('car-detail', args=[self.car1.id])
        data = {'name': 'UpdatedCar', 'horsepower': 120, 'color': 'Green', 'year': 2021, 'country': 'UK'}
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Car.objects.get(id=self.car1.id).name, 'UpdatedCar')

    def test_delete_car(self):
        url = reverse('car-detail', args=[self.car1.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Car.objects.count(), 1)


class GetCarsByHorsepowerTests(APITestCase):
    def setUp(self):
        Car.objects.create(name='Car1', horsepower=100, color='Red', year=2021, country='USA')
        Car.objects.create(name='Car2', horsepower=200, color='Blue', year=2022, country='Germany')

    def test_get_cars_by_horsepower(self):
        url = reverse('get_cars_by_horsepower', kwargs={'horsepower': 100})
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['horsepower'], 100)

    def test_get_horsepowers(self):
        url = reverse('horsepowers')
        response = self.client.get(url)
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[0], 100)