def application(environ, start_response):
    print(environ)
    if environ['PATH_INFO'] == '/info/':
        response_text = b'Contact page'
    else:
        response_text = b'404'
    start_response('200 OK', [('Content-Type', 'text/html')])
    return [response_text]
