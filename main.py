import webapp2
import cgi
import jinja2
import os
from google.appengine.ext import db

template_dir = os.path.join(os.path.dirname(__file__), "templates")
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape = True)

class BlogPost(db.Model):
    title = db.StringProperty(required = True)
    body = db.StringProperty(required = True)
    created = db.DateTimeProperty(auto_now_add = True)

class Handler(webapp2.RequestHandler):
    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)
    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)
    def render(self, template, **kw):
        self.write(self.render_str(template, **kw))
    def renderError(self, error_code):
        self.error(error_code)
        self.response.write("Oops! Something went wrong.")

class MainPage(Handler):
    def render_front(self, title="", body="", error=""):
        posts = db.GqlQuery('SELECT * FROM BlogPost ORDER BY created DESC LIMIT 5')
        self.render("Frontpage.html", title = title, body = body, error = error, posts = posts)

    def get(self):
        self.render_front()

    def post(self):
        title = self.request.get("title")
        body = self.request.get("body")

        if title and body:
            a = BlogPost(title=title, body=body)
            a.put()
            self.redirect("/")
        else:
            error = "Actually type something!"
            self.render_front(title, body, error)

class NewPost(Handler):
        def render_newpost(self, title="", body="", error=""):
            posts = db.GqlQuery('SELECT * FROM BlogPost ORDER BY created DESC LIMIT 5')
            self.render("newpost.html", title = title, body = body, error = error, posts = posts)

        def get(self):
            self.render_newpost()

        def post(self):
            title = self.request.get("title")
            body = self.request.get("body")

#class ViewPostHandler(webapp2.RequestHandler):
    #def get(self, id):
        #self.response.write()

#webapp2.Route('//<id:\d+>', ViewPostHandler)

app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/newpost', NewPost)
    #('//<id:\d+>', ViewPostHandler)
], debug=True)
