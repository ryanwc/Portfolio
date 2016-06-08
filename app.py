import os, webapp2, jinja2, re
from webapp2 import redirect_to

template_dir = os.path.join(os.path.dirname(__file__), "templates")
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir),
	autoescape=True, auto_reload=True)
jinja_env.globals['url_for'] = webapp2.uri_for


class Handler(webapp2.RequestHandler):
	def write(self, *a, **kw):
		self.response.out.write(*a, **kw)

	def render_str(self, template, **params):
		t = jinja_env.get_template(template)
		return t.render(params)

	def render(self, template, **kw):
		self.write(self.render_str(template, **kw))

# define template servers
class Index(Handler):
	def get(self):

		self.render("index.html")

app = webapp2.WSGIApplication(
		[webapp2.Route("/", handler=Index, name="index")],
		debug=True)


