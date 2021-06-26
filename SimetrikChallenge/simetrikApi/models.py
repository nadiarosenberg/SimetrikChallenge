from django.db import models
import pandas
import sqlalchemy
import pymysql
from simetrikApi import uploadCsv
import os
from dotenv import load_dotenv

load_dotenv(verbose=True)

ENGINE_STRING = os.getenv('DB_URL')

def get_name(url):
  file_dir, file_name = os.path.split(url)
  validate = file_name.find('.csv')
  if(validate == -1):
    return 0
  else:
    name = file_name.strip('.csv')
  return name

def is_column_validation(name, param):
  q = 'SELECT * FROM {} LIMIT 1'.format(name)
  engine = sqlalchemy.create_engine(ENGINE_STRING)
  connection = engine.raw_connection()
  cursor = connection.cursor(pymysql.cursors.DictCursor)
  cursor.execute(q)
  field_names = [i[0] for i in cursor.description]
  engine.dispose()
  for i in field_names:
    if param == i:
      return param
  param = None
  return param

def sql_sentence(name, where, equals, prop, limit, offset):
  q=''
  if (where == None and prop == None ):
    q = 'SELECT * FROM {} LIMIT {} OFFSET {}'.format(name, limit, offset)
    return q
  elif (where == None and prop != None):
     q = 'SELECT * FROM {} ORDER BY {} DESC LIMIT {} OFFSET {}'.format(name, prop, limit, offset)
     return q
  elif (where != None and prop == None):
    q = 'SELECT * FROM {} WHERE {} = "{}" LIMIT {} OFFSET {}'.format(name, where, equals, limit, offset)
    return q
  elif (where != None and prop != None):
    q = 'SELECT * FROM {} WHERE {} = "{}" ORDER BY {} DESC LIMIT {} OFFSET {}'.format(name, where, equals, prop, limit, offset)
    return q

def sql_count_sentence(name, where, equals):
  q_count =''
  if (where == None):
    q_count = 'SELECT COUNT(*) FROM {}'.format(name)
    return q_count
  else:
    q_count = 'SELECT COUNT(*) FROM {} WHERE {} = "{}"'.format(name, where, equals)
    return q_count
class TablesManager:
  def create_table(data):
    client_url = data.get('url')
    name = get_name(client_url)
    if name == 0:
      return 'Invalid url'
    try:
      engine = sqlalchemy.create_engine(ENGINE_STRING)
      connection = engine.raw_connection()
      cursor = connection.cursor(pymysql.cursors.DictCursor)
      cursor.execute('SELECT * FROM {} LIMIT 1'.format(name))
      engine.dispose()
      return 'Table already exist'
    except:
      url = uploadCsv.upload_file(client_url)
      try:
        csv_readed = pandas.read_csv(url)
        database = csv_readed.to_sql(name, engine, if_exists='fail')
        engine.dispose()
        return 'Table created'
      except:
        engine.dispose()
        return 'Error creating table'
      
  def get_all_tables():
    try:
      engine = sqlalchemy.create_engine(ENGINE_STRING)
      connection = engine.raw_connection()
      cursor = connection.cursor(pymysql.cursors.DictCursor)
      cursor.execute('SHOW tables')
      result = cursor.fetchall()
      engine.dispose()
      return result
    except:
      engine.dispose()
      return 'error'
  
  def get_one_table(name, prop, where, equals, paginationParams):
    try:
      limit = paginationParams.get('limit')
      offset = paginationParams.get('offset')
      prop = is_column_validation(name, prop)
      where = is_column_validation(name, where)
      q = sql_sentence(name, where, equals, prop, limit, offset)
      engine = sqlalchemy.create_engine(ENGINE_STRING)
      connection = engine.raw_connection()
      cursor = connection.cursor(pymysql.cursors.DictCursor)
      cursor.execute(q)
      result = cursor.fetchall()
      engine.dispose()
      return result
    except:
      engine.dispose()
      return 'error'

  def get_count(name, where, equals):
    try:
      where = is_column_validation(name, where)
      engine = sqlalchemy.create_engine(ENGINE_STRING)
      connection = engine.raw_connection()
      cursor = connection.cursor(pymysql.cursors.DictCursor)
      q_count = sql_count_sentence(name, where, equals)
      cursor.execute(q_count)
      result = cursor.fetchall()
      engine.dispose()
      count = result[0].get('COUNT(*)')
      return count
    except:
      engine.dispose()
      return 'error'