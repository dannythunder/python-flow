import requests
from dotenv import load_dotenv
import json
import os
import warnings

class Flow:
  
  def httpCall(method, endpoint, namespace=None, objectId=None, data=None, params=None):

    load_dotenv()

    if os.getenv('FLOW_AUTHORIZATION') == None:
      raise Exception("Missing FLOW_AUTHORIZATION from .env")

    if os.getenv('FLOW_URL') == None:
      raise Exception("Missing FLOW_URL from .env")
    
    secureRequest = True if os.getenv('FLOW_SECURE_REQUEST') is None else os.getenv('FLOW_SECURE_REQUEST') == "True"

    if(secureRequest == False):
      warnings.filterwarnings("ignore", message="Unverified HTTPS request")

    headers = {}

    headers["Authorization"] = os.getenv("FLOW_AUTHORIZATION")
    headers["Flow-Request-Method"] = method
    headers["Flow-Request-Namespace"] = endpoint

    if params != None:
      headers["Flow-Request-Parameter"] = json.dumps({"parameters": params })

    if objectId is not None:
      headers["Flow-Request-ObjectId"] = objectId

    url = os.getenv("FLOW_URL")

    if endpoint.split('/')[0] == "catalogue":
      url = url + "/api/product/"+endpoint+"/"
    else:
      url = url + "/api/"+endpoint.split('/')[0]+"/"+endpoint+"/"

    try:
      if method in ["LIST","OPEN","DELETE"] and data is None:
        resp = requests.get(url, headers=headers, verify=secureRequest)
      else:
        resp = requests.post(url, headers=headers, json=data, verify=secureRequest)
    except requests.exceptions.SSLError:
      print("Unsecured SSL attempt, add FLOW_SECURE_REQUEST=False to .env file or shell env.")
    except Exception as ex:
      print("Unknown exception:" + str(ex))
    
    try:
      return resp.json()
    except requests.exceptions.JSONDecodeError as jsonError:
      raise Exception("Could not convert to json, response: " + str(resp))
    except Exception as ex:
      raise Exception("Unknown exception:" + str(ex))
    
  def httpList(endpoint, objectId=None, searchItems=None, sortBy=None, sortOrder="ASC"):
    params = None

    if searchItems is not None:
      if params is None:
        params = {}

      params["condition"] = True
      params["condition.values"] = []
      for key, value in searchItems.items():
        params["condition.values"].append({key: value})

    if sortBy is not None:
      if params is None:
        params = {}

      params["sorting"] = True
      params["sorting.by"] = sortBy
      params["sorting.order"] = sortOrder

    return Flow.httpCall("LIST", endpoint, objectId=objectId, params=params)

  def httpOpen(endpoint, objectId=None, data=None):
    return Flow.httpCall("OPEN", endpoint, objectId=objectId, data=data)

  def httpCreate(endpoint, data, objectId=None):
    return Flow.httpCall("CREATE", endpoint, objectId=objectId, data=data)

  def httpUpdate(endpoint, data, objectId=None):
    return Flow.httpCall("UPDATE", endpoint, objectId=objectId, data=data)
