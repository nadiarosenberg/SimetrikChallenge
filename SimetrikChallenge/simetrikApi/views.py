from rest_framework.decorators import api_view
from simetrikApi import models
from rest_framework.response import Response
from rest_framework import status
from simetrikApi import pagination 

def pagination_params_validation(param, default_value):
  if param == None:
    param = default_value
  return int(param) 

@api_view(["GET"])
def get_tables(request):
  query = models.TablesManager.get_all_tables()
  if query == 'error':
    return Response({'message': 'Something wrong happened'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
  else:
    return Response(query, status=status.HTTP_200_OK)

@api_view(["GET"])
def get_table(request, name):
  limit = request.GET.get('pageSize')
  page = request.GET.get('page')
  limit = pagination_params_validation(limit, 10)
  page = pagination_params_validation(page, 1)
  prop = request.GET.get('prop')
  where = request.GET.get('where')
  equals = request.GET.get('equals')
  offset = pagination.get_offset(page, limit)
  pagination_params = {'page': page, 'limit': limit, 'offset': offset}
  query = models.TablesManager.get_one_table(name, prop, where, equals, pagination_params)
  if query == 'Table does not exist':
    return Response({'message': query}, status=status.HTTP_404_NOT_FOUND)
  count = models.TablesManager.get_count(name, where, equals)
  if count == 'error' or query == 'error':
    return Response({'message': 'Something wrong happened'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
  else:
    paginationResult = pagination.get_pagination_result(page, limit, name, count)
    return Response({'pagination': paginationResult, 'result': query}, status=status.HTTP_200_OK)

@api_view(["POST"])
def create_table(request):
  data = request.data
  if data == {}:
    return Response({'message': '.csv file url is required'}, status=status.HTTP_400_BAD_REQUEST)
  query = models.TablesManager.create_table(data)
  if query == 'Invalid url':
    return Response({'message': query}, status=status.HTTP_400_BAD_REQUEST)
  elif query == 'Error creating table':
    return Response({'message': query}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
  elif query == 'Table already exist':
    return Response({'message': query}, status=status.HTTP_200_OK)
  elif query == 'Table created':
    return Response({'message': query}, status=status.HTTP_201_CREATED)