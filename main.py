import argparse
from functions.update import update
from functions.add import add
from functions.delete import delete
from functions.mark_in_progress import mark_in_progress
from functions.mark_done import mark_done
from functions.list import listTask

def arg_type(value):
  try:
    return int(value)
  except ValueError:
    return str(value)

def main():
  parse = argparse.ArgumentParser(description="Add Task")
  parse.add_argument("functionName", type=str, help="Type the name of your function")
  parse.add_argument("--first", type=arg_type, help="First Argument")
  parse.add_argument("--second", type=str, help="Second Argument")
  args = parse.parse_args()
  
  match args.functionName:
    case 'add':
      add()
    case 'update':
      update()
    case 'delete':
      delete()
    case 'mark-in-progress':
      mark_in_progress()
    case 'mark-done':
      mark_done()
    case 'list':
      listTask()
      
    
  
if __name__ == "__main__":
  main()
  

