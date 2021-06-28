from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from simetrikApi import models
from simetrikApi.models import TablesManager
import simetrikApi.pagination 
import mock

class TablesManagerTest(APITestCase):
  @mock.patch("simetrikApi.models.TablesManager.create_table")
  def test_create_table_400_case1(self, mock_method):
    url = reverse('tables-create')
    data = {'url': 'https://raw.githubusercontent.com/nadiarosenberg/csvForTesting/main/fig4.abc'}
    mock_method.return_value = 'Invalid url'
    response = self.client.post(url, data)
    self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    self.assertEqual(response.data, 'Invalid url')
  
  @mock.patch("simetrikApi.models.TablesManager.create_table")
  def test_create_table_400_case2(self, mock_method):
    url = reverse('tables-create')
    mock_method.return_value = '.csv file url is required'
    response = self.client.post(url)
    self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    self.assertEqual(response.data, '.csv file url is required')

  @mock.patch("simetrikApi.models.TablesManager.create_table")
  def test_create_table_200(self, mock_method):
    url = reverse('tables-create')
    data = {'url': 'https://raw.githubusercontent.com/nadiarosenberg/csvForTesting/main/fig4.csv'}
    mock_method.return_value = 'Table already exist'
    response = self.client.post(url, data)
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertEqual(response.data, 'Table already exist')
    
  @mock.patch('simetrikApi.models.TablesManager.create_table')
  def test_get_one_table_500(self, mock_method):
    url = reverse('tables-create')
    mock_method.return_value = 'Error creating table'
    response = self.client.get(url)
    self.assertEqual(response.status_code, status.HTTP_500_INTERNAL_SERVER_ERROR)

  @mock.patch("simetrikApi.models.TablesManager.get_all_tables")
  def test_get_tables_200(self, mock_method):
    url = reverse('tables')
    mock_method.return_value = [{'Tables_in_database': 'tablename'}]
    response = self.client.get(url)
    self.assertEqual(response.status_code, status.HTTP_200_OK)
  
  @mock.patch('simetrikApi.models.TablesManager.get_all_tables')
  def test_get_one_table_500(self, mock_method):
    url = reverse('tables')
    mock_method.return_value = 'error'
    response = self.client.get(url)
    self.assertEqual(response.status_code, status.HTTP_500_INTERNAL_SERVER_ERROR)
  
  @mock.patch("simetrikApi.models.TablesManager.get_count")
  @mock.patch("simetrikApi.models.TablesManager.get_one_table")
  @mock.patch("simetrikApi.pagination.get_pagination_result")
  def test_get_one_table_200(self, mock_method1, mock_method2, mock_method3):
    url = reverse('tables-name', args=['tablename'])
    mock_method1.return_value = 1
    mock_method2.return_value = [{'property': 'propname1'}]
    mock_method3.return_value = [{'current': 1, 'prev': None, 'next': None}]
    response = self.client.get(url)
    self.assertEqual(response.status_code, status.HTTP_200_OK)
  
  @mock.patch("simetrikApi.models.TablesManager.get_one_table")
  def test_get_one_table_404(self, mock_method):
    url = reverse('tables-name', args=['tablename'])
    mock_method.return_value = 'Table does not exist'
    response = self.client.get(url)
    self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

  @mock.patch('simetrikApi.models.TablesManager.get_one_table')
  def test_get_one_table_500(self, mock_method):
    url = reverse('tables-name', args=['tablename'])
    mock_method.return_value = 'error'
    response = self.client.get(url)
    self.assertEqual(response.status_code, status.HTTP_500_INTERNAL_SERVER_ERROR)

  @mock.patch("simetrikApi.models.TablesManager.create_table")
  def test_create_table_201(self, mock_method):
    url = reverse('tables-create')
    data = {'url': 'https://raw.githubusercontent.com/nadiarosenberg/csvForTesting/main/fig4.csv'}
    mock_method.return_value = 'Table created'
    response = self.client.post(url, data)
    self.assertEqual(response.status_code, status.HTTP_201_CREATED)