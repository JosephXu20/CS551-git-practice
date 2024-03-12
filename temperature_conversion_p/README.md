# Temperature Conversion using Python and Flask
A python based web application for temperature conversion with no models. This is part of a 'deliberate practice' coding exercise. You can do this on your own or as part of a pair programming experience. Only look at the code in the repo when you're done.

The goal of the exercise is to think about how you'd solve this challenge, and to work at developing code to make the idea work. There is no 'correct' version of this code. The purpose is spend time on 'deliberate practice' to gain more experience creating 
Python web applications.

The formula for conversion from farhrenheit to celsius is:

        F to C: (F - 32) * 5/9
        C to F: (C * 9/5) + 32

## First, create the app basics
When working with python apps you should use a virtual environment so that your applications are self-contained and you can change the version of python and associated libraries as required. We'll use https://github.com/pyenv/pyenv in this example.

Create a new project folder called 'temp_converter' and then cd into the folder via the terminal and execute these commands:

        pyenv local 3.7.0 # this sets the local version of python to 3.7.0
        python3 -m venv .venv # this creates the virtual environment for you
        source .venv/bin/activate # this activates the virtual environment
        pip install --upgrade pip [ this is optional]  # this installs pip, and upgrades it if required.

We will use Flask (https://flask.palletsprojects.com/en/1.1.x/) as our web framework for the application. We install that with 

        pip install flask

And that will install flask with its associated dependencies. We can now start to build the application.

## Start the web components 
Create a new file called temp_c.py in the main folder.
Put this code in the file:
        # a temperature conversion app
        from flask import Flask, render_template
        app = Flask(__name__)

        @app.route('/')
        def index():
            return render_template("index.html")

We'll use an html template for the view in the browser to make it easier to write than if we did the view as a method and outout html in the temp_c.py file. 

Create a folder 'templates' in the main folder. Inside 'templates' create a file called 'index.html' and put this into that file:

        <!DOCTYPE html>
            <html>
                <head>
                    <title>Temperature Conversion</title>
                </head>
            <body>
            <h1>Temperature Conversion</h1>
            <p>Your converted temperature of x in F is y in C </p>
            </body>
        </html>

We can confirm this runs by setting a few variables in your environment via the terminal (this assumes you're either using Linus or MacOS)

        export FLASK_APP=temp_c.py
        export FLASK_ENV=development
        python3 -m flask run

You can now view your site at localhost:5000 in the browser. It won't show much, but is enough to confirm that everything works correctly.

## Add in the Temperature Conversion Part

With that running, we're ready to do the work. Just refresh the page, modify the form, try it, etc. As you have errors, just edit the file and then refresh the page.

You can get started by creating a form in the index.html file to enter the temperature to convert. The form needs a number field to take the value to convert, and a submit button. We can also modify the original line to show the requested temperature, and its converted value.

    <form action="/" method="post">
        <p>Enter the temperature in fahrenheit to convert to celsius:</p>
    <input type="number" name="temp">
    <input type="submit" value="Convert">
    </form>
    <p>
    Your temperature of {{ temp }} in F converts to {{ converted_t }} in C
    </p>

We can rewrite the method in the temp_c.py file to check if the page request is a GET or a POST, and respond accordingly.
We need to declare the variables that we pass back to the index.html page so that they have a value even when it is a GET request. We also need to convert the input value from the string that's in the form to an integer before we can use it to determine the temperature in celsius.

    from flask import Flask, render_template, request
    app = Flask(__name__)

    @app.route('/', methods=["GET", "POST"])
    def index():
        converted_t = None
        temp = None
        if request.method== "POST":
            temp = int(request.form["temp"])
            converted_t = (temp-32)*0.5556
        return render_template("index.html", converted_t=converted_t, temp=temp)

## Take it further

Round one: This version does the conversion in the index() method. You could move the conversion to a separate method so that you have more scope for change in round two.

Round two: Build on the previous round so that you can convert from celsius to farhrenheit in the same form by adding a radio button, which will let you indicate which way you want to do the conversion. 

Round three: Develop some other feature to push the boundaries of what you want to learn with Flask. For example, you might add two methods (convert_t_f, and convert_t_c) which are called as needed from index method.