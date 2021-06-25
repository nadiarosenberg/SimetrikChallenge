from django.db import models
import pandas
import sqlalchemy
import pymysql
import json
import io

'''def dictfetchall(engine):
  desc = engine.description
  return [
    dict(zip([col[0] for col in desc], row))
    for row in engine.fetchall()
  ]'''

def convertToJson(res):
  result = []
  for row in res:
    result.append(row)
  jsonResponse = json.dumps(result, default=str)
  return jsonResponse

class TablesManager:
  def createTable(url):
    try:
      engine = sqlalchemy.create_engine('mysql+pymysql://root:12345@localhost:3306/simetrikapidb')
      data = pandas.read_csv(url)
      try:
        database = data.to_sql('fig4',engine, if_exists='fail')
        engine.dispose()
        return 'Table created'
      except:
        engine.dispose()
        return 'Table already exist'
    except:
      return 'Error creating table'
      
  def getTables():
    try:
      engine = sqlalchemy.create_engine('mysql+pymysql://root:12345@localhost:3306/simetrikapidb')
      rs = engine.execute('SHOW tables')
      engine.dispose()
      rsToJson = convertToJson(rs)
      return rsToJson
    except:
      return 'error'
  
  def getOneTable():
    try:
      engine = sqlalchemy.create_engine('mysql+pymysql://root:12345@localhost:3306/simetrikapidb')
      prop = 'Day'
      limit = 2
      name = 'fig4'
      q = 'SELECT * FROM {} ORDER BY {} DESC LIMIT {}'.format(name, prop, limit)
      rs = engine.connect().execute(q)
      engine.dispose()
      rsToJson = convertToJson(rs)
      return rsToJson
    except:
      return 'error'

