import webapp2
from requestHandler.helloWebapp2 import HelloWebapp2
from requestHandler.helloWebapp2 import NextOne

app = webapp2.WSGIApplication([
    ('/', HelloWebapp2),
    ('/next', NextOne),
], debug=True)


def main():
    from paste import httpserver
    httpserver.serve(app, host='127.0.0.1', port='8080')

if __name__ == '__main__':
    main()
