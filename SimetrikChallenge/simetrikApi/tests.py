'''import json
from rest_framework.test import APITestCase
from rest_framework import status
from rest_framework import reverse
from simetrikApi import models
from simetrikApi.models import TablesManager
class TablesManagerTest(APITestCase):
  #Create table devuelve 500, 401 si la url es invalida, 200 si la tabla ya existe o 201 created
  def test_create_table(self):
    data = {'url': 'https://github.com/nadiarosenberg/csvForTesting/blob/main/fig4.csv'}
    response = self.client.post('tables/create/', data)
    self.assertEqual(response.status_code, status.HTTP_201_CREATED)
  
  #Get tables devuelve 500 y 200
  def test_get_table(self):
    response = self.client.get(reverse('tables/<str:name>'), kwars = {'name': 'fig4'})
    self.assertEqual(response.status_code, status.HTTP_200_OK)
  
  #Get table devuelve 500, 200 y 404 
  def test_get_one_table(self):
    response = self.client.get(reverse('tables/<str:name>'), kwars = {'name': 'fig4'})
    self.assertEqual(response.status_code, status.HTTP_200_OK)'''
