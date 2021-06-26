import json

def convert_to_json(res):
  result = []
  for row in res:
    result.append(row)
  jsonResponse = json.dumps(result, default=str)
  return jsonResponse

def get_offset(page, limit):
  offset = (page * limit) - limit
  return offset

def get_next_page(page, limit, name, count):
  rest = count - page * limit
  if (rest > 0):
    nextPage = '/'+name+'?page='+str(page + 1)+'&pageSize='+str(limit)
    return nextPage
  else:
    return None

def get_previous_page(page, limit, name):
  if (page <= 1):
    return None
  else:
    return '/'+name+'?page='+str(page - 1)+'&pageSize='+str(limit)

def get_pagination_result(page, limit, name, count):
  pagination_info = {
    'current': '/'+name+'?page='+str(page)+'&pageSize='+str(limit),
    'prev': get_previous_page(page, limit, name),
    'next': get_next_page(page, limit, name, count)
  }
  convert_to_json(pagination_info)
  return pagination_info
