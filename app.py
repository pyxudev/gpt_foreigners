from flask import Flask, request, render_template


app = Flask(__name__)

@app.route('/index')
def index():
    return render_template('home.html')

@app.route("/gpt", methods=['POST'])

def gpt():
    data = request.get_json()
    prompt = json.loads(data)["prompt"]

   return prompt
