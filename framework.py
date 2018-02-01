# def application(env, start_response):
#     start_response('200 OK', [('Content-Type','text/html')])
#     return [b"Hello hello World"]

def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/plain')])
    return [b'Hello world from a simple WSGI application!']