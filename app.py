from flask import Flask, render_template, request, redirect, url_for
import subprocess

app = Flask(__name__)

# Route for the home page
@app.route('/')
def index():
    return render_template('index.html')

# Route for the form page
@app.route('/form')
def form():
    return render_template('form.html')

# Route for the calendar page
@app.route('/calendar')
def calendar():
    return render_template('calendar.html')

# Route to handle form submission and execute script
@app.route('/handle_submission', methods=['POST'])
def handle_submission():
    phone_number = request.form.get('phone')

    if not phone_number:
        return "Error: Phone number is required."

    try:
        # Execute the external Python script with the phone number as an argument
        result = subprocess.run(
            ['python', 'script.py', phone_number],
            capture_output=True,
            text=True
        )
        if result.stderr:
            return f"Error: {result.stderr}"
        return f"Success: {result.stdout}"
    except Exception as e:
        return f"An error occurred: {str(e)}"

# Route to execute a script and return its output
@app.route('/run_script', methods=['POST'])
def run_script():
    try:
        # Get the phone number from the form
        phone_number = request.form['phone']

        # Validate the phone number format
        if not phone_number.startswith('+'):
            return "Error: Phone number must include the country code (e.g., +91)."

        # Execute the script with the phone number as an argument
        result = subprocess.run(['python', 'script.py', phone_number], capture_output=True, text=True)
        output = result.stdout
        error = result.stderr

        if error:
            return f"Error executing script: {error}"
        else:
            return f"Script executed successfully.<br>Output: <pre>{output}</pre>"
    except Exception as e:
        return f"An error occurred: {str(e)}"

# Route for the success page
@app.route('/success')
def success():
    return render_template('success.html')

if __name__ == '__main__':
    app.run(debug=True)
