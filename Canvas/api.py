import urllib.request
import json
url = 'https://canvas.eee.uci.edu'
course_url = url + '/api/v1/courses'
access = '?access_token='


def get_course_id() -> list:
    request = urllib.request.Request(course_url + access)
    response = urllib.request.urlopen(request)
    list_response = json.load(response)
    return [course['id'] for course in list_response if 'name' in course]

def get_assignments(course_id: str) -> list:
    assignment_url = url + f'/api/v1/courses/{course_id}/assignments'
    request = urllib.request.Request(assignment_url + access + '&bucket=unsubmitted&per_page=100')
    response = urllib.request.urlopen(request)
    list_response = json.load(response)
    return list_response
