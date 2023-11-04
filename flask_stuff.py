from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_cors import cross_origin
import sys


app = Flask(__name__)
CORS(app, origins="http://localhost:3000")


# Create a route to handle POST requests for processing data
@app.route("/process_data", methods=["POST"])
@cross_origin(supports_credentials=True)
def process_data():
    try:
        # Get the 'code' value from the JSON data sent by the frontend
        data = request.json
        name = data.get("name")
        age = data.get("name")
        # Check for additional keys to determine the action

        # Call the main function and return its result
        result = main(code)
        return jsonify(result)

    except Exception as e:
        return jsonify({"error": str(e)})