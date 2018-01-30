from http_status import Status


class App:
    def __init__(self):
        self.handlers = {}

    def __call__(self, environ, start_response):
        current_url_handler = self.handlers.get(
            environ['PATH_INFO'],
            self.not_found_handler
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

    def register_handler(self, url):
        def wrapped(handler):
            self.handlers[url] = handler
        return wrapped

    @staticmethod
    def not_found_handler(environ):
        return b'404', 404, {}

application = App()

@application.register_handler('/cart/')
def cart_url_handler(environ):
    return b'Cart page', 200, {}

@application.register_handler('/')
def index_url_handler(environ):
    return b'Index page', 200, {}

@application.register_handler('/info/')
def info_url_handler(environ):
    return b'Contact page', 201, {'X-test-header': '123'}


