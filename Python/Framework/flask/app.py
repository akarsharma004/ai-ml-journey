from flask import Flask,render_template

# 1. INITIALIZATION
# Creating an instance of the Flask class. 
# This object acts as our WSGI (Web Server Gateway Interface) application.
app = Flask(__name__)

# 2. ROUTING LOGIC
# The @app.route decorator binds a URL path to a specific Python function.

@app.route("/")
def welcome():
    """
    Handler for the root URL ('/').
    When a user visits http://127.0.0.1:5000/, this function executes.
    """
    return "Welcome to this Flask Course"

@app.route("/index")
def index():
    """
    Handler for the '/index' URL path. This will redirect the to the html file. This is done by going to template folder(jinja 2) and search for the html file.
    """
    return render_template('index.html')

# 3. EXECUTION BLOCK
if __name__ == "__main__":
    # app.run starts the local development server.
    # debug=True enables:
    #   - Auto-reload: Server restarts when you save code changes.
    #   - Debugger: Provides interactive error tracking in the browser.
    app.run(debug=True)