from http_status import Status


def application(environ, start_response):
    print(environ)
    if environ['PATH_INFO'] == '/info/':
        response_text, status_code, extra_headers = info_url_handler(environ)
    elif environ['PATH_INFO'] == '/':
        response_text, status_code, extra_headers = index_url_handler(environ)
    else:
        response_text, status_code, extra_headers = not_found_handler(environ)
    status_code_message = '{}{}'.format(
        Status(status_code).code,
        Status(status_code).name,
    )
    headers = {
        'Content-Type': 'text/html',
    }
    headers.update(extra_headers)

    start_response(
        status_code_message,
        list(headers.items()),
    )
    return [response_text]


def index_url_handler(environ):
    return b'Index page', 200, {}


def info_url_handler(environ):
    return b'Contact page', 201, {'X-test-header': '123'}


def not_found_handler(environ):
    return b'404', 404, {}
