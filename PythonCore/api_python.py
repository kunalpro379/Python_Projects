import requests as rq
import json
import os
def FetchRandomUser():
    url ="https://api.freeapi.app/api/v1/public/randomusers?page=1&limit=10"
    response =requests.get(url)
    data =response.json()

    if data["success"] and "data" in data:
        