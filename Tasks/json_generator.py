from datetime import datetime
from googleapiclient.discovery import Resource

def createAndAddTask(service: Resource, * , tasklistID: str, title: str, dueDate: tuple|str = None) -> dict:
    """Create a new task with specified title and add it to task list with tasklistID"""

    newTask = service.tasks().insert(tasklist=tasklistID).execute()
    newTask["title"] = title

    if dueDate is not None:
      if type(dueDate) is tuple:
         dueStr = _formatRFC(*dueDate)
      elif type(dueDate) is str:
         dueStr = dueDate
      newTask['due'] = dueStr

    newTask = service.tasks().update(tasklist=tasklistID, task=newTask["id"], body=newTask).execute()
    return newTask

def getTasksFromTaskList(service: Resource, tasklistID: str) -> dict:
  """Return the dictionary that represents all the tasks in the specified task list"""
   
  response = service.tasks().list(tasklist=tasklistID).execute()
  return response

def createCanvasTaskList(service: Resource, tasklistsList: list) -> str:
   """
   Creat a task list call 'Canvas' (if not already existed) and return its ID.
   Otherwise, return the 'Canvas' task list's ID
   """
   
   checkExistenceList = [tasklist for tasklist in tasklistsList if tasklist['title'] == "Canvas"]
   if not checkExistenceList:
      newList = service.tasklists().insert().execute()
      newList["title"] = "Canvas"
      newList = service.tasklists().update(tasklist=newList["id"], body=newList).execute()
      return newList["id"]
   return checkExistenceList[0]["id"]

def _formatRFC(year: int, month: int, day: int) -> str:
   return f"{year}-{month if len(str(month)) > 1 else f'0{month}'}-{day if len(str(day)) > 1 else f'o{day}'}T00:00:00.000Z"

    