'''import json
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from simetrikApi import models
from simetrikApi.models import TablesManager
class TablesManagerTest(APITestCase):
  #Create table returns 200 (success), 200 (table already exist), 401 (invalid url) or 500 (internal server error)
  def test_create_table_200(self):
    url = reverse('tables-create')
    data = {'url': 'https://raw.githubusercontent.com/nadiarosenberg/csvForTesting/main/fig4.csv'}
    response = self.client.post(url, data)
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertEqual(response.data, 'Table created')

  def test_create_table_401(self):
    url = reverse('tables-create')
    data = {'url': 'https://raw.githubusercontent.com/nadiarosenberg/csvForTesting/main/fig4.abc'}
    response = self.client.post(url, data)
    self.assertEqual(response.status_code, status.HTTP_401_BAD_REQUEST)
    self.assertEqual(response.data, 'Invalid url')
  
  #Get tables returns 200 (success) or 500 (internal server error)
  def test_get_tables_200(self):
    url = reverse('tables')
    response = self.client.get(url)
    self.assertEqual(response.status_code, status.HTTP_200_OK)
  
  #Get table returns 200 (success), 500 (internal server error) and 404 (Table doesnt exist)
  def test_get_one_table_200(self):
    url = reverse('tables-name')
    response = self.client.get(url, arg=['fig4'])
    self.assertEqual(response.status_code, status.HTTP_200_OK)
  
  def test_get_one_table_404(self):
    url = reverse('tables-name')
    response = self.client.get(url, arg=['fig40'])
    self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)'''
