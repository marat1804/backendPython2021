"""
Simple WSGI app
"""

import json
from datetime import datetime


def app(environ, start_response):
    """
	Simple JSON sender
	"""
    url = environ['RAW_URI']
    time = datetime.now().strftime("%H:%M:%S")
    data_dict = {
        'url': url,
        'time': time}
    data = json.dumps(data_dict, indent=4).encode('utf-8')
    status = '200 OK'
    response_headers = [
        ('Content-type', 'application/json'),
        ('Content-Length', str(len(data)))
    ]
    start_response(status, response_headers)
    return iter([data])
