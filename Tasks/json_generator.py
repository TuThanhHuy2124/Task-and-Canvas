from datetime import datetime
from googleapiclient.discovery import Resource
from collections import namedtuple

def createParentTask(service: Resource, * , tasklistID: str, title: str) -> str:
   """Create a parent task with the same name as the course name"""

   parentTask = service.tasks().insert(tasklist=tasklistID).execute()
   parentTask['title'] = title
   parentTask = service.tasks().update(tasklist=tasklistID, task=parentTask["id"], body=parentTask).execute()
   return parentTask['id']

def createAndAddChildTask(service: Resource, * , tasklistID: str, title: str, dueDate: tuple|str = None, parentID: str = None) -> dict:
   """Create a new task with specified title and add it to task list with tasklistID under task with parentID"""
   
   newTask = service.tasks().insert(tasklist=tasklistID).execute()
   newTask["title"] = title

   if dueDate is not None:
      if type(dueDate) is tuple:
         dueStr = _formatRFC(*dueDate)
      elif type(dueDate) is str:
         dueStr = dueDate
   newTask['due'] = dueStr

   newTask = service.tasks().update(tasklist=tasklistID, task=newTask["id"], body=newTask).execute()
   newTask = service.tasks().move(tasklist=tasklistID, task=newTask["id"], parent=parentID).execute()

   return newTask

def sortChildrenTask(service: Resource, * , tasklistID: str) -> None:
   """Sort all children tasks by due date"""

   taskDict = dict()
   childTask = namedtuple('childTask', ["id", "due", "parent"])
   tasklistObj = getTasksFromTaskList(service, tasklistID=tasklistID)
   tasklist = tasklistObj["items"]
   childrenTasks = {childTask(task['id'], task['due'], task['parent']) for task in tasklist if "parent" in task}
   
   for task in childrenTasks:
      if task.parent not in taskDict:
         taskDict[task.parent] = [task]
      else:
         taskDict[task.parent].append(task)

   for childrenList in taskDict.values():
      childrenList.sort(key=lambda x: datetime.fromisoformat(x.due))

   for parentID, childrenList in taskDict.items():
      for i in range(0, len(childrenList)):
         if i == 0:
            service.tasks().move(tasklist=tasklistID, 
                                 task=childrenList[i].id, 
                                 parent=parentID).execute()
         else:
            service.tasks().move(tasklist=tasklistID, 
                                 task=childrenList[i].id, 
                                 parent=parentID, 
                                 previous=childrenList[i-1].id).execute()
            
def markComplete(service: Resource, * , tasklistID: str, taskBody: dict) -> None:
   print(taskBody, "\n")
   taskBody["status"] = "completed"
   service.tasks().update(tasklist=tasklistID, task=taskBody["id"], body=taskBody).execute()

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

    