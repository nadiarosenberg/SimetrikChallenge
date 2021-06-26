from rest_framework.decorators import api_view
from simetrikApi import models
from django.http import JsonResponse
from rest_framework import status
from simetrikApi import pagination 

def pagination_params_validation(param, default_value):
  if param == None:
    param = default_value
  return int(param) 

@api_view(["GET"])
def get_count(request, name):
  query = models.TablesManager.get_count(name)
  if query == 'Ivalid url':
    return JsonResponse(query, safe=False, status=status.HTTP_400_BAD_REQUEST)
  elif query == 'error':
    return JsonResponse('Something wrong happened', safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
  else:
    return JsonResponse(query, safe=False, status=status.HTTP_200_OK)

@api_view(["GET"])
def get_tables(request):
  query = models.TablesManager.get_all_tables()
  if query == 'error':
    return JsonResponse('Something wrong happened', safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
  else:
    return JsonResponse(query, safe=False, status=status.HTTP_200_OK)

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
  paginationParams = {'page': page, 'limit': limit, 'offset': offset}
  query = models.TablesManager.get_one_table(name, prop, where, equals, paginationParams)
  count = models.TablesManager.get_count(name, where, equals)
  if count == 'error' or query == 'error':
    return JsonResponse('Something wrong happened', safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
  else:
    paginationResult = pagination.get_pagination_result(page, limit, name, count)
    return JsonResponse({'pagination': paginationResult, 'result': query}, safe=False, status=status.HTTP_200_OK)

@api_view(["POST"])
def create_table(request):
  data = request.data
  query = models.TablesManager.create_table(data)
  if query == 'Error creating table':
    return JsonResponse(query, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
  elif query == 'Table already exist':
    return JsonResponse(query, safe=False)
  else:
    return JsonResponse(query, safe=False, status=status.HTTP_200_OK)