import json
from datetime import datetime

def mark_done(id):
  
  # OPEN FILE
  
  with open('data.json') as f:
    data = json.load(f)

  # FIND OBJECT
    
  for item in data:
    if item['id'] == id:
      item['status'] = 'done'
      item['updatedAt'] = str(datetime.now())[:19]
  
  # WRITE DATA
  
  with open('data.json', 'w') as f:
    json.dump(data, f, indent=4)