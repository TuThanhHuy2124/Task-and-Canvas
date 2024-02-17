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
with open("Canvas\\token.json") as file:
    data = json.load(file)
accessToken = data["token"]

Task = namedtuple('Task', ['name', 'due'])

def get_course_id() -> list:
    request = urllib.request.Request(course_url + access + accessToken + enrollment_state + state + increaseMax)
    response = urllib.request.urlopen(request)
    list_response = json.load(response)
    return [course['id'] for course in list_response if 'name' in course]

def get_assignments(course_id: str) -> list:
    assignment_url = url + f'/api/v1/courses/{course_id}/assignments'
    request = urllib.request.Request(assignment_url + access + accessToken + increaseMax + future)
    response = urllib.request.urlopen(request)
    list_response = json.load(response)
    for item in list_response:
        if item["due_at"] is not None:
            yield Task(item['name'], item['due_at'])