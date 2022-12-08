import requests, json
from flask import Flask, render_template

app = Flask(__name__)

def get_meme():
    url = 'https://meme-api.com/gimme'
    response = json.loads(requests.request('GET', url).text)
    img = response['url']
    return img

@app.route('/')
def index():
    meme = get_meme()
    return render_template('index.html', meme=meme)

app.run(port=8080)