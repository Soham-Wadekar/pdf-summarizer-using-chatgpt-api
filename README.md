# PDF Summarizer using ChatGPT API

This application is made with the use of ChatGPT's API and it tests the capabilities of ChatGPT.
The model takes a PDF as an input and outputs its summary by feeding the PDF to ChatGPT in chunks.
*Note that this applications has limitations of license and free OpenAI license can only summarize PDFs of small sizes.*

To run the Flask application, adhere to the following instructions:
1. Go to the project directory using command line interface
2. Create a virtual environment using the command: python -m venv env
3. Activate the environment using the following command: source env/bin/activate
4. Install the libraries `flask`, `openai` and `PyPDF2` using the command: `pip install flask openai PyPDF2`
5. Run the application using the command: python app.py
6. Go to `http://127.0.0.1:5000/` to view the application
