from http_status import Status


class App:
    def __init__(self):
        self.handlers = {}

    def __call__(self, environ, start_response):
        current_method = environ['REQUEST_METHOD']
        current_url_handler, allowed_methods = self.handlers.get(
            environ['PATH_INFO'],
            self.not_found_handler
        )
        if current_method not in allowed_methods:
            current_url_handler = self.not_allowed_handler

        response_text, status_code, extra_headers = current_url_handler(
            environ
        )

        status_code_message = '{} {}'.format(
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
        return [response_text.encode('utf-8')]

    def register_handler(self, url, methods=None):
        methods = methods or ['GET']

        def wrapped(handler):
            self.handlers[url] = handler, methods
        return wrapped


    @staticmethod
    def not_found_handler(environ):
        return '404', 404, {}

    @staticmethod
    def not_allowed_handler(environ):
        return 'Not allowed', 405, {}

application = App()

@application.register_handler('/cart/', methods=['GET', 'POST'])
def cart_url_handler(environ):
    return 'Cart page', 200, {}

@application.register_handler('/')
def index_url_handler(environ):
    return 'Index page', 200, {}

@application.register_handler('/info/')
def info_url_handler(environ):
    return 'Contact page', 201, {'X-test-header': '123'}


