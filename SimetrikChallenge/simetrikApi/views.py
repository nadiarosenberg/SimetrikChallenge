from rest_framework.decorators import api_view
from simetrikApi import models
from django.http import JsonResponse
from rest_framework import status

@api_view(["GET"])
def get_tables(request):
  queryset = models.TablesManager.getTables()
  if queryset == 'error':
    return JsonResponse('Something wrong happened', safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
  else:
    return JsonResponse(queryset, safe=False, status=status.HTTP_200_OK)

@api_view(["GET"])
def get_table(request):
  #prop = request.GET('prop')
  #limit = request.GET('limit')
  #print(prop, limit)
  queryset = models.TablesManager.getOneTable()
  if queryset == 'error':
    return JsonResponse('Something wrong happened', safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
  else:
    return JsonResponse(queryset, safe=False, status=status.HTTP_200_OK)

'''@api_view(["GET"])
def create_table(request):
  queryset = models.TablesManager.createTable()
  if queryset == 'error':
    return JsonResponse('Error creating table', safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
  else:
    return JsonResponse(queryset, safe=False, status=status.HTTP_200_OK)'''