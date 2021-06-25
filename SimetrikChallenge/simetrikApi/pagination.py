import json

def convertToJson(res):
  result = []
  for row in res:
    result.append(row)
  jsonResponse = json.dumps(result, default=str)
  return jsonResponse

def getOffSet(page, limit):
  offset = (page * limit) - limit
  return offset

def getNextPage(page, limit, name, count):
  rest = count - page * limit
  if (rest > 0):
    nextPage = '/'+name+'?page='+str(page + 1)+'&pageSize='+str(limit)
    return nextPage
  else:
    return None

def getPreviousPage(page, limit, name):
  if (page <= 1):
    return None
  else:
    return '/'+name+'?page='+str(page - 1)+'&pageSize='+str(limit)

def getPaginationResult(page, limit, name, count):
  paginationInfo = {
    'current': '/'+name+'?page='+str(page)+'&pageSize='+str(limit),
    'prev': getPreviousPage(page, limit, name),
    'next': getNextPage(page, limit, name, count)
  }
  convertToJson(paginationInfo)
  return paginationInfo
