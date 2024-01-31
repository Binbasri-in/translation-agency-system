from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

# Change this to your secret key (can be anything, it's for extra protection)
app.secret_key = 'your secret key'


# prompt request: 
def make_translation_request(prompt):
    url = 'https://api.cloudflare.com/client/v4/accounts/4da66dac8f0c0483794586300c5ccc66/ai/run/@cf/meta/llama-2-7b-chat-int8'
    headers = {
        'Authorization': 'Bearer JQZD7dYHmbLp5kTVt4NglPvmh-C4mrwyLu7Q1Kp-',
        'Content-Type': 'application/json'
    }
    data = {
        'prompt': prompt
    }

    response = requests.post(url, headers=headers, json=data)
    return response.json()

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/translate', methods=['GET', 'POST'])
def translate_request():
    if request.method == 'POST':
        data = request.get_json()
        if 'text' in data:
            text = data['text']
            response = make_translation_request(text)
            print(response)
            return jsonify({'text': response})
        