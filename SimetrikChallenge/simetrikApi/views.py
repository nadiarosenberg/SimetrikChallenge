from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from django.http import JsonResponse
import json
import sqlalchemy
from sqlalchemy import create_engine
import pymysql

engine = sqlalchemy.create_engine('mysql+pymysql://root:12345@localhost:3306/simetrikapidb')

def convertToJson(res):
  result = []
  for row in res:
    result.append(row)
  jsonResponse = json.dumps(result, default=str)
  return jsonResponse

@api_view(["GET"])
def get_tables(request):
  try:
    rs = engine.execute('SHOW tables')
    jsonResponse = convertToJson(rs)
    return JsonResponse(jsonResponse,  safe=False, status=status.HTTP_200_OK)
  except:
    return JsonResponse('Something wrong happened', safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(["GET"])
def get_table(request, name):
  try:
    q = "Select * FROM {}".format(name)
    rs = engine.connect().execute(q)
    jsonResponse = convertToJson(rs)
    return JsonResponse(rs, safe=False, status=status.HTTP_200_OK)
  except:
    return JsonResponse('Something wrong happened', safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)