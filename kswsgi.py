from wsgiref.simple_server import make_server, demo_app
import ksclock

def ks_app(environ, start_response):
    status = '200 OK' # HTTP Status
    headers = [('Content-type', 'image/png')] # HTTP Headers
    start_response(status, headers)
    #kind = environ.items()[0]['QUERY_STRING']
    #kind = dict(environ.items())['QUERY_STRING']
    if not dict(environ.items())['QUERY_STRING']:
        clock = ksclock.clock("line").save("clock.png")
    f = open("clock.png")
    return f.read()
httpd = make_server('', 8000, ks_app)
# httpd = make_server('', 8000, demo_app)

print "Serving on port 8000..."

# Serve until process is killed
httpd.serve_forever()