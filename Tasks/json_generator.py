from datetime import datetime
from googleapiclient.discovery import Resource

def createAndAddTask(service: Resource, * , tasklistID: str, title: str, dueDate: tuple = None) -> dict:
    """Create a new task with specified title and add it to task list with tasklistID"""

    newTask = service.tasks().insert(tasklist=tasklistID, body=dict()).execute()
    newTask["title"] = title
    if dueDate is not None:
       dueStr = formatRFC(*dueDate)
       newTask['due'] = dueStr
    newTask = service.tasks().update(tasklist=tasklistID, task=newTask["id"], body=newTask).execute()
    return newTask

def formatRFC(year: int, month: int, day: int) -> str:
   return f"{year}-{month if len(str(month)) > 1 else f'0{month}'}-{day if len(str(day)) > 1 else f'o{day}'}T00:00:00.000Z"

def getTasksFromTaskList(service: Resource, tasklistID: str) -> dict:
  """Return the dictionary that represents all the tasks in the specified task list"""

  response = service.tasks().list(tasklist=tasklistID).execute()
  return response

    