import json
from datetime import datetime

def update(id, name):
  
  # OPEN FILE
  
  with open('data.json') as f:
    data = json.load(f)
    
  # SEARCH OF THE ID
    
  for item in data:
    if item['id'] == id:
      item['desc'] = name
      item['updatedAt'] = str(datetime.now())[:19]
      break
    
  # WRITING THE NEW DATA
    
  with open('data.json', 'w') as f:
    json.dump(data, f, indent=4)