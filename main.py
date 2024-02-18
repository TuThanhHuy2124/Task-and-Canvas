import os.path
import urllib.request

from datetime import datetime, timedelta
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build, Resource
from googleapiclient.errors import HttpError
from Tasks.json_generator import *
from Canvas.api import *

# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/tasks.readonly", "https://www.googleapis.com/auth/tasks"]

def main():
  """
  Shows basic usage of the Tasks API.
  Prints the title and ID of the first 10 task lists.
  """
  creds = None
  # The file token.json stores the user's access and refresh tokens, and is
  # created automatically when the authorization flow completes for the first
  # time.
  if os.path.exists("Tasks\\token.json"):
    creds = Credentials.from_authorized_user_file("Tasks\\token.json", SCOPES)
  # If there are no (valid) credentials available, let the user log in.
  if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
      creds.refresh(Request())
    else:
      flow = InstalledAppFlow.from_client_secrets_file(
          "Tasks\\credentials.json", SCOPES
      )
      print(SCOPES)
      creds = flow.run_local_server(port=0)
    # Save the credentials for the next run
    with open("Tasks\\token.json", "w") as token:
      token.write(creds.to_json())

  try:
    service: Resource = build("tasks", "v1", credentials=creds)

    # Call the Tasks API
    results = service.tasklists().list(maxResults=100).execute()
    items = results.get("items", [])
    
    if not items:
      print("No task lists found.")
      return
    
    tasklistID = createCanvasTaskList(service, tasklistsList=items)
    courses = get_course()
    for course in courses:
      assignmentGenerator = get_assignments(*course)
      try:
        parentID = createParentTask(service, tasklistID=tasklistID, title=course.name)
        while True:
          assignment = next(assignmentGenerator)
          #Everything is off by 1 day so I subtract 1
          due = datetime.fromisoformat(assignment.due) - timedelta(days=1)
          createAndAddChildTask(service, tasklistID=tasklistID, title=assignment.name, dueDate=due.isoformat(), parentID=parentID)
      except StopIteration:
        pass
      
    deleteChildlessParentTask(service, tasklistID=tasklistID)
    sortChildrenTask(service, tasklistID=tasklistID)
  except HttpError as err:
    print(err)


if __name__ == "__main__":
  main()