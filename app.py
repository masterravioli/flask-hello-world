# Import dependencies
from flask import Flask, jsonify, request

# Import flask class from module
app = Flask(__name__)

# Define route for the root URL
@app.route("/")
def hello():
    return "Hello World"

# Define route /check_number
@app.route("/check_number", methods=["POST"])
def check_number():
    # Get the JSON payload data
    data = request.get_json()
    # Get the value of the field 'integer'
    number = data.get("integer")
    if number is None:
        return jsonify({"error": "Missing integer parameter"}), 400
    try:
        number = int(number)
    except ValueError:
        return jsonify({"error": "Invalid integer value"}), 400
    if number > 100:
        result = "high"
    else:
        result = "low"
    # Return the result in JSON format
    return jsonify({"integer": result})

# Run script if the current module is '__main__'
if __name__ == "__main__":
    app.run(debug=True)
