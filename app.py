from flask import Flask, render_template, request, jsonify
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_location_info', methods=['POST'])
def get_location_info():
    data = request.get_json()
    location = data['location']
    # Call the Python script to generate HTML content
    html_content = subprocess.check_output(['python', 'generate_html.py', location], text=True)
    return html_content

if __name__ == '__main__':
    app.run(debug=True)