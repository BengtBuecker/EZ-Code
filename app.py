from flask import Flask,request, render_template
import json
from llamaapi import LlamaAPI
import os

template_dir = os.path.abspath('./templates')
app = Flask(__name__, template_folder=template_dir)

@app.route('/')
def index():
    return render_template('home.html')
@app.route('/uebersetzer')
def uebersetzer():
    return render_template('uebersetzer.html')
@app.route('/home')
def home():
    return render_template('home.html')
@app.route('/index')
def Index():
    return render_template('index')
@app.route('/lexikonHtml')
def lexikonHtml():
    return render_template('lexikon-html.html')
@app.route('/lexikonJs')
def lexikonJs():
    return render_template('lexikon-js.html')
@app.route('/lexikonCss')
def lexikonCss():
    return render_template('lexikon-css.html')
@app.route('/challenges')
def challenges():
    return render_template('challenges.html')
@app.route('/process_input', methods=['POST'])
def process_input():
  user_input =request.form['user_input']
  # Initialize llamaapi with token
  llama = LlamaAPI("LL-KepCmrkxMQRPLovpgntuSh5VtrLxxl7TNeWwKmhWkhjaNxGimErM9xuWfGKGDX1M")
  # API request
  api_request_json = {
  "model": "llama-13b-chat",
  "messages": [
    {"role": "system", "content": "You are an AI assistant explaining code to help students on every level understand every component of it"},
    {"role": "user", "content":"Explain this code:"+ user_input+"in an understandable way, taking a look at every component of it. Don't greet the user and don't ask any follow-up questions. Start directly with explainig the code."},
  ]
  } 
  r = llama.run(api_request_json)
  r2=json.dumps(r.json())
  r3=r2[r2.find("content")+11:r2.find("function_call")-1].strip().replace('\\n',' ').replace('\\',' ')
  
  return render_template('uebersetzer.html', output=r3)
if __name__ == '__main__':
    app.run(debug=True)