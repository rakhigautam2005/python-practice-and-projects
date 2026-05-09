#explore the 'flask' module  and create a web server using flask & python.

from flask import Flask

# Create Flask app
app = Flask(__name__)

# Route for home page
@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"  # this is my first flask server web page

# Run the server
if __name__ == "__main__":
    app.run(debug=True)