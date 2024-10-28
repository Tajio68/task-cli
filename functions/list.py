import json

def listTask(status):
  
  # OPEN FILE
  
  with open('data.json') as f:
    data = json.load(f)
  
  # DISPLAY TASKS
  
  for item in data:
    if item['status'] == status:
      print(f'({item["id"]}) {item["desc"]} : {item["status"]}')
    elif status == None:
      print(f'({item["id"]}) {item["desc"]} : {item["status"]}')