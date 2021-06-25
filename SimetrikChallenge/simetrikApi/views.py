from rest_framework.decorators import api_view
from simetrikApi import models
from django.http import JsonResponse
from rest_framework import status

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
  limit = request.GET.get('limit')
  query = models.TablesManager.getOneTable(name, prop, limit)
  if query == 'error':
    return JsonResponse('Something wrong happened', safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
  else:
    return JsonResponse(query, safe=False, status=status.HTTP_200_OK)

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