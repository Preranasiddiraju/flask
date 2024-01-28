from flask import Flask, render_template

# Create a Flask instance
app = Flask(__name__)

# Define a route for the root URL ('/')
@app.route('/')
#def hello_world():
#    return 'Hello World!'
#safe
#captalize
#lower
#upper
#title
#trim
#striptags



def index():
    first_name = "Prerana"
    stuff = "This is bold text"

    favorite_burger = ["Fish", "Cheese", "Chicken", 41]
    return render_template("index.html", first_name=first_name, stuff=stuff, favorite_burger=favorite_burger)

# localhost:5000/user/Preru
@app.route('/user/<name>')

def user(name):
    return render_template("user.html", user_name=name)


# Create Custom Error Pages

# Invalid URL
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

# Internal Server Error
@app.errorhandler(500)
def page_not_found(e):
    return render_template("500.html"), 500




# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
