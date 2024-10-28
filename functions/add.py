import json
from datetime import datetime

def add(valueName):
  
  # OPEN JSON
  
  try:
    with open('data.json') as f:
      dataFile = json.load(f)
  except FileNotFoundError:
    dataFile = []
    
  # FIND MAX INDEX
    
  max_id_object = (max(dataFile, key=lambda obj: obj['id']))['id'] + 1
  
  # CREATION OF THE OBJECT
  
  data = {
    "id": max_id_object,
    "desc": valueName,
    "status": 'todo',
    "createdAt": str(datetime.now())[:19],
    "updatedAt": str(datetime.now())[:19]
  }
  
  # ADDING TO FILE
  
  dataFile.append(data)
  
  with open('data.json', 'w') as f:
    json.dump(dataFile, f, indent=4)
    
  # CONFIRMATION OUTPUT
    
  print(f'Task added successfully (ID: {max_id_object})')