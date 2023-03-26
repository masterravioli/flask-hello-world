# Flask Hello World App

This is a simple Flask application that demonstrates the basic structure of a web application and includes an endpoint that takes an integer value and returns a JSON response with the value "high" or "low" depending on whether the integer is greater than 100.

## Getting Started

To run this application on your local machine, you will need to have Python 3 and Flask installed.

1. Clone this repository to your local machine using the following command:

```
git clone https://github.com/your-username/flask-hello-world.git
```

2. Navigate to the project directory:

```
cd flask-hello-world
```

3. Install the required dependencies using pip3:

```
pip3 install -r requirements.txt
```

4. Start the Flask development server:

```
python3 app.py
```

5. Open a web browser and navigate to http://localhost:5000/ to see the "Hello World" message, or send a POST request to http://localhost:5000/check_number with a payload containing an integer value to test the /check_number endpoint.
