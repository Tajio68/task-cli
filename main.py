import argparse
from functions.add import add

def arg_type(value):
  try:
    return int(value)
  except ValueError:
    return str(value)

def main():
  print('test')
  parse = argparse.ArgumentParser(description="Add Task")
  parse.add_argument("functionName", type=str, help="Type the name of your function")
  parse.add_argument("--first", type=arg_type, help="First Argument")
  parse.add_argument("--second", type=str, help="Second Argument")
  
  args = parse.parse_args()
  
if __name__ == "__main__":
  main()
  

