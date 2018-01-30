from http_status import Status


def application(environ, start_response):
    print(environ)
    if environ['PATH_INFO'] == '/info/':
        response_text, status_code, extra_headers = info_url_handler(environ)
    else:
        response_text = b'404'
    status_code_message = '{}{}'.format(
        Status(status_code).code,
        Status(status_code).name
    )
    start_response(
        status_code_message,
        [('Content-Type', 'text/html')])
    return [response_text]

def info_url_handler(environ):
    return b'Contact page', 201, {}