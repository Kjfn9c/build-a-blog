import webapp2
import cgi
import jinja2
import os

template_dir = os.path.join(os.path.dirname(__file__), "templates")
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir))

class MainHandler(webapp2.RequestHandler):
    def get(self):
        t = jinja_env.get_template("frontpage.html")
        error = cgi.escape(self.request.get("error"), quote=True)
        content = t.render(error=error)
        self.response.write(content)

#class Blog(webapp2.RequestHandler):
    #def post(self):

class NewPost(webapp2.RequestHandler):
    def post(self):
            New_post = self.request.get("newpost")

            New_post_escaped = cgi-escape(New_post, quote=True)
            t = jinja_env.get_template("newpost.html")
            content = t.render(newpost = new_movie_escaped)

            self.response.write(content)

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/Blog'),
    ('/NewPost')
], debug=True)
