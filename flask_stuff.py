# flask_stuff.py

from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin

# Import the placeholder functions from processing.py
import processing as p

app = Flask(__name__)
CORS(app, origins="http://localhost:3000")

@app.route("/process_data", methods=["POST"])
@cross_origin(supports_credentials=True)
def process_data():
    try:
        # Get the data from the JSON sent by the frontend
        data = request.json
        name = data.get("name")
        age = data.get("age")

        # Use imported functions to process the data
        processed_name = p.process_name(name)
        processed_age = p.process_age(age)

        # Prepare the result with the processed data
        result = {
            "processed_name": processed_name,
            "processed_age": processed_age,
        }

        # Return the result as JSON
        return jsonify(result)

    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(debug=True)
