# Task & Canvas

Task & Canvas brigdes the gap between Google Tasks and Canvas, allowing users to pull and write tasks data from Canvas to Google Tasks

## Installation

1. Clone the project to your local machine '''git clone https://github.com/TuThanhHuy2124/Task-and-Canvas'''
2. Get [Google Credentials](https://developers.google.com/tasks/quickstart/python#authorize_credentials_for_a_desktop_application)
3. Download '''credentials.json''' to the '''Tasks''' folder
4. Get [Canvas API Access Token](https://community.canvaslms.com/t5/Admin-Guide/How-do-I-manage-API-access-tokens-as-an-admin/ta-p/89)
5. Write '''{"token": "<YOUR CANVAS ACCESS TOKEN HERE>"}''' into '''token.json''' and put into the '''Canvas''' folder
6. Run '''py main.py'''

## Usage

```python
import foobar

# returns 'words'
foobar.pluralize('word')

# returns 'geese'
foobar.pluralize('goose')

# returns 'phenomenon'
foobar.singularize('phenomena')
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)
