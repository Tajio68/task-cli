import argparse
from functions.update import update
from functions.add import add
from functions.delete import delete
from functions.mark_in_progress import mark_in_progress
from functions.mark_done import mark_done
from functions.list import listTask

def main():
  
  parse = argparse.ArgumentParser(description="Add Task")
  subparsers = parse.add_subparsers(dest='command', help="subcommands")
  
  # ADD SUBPARSER
  
  add_parse = subparsers.add_parser('add', help="Add new task")
  add_parse.add_argument('task', type=str, help="Task to add")
  
  # UPDATE SUBPARSER
  
  update_parse = subparsers.add_parser('update', help='Update task')
  update_parse.add_argument('id', type=int, help='ID of the task to update')
  update_parse.add_argument('name', type=str, help='Name of the task to update')
  
  # DELETE SUBPARSER
  
  delete_parse = subparsers.add_parser('delete', help='Delete a task')
  delete_parse.add_argument('id', type=int, help='ID of the task to delete')
  
  # MARK-IN-PROGRESS SUBPARSER
  
  mark_in_progress_parse = subparsers.add_parser('mark-in-progress', help='Mark a task in progress')
  mark_in_progress_parse.add_argument('id', type=int, help='ID of the task to mark')
  
  # MARK-DONE SUBPARSER
  
  mark_done_parse = subparsers.add_parser('mark-done', help='Mark a task done')
  mark_done_parse.add_argument('id', type=int, help='ID of the task to mark')

  # LIST SUBPARSER

  list_parse = subparsers.add_parser('list', help='See the lists')
  list_parse.add_argument('status', nargs='?', choices=['done', 'todo', 'in-progress'], default=None, help='Display of the lists')

  args = parse.parse_args()

  match args.command:
    case 'add':
      add(args.task)
    case 'update':
      update(args.id, args.name)
    case 'delete':
      delete(args.id)
    case 'mark-in-progress':
      mark_in_progress(args.id)
    case 'mark-done':
      mark_done(args.id)
    case 'list':
      listTask(args.status)
    case _:
      print(f'Error: command \'{args.functionName}\' does not exist')
  
if __name__ == "__main__":
  main()