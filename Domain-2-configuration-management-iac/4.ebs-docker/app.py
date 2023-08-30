from flask import Flask
# Print a nice greeting to the user
def say_hello(username = "World"):
 return '<html><body background="https://bit.ly/2NuGl9Q" backgroundposition=center background-repeat=no-repeat background-size=cover style="padding:210px 0; background-color:#000" ><font color="white"><center><h1>Hello %s! , Welcome to the World of AWS DevOps</h1></font><br><br><br></body>' % username

# Some bits of text for the page
header_text = '''
 <html>\n<head> <title>Welcome to AWS Manifold AI Learning Course</title> </head>\n<body>'''

instructions = '''
 <font color="white"><h2><em> Hope you are Enjoying!! - Team Manifold AI Learning</h2></font>\n'''

home_link = '<p><a href="/">Back</a></p>\n'
footer_text = '</body>\n</html>'
# Elastic Beanstalk looks for an 'application' that is callable by default
application = Flask(__name__)
# Add a rule for the index page
application.add_url_rule('/', 'index', (lambda: header_text +  say_hello() + instructions + footer_text))
# Add a rule when the page is accessed with a name appended to the site
# URL
application.add_url_rule('/<username>', 'hello', (lambda username: header_text + say_hello(username) + home_link + footer_text))
# Run the application
if __name__ == "__main__":
 # Setting debug to True enables debug output. This line should be
 # removed before deploying a production application.
 application.debug = True
 application.run(host="0.0.0.0")