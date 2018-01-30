from http_status import Status


def application(environ, start_response):
    # print(environ)

    handlers = {
        '/': index_url_handler,
        '/info/': info_url_handler,
    }
    current_url_handler = handlers.get(
        environ['PATH_INFO'],
        not_found_handler
    )
    response_text, status_code, extra_headers = current_url_handler(environ)

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
