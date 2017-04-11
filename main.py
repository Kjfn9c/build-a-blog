import webapp2
import cgi
import jinja2
import os
from google.appengine.ext import db


template_dir = os.path.join(os.path.dirname(__file__), "templates")
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir))

class BlogPost(db.Model):
    title = db.StringProperty(required = True)
    body = db.TextareaProperty(required = True)
    created = db.DateTimeProperty(auto_now_add = True)

class Handler(webapp2.RequestHandler):
    def renderError(self, error_code):
        self.error(error_code)
        self.response.write("Oops! Something went wrong.")

class Index(Handler):
    def get(self):
        t = jinja_env.get_template("frontpage.html")
        error = cgi.escape(self.request.get("error"), quote=True)
        content = t.render(error=error)
        self.response.write(content)

#class Blog(Handler):
    #def post(self):

class NewPost(Handler):
    def post(self):
            New_post = self.request.get("newpost")

            New_post_escaped = cgi-escape(New_post, quote=True)
            t = jinja_env.get_template("newpost.html")
            content = t.render(newpost = new_movie_escaped)

            self.response.write(content)

app = webapp2.WSGIApplication([
    ('/', Index),
    ('/blog', Blog),
    ('/newpost', NewPost)
], debug=True)
