from flask import Flask, render_template, request

import google.generativeai as genai
#install nyo to sa terminal: pip install -q -U google-genai
#pip install google-generativeai

genai.configure(api_key="AIzaSyBmgrPyn0Wc1bPn9iTWs-HetfK9Dti9-9s") 
model = genai.GenerativeModel('gemini-2.0-flash')

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('chat.html')

@app.route("/get", methods=["GET", "POST"])
def chat():
    msg = request.form['msg']
    input_text = msg
    return get_Chat_response(input_text)

def get_Chat_response(text):
    """Generates a response using the Gemini Pro model."""
    try:
        response = model.generate_content(text)
        return response.text
    except Exception as e:
        return f"Error: {e}"

if __name__ == '__main__':
    app.run(debug=True)