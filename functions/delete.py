import json

def delete(id):
  
  # OPEN FILE
  
  with open('data.json') as f:
    data = json.load(f)
    
  # EXCLUDE TARGET OBJECT FROM DATA
    
  data = [item for item in data if item['id'] != id]
  
  # WRITE JSON

  with open('data.json', 'w') as f:
    json.dump(data, f, indent=4)