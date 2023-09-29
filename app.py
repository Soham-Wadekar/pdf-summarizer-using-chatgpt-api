# Importing necessary libraries
from flask import Flask, render_template, request, redirect, url_for
import os
from PyPDF2 import PdfReader
import re
import openai

# Enter your OpenAI key

openai.api_key = '<Your OpenAI key>'

# Initializing Flask application

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'pdf'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Some utility functions

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.',1)[1].lower() in ALLOWED_EXTENSIONS

def preprocess_input(text):
    text = text.replace('\n','')
    text = re.sub(r'[0-9]\.','',text)

    return text

def summarize(pdf,model='gpt-3.5-turbo'):
    responses = []

    reader = PdfReader(pdf)

    for page in reader.pages[:2]:
        text = page.extract_text()
        text = preprocess_input(text)

        messages = [{"role": "user", "content": f'Summarize the following: {text}'}]

        response = openai.ChatCompletion.create(
            model = model,
            messages = messages,
            temperature = 0
        )

    response = response.choices[0].message["content"]
    responses.append(response)

    final_summary_messages = [{"role": "user", "content": f"Summarize the list in 50 words: {responses}"}]

    final_summary_response = openai.ChatCompletion.create(
        model = model,
        messages = final_summary_messages,
        temperature = 0
    )

    final_summary = final_summary_response.choices[0].message["content"]

    return final_summary

# Creating routes for multiple pages

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return redirect(request.url)

    file = request.files['file']

    if file.filename == '':
        return redirect(request.url)

    if file and allowed_file(file.filename):
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(file_path)
        summarization_result = summarize(file_path)
        return render_template('result.html', summarization_result=summarization_result)

    return render_template('index.html', error='Invalid file format')

# Main

if __name__ == '__main__':
    app.run(debug=True)

# Author: Soham Wadekar

