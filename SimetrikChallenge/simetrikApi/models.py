from django.db import models
import pandas
import sqlalchemy
import pymysql
class TablesManager:
  def createTable(data):
    try:
      engine = sqlalchemy.create_engine('mysql+pymysql://root:12345@localhost:3306/simetrikapidb')
      url = data.get('url')
      name = data.get('name')
      csvReaded = pandas.read_csv(url)
      try:
        database = csvReaded.to_sql(name, engine, if_exists='fail')
        engine.dispose()
        return 'Table created'
      except:
        engine.dispose()
        return 'Table already exist'
    except:
      engine.dispose()
      return 'Error creating table'
      
  def getTables():
    try:
      engine = sqlalchemy.create_engine('mysql+pymysql://root:12345@localhost:3306/simetrikapidb')
      connection = engine.raw_connection()
      cursor = connection.cursor(pymysql.cursors.DictCursor)
      cursor.execute('SHOW tables')
      result = cursor.fetchall()
      engine.dispose()
      return result
    except:
      return 'error'
  
  def getOneTable(name, prop, paginationParams):
    try:
      limit = paginationParams.get('limit')
      offset = paginationParams.get('offset')
      engine = sqlalchemy.create_engine('mysql+pymysql://root:12345@localhost:3306/simetrikapidb')
      connection = engine.raw_connection()
      cursor = connection.cursor(pymysql.cursors.DictCursor)
      q = 'SELECT * FROM {} ORDER BY {} DESC LIMIT {} OFFSET {}'.format(name, prop, limit, offset)
      cursor.execute(q)
      result = cursor.fetchall()
      engine.dispose()
      return result
    except:
      return 'error'

  def getCount(name):
    try:
      engine = sqlalchemy.create_engine('mysql+pymysql://root:12345@localhost:3306/simetrikapidb')
      connection = engine.raw_connection()
      cursor = connection.cursor(pymysql.cursors.DictCursor)
      qCount = 'SELECT COUNT(*) FROM {}'.format(name)
      cursor.execute(qCount)
      result = cursor.fetchall()
      engine.dispose()
      count = result[0].get('COUNT(*)')
      return count
    except:
      return 'error'