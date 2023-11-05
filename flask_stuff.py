from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# This is a placeholder for the Patient class.
# You would replace this with the actual class code that you provide later.
class Patient:
    def __init__(self, name, age, symptoms):
        self.name = name
        self.age = age
        self.symptoms = symptoms
        # You can add more attributes here based on the actual Patient class definition.

patients = []

@app.route('/receive_data', methods=['POST'])
def receive_data():
    data = request.json
    try:
        # Create a Patient object with the incoming data
        patient = Patient(
            name=data.get('name'),
            age=data.get('age'),
            symptoms={
                'name': data.get('symptom_name'),
                'severity': data.get('severity'),
                'time': data.get('time')
            }
        )
        # Store the patient object in a list (you might want to use a database in production)
        patients.append(patient)
        # Acknowledge the receipt of patient data
        return jsonify({'message': 'Patient data received successfully.'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/patients', methods=['GET'])
def get_patients():
    try:
        # Assuming there is a method to serialize Patient objects to a dictionary
        # This is just a placeholder to show the structure
        patients_data = [{'name': patient.name, 'age': patient.age, 'symptoms': patient.symptoms} for patient in patients]
        return jsonify(patients_data), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
