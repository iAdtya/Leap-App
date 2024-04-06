import requests
from celery import Celery


app = Celery('tasks', backend='rpc://', broker='pyamqp://')

@app.task
def fetch_cat_fact():
  response = requests.get("https://cat-fact.herokuapp.com/facts")
  if response.status_code == 200:
    data = response.json()
    if data:  # check if data is not empty
      return {"fact": data[0]["text"]}  # return the "text" field of the first dictionary in the list
    else:
      return {"error": "No facts found"}
  else:
    return {"error": "Unable to fetch cat facts"}