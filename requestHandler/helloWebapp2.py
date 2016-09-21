import webapp2


class HelloWebapp2(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello, webapp2!')


class NextOne(webapp2.RequestHandler):
    def get(self):
        self.response.write('Next one!')
