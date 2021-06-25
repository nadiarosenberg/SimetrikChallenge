from pandas.core import indexing
from rest_framework.decorators import api_view
from simetrikApi import models
from django.http import JsonResponse
from rest_framework import status
from simetrikApi import pagination 

@api_view(["GET"])
def get_count(request, name):
  query = models.TablesManager.getCount(name)
  if query == 'error':
    return JsonResponse('Something wrong happened', safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
  else:
    return JsonResponse(query, safe=False, status=status.HTTP_200_OK)

@api_view(["GET"])
def get_tables(request):
  query = models.TablesManager.getTables()
  if query == 'error':
    return JsonResponse('Something wrong happened', safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
  else:
    return JsonResponse(query, safe=False, status=status.HTTP_200_OK)

@api_view(["GET"])
def get_table(request, name):
  prop = request.GET.get('prop')
  limit = request.GET.get('pageSize')
  if limit==None:
    limit = 10
  else:
    int(limit)
  page = request.GET.get('page')
  if page == None:
    page = 1
  else:
    int(page)
  where = request.GET.get('where')
  equals = request.GET.get('equals')
  offset = pagination.getOffSet(page, limit)
  paginationParams = {'page': page, 'limit': limit, 'offset': offset}
  query = models.TablesManager.getOneTable(name, prop, where, equals, paginationParams)
  count = models.TablesManager.getCount(name, where, equals)
  paginationResult = pagination.getPaginationResult(page, limit, name, count)
  if query == 'error':
    return JsonResponse('Something wrong happened', safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
  else:
    return JsonResponse({'pagination': paginationResult, 'result': query}, safe=False, status=status.HTTP_200_OK)

@api_view(["POST"])
def create_table(request):
  data = request.data
  query = models.TablesManager.createTable(data)
  if query == 'Error creating table':
    return JsonResponse(query, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
  elif query == 'Table already exist':
    return JsonResponse(query, safe=False)
  else:
    return JsonResponse(query, safe=False, status=status.HTTP_200_OK)