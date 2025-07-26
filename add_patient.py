from flask import Flask, render_template, request, redirect
import uuid

app = Flask(__name__)

patients = []  # Temporary store

@app.route('/add_patient', methods=['GET', 'POST'])
def add_patient():
    if request.method == 'POST':
        new_patient = {
            'reg_number': str(uuid.uuid4())[:8],  # auto-gen short ID
            'full_name': request.form['full_name'],
            'age': request.form['age'],
            'sex': request.form['sex'],
            'address': request.form['address'],
            'religion': request.form['religion'],
            'phone': request.form['phone'],
            'visits': []
        }
        patients.append(new_patient)
        return redirect('/dashboard')  # Redirect after save
    return render_template('add_patient.html')

