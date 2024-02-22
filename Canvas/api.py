from collections import namedtuple
import urllib.request
import json

url = 'https://canvas.eee.uci.edu'
course_url = url + '/api/v1/courses'
access = '?access_token='
enrollment_state = "&enrollment_state="
state = "active"
increaseMax = "&per_page=100"
future = "&bucket=future"
ungraded ="&bucket=ungraded"
with open("Canvas\\token.json") as file:
    data = json.load(file)
accessToken = data["token"]

Course = namedtuple('Course', ['id', 'name'])
Task = namedtuple('Task', ['course_name','name', 'due'])

def get_course() -> list:
    request = urllib.request.Request(course_url + access + accessToken + enrollment_state + state + increaseMax)
    response = urllib.request.urlopen(request)
    list_response = json.load(response)
    return [Course(course['id'], course['name']) for course in list_response if 'name' in course]

def get_assignments(course_id: str, course_name: str) -> list:
    assignment_url = url + f'/api/v1/courses/{course_id}/assignments'
    request = urllib.request.Request(assignment_url + access + accessToken + increaseMax + future)
    response = urllib.request.urlopen(request)
    list_response = json.load(response)
    for item in list_response:
        if item["due_at"] is not None:
            yield Task(course_name, item['name'], item['due_at'])

def get_ungraded(course_id: str, course_name: str) -> list:
    assignment_url = url + f'/api/v1/courses/{course_id}/assignments'
    request = urllib.request.Request(assignment_url + access + accessToken + increaseMax + ungraded)
    response = urllib.request.urlopen(request)
    list_response = json.load(response)
    for item in list_response:
        yield Task(course_name, item['name'], item['due_at'])

for course in get_course():
    get_ungraded(course_id=course.id, course_name=course.name)