# Task & Canvas

**Task & Canvas** bridges the gap between Google Tasks and Canvas, allowing users to pull and write task data from Canvas to Google Tasks

## Installation

1. Clone the project to your local machine ```git clone https://github.com/TuThanhHuy2124/Task-and-Canvas```
2. Get [Google Credentials](https://developers.google.com/tasks/quickstart/python#authorize_credentials_for_a_desktop_application)
3. Download ```credentials.json``` to the ```Tasks``` folder
4. Get [Canvas API Access Token](https://community.canvaslms.com/t5/Admin-Guide/How-do-I-manage-API-access-tokens-as-an-admin/ta-p/89)
5. Write ```{"token": "<YOUR CANVAS ACCESS TOKEN HERE>"}``` into ```token.json``` and put into the ```Canvas``` folder
6. Create a virtual environment ```python -m venv .venv```
7. Activate the virtual environment ```.venv/Scripts/activate```
8. Install the Google client library ```pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib```

## Usage

Run ```python main.py```, log in to your Google account, and then check your Google Tasks

## Acknowledgments

* [Google Quick Start Code](https://github.com/googleworkspace/python-samples/blob/main/tasks/quickstart/quickstart.py)

## License

MIT License

    Copyright (c) [2024] [Thanh Huy Tu]
  
    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:
    
    The above copyright notice and this permission notice shall be included in all
    copies or substantial portions of the Software.
    
    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
    SOFTWARE.
