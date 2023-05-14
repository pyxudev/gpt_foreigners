from flask import Flask, request, render_template
import openai
import json
import os
import io,sys


app = Flask(__name__)

@app.route('/index')
def index():
    return render_template('home.html')

@app.route("/gpt/<prompt>", methods=['GET'])
def gpt(prompt):
    openai.organization = "org-7R2GbHNVDVqpskX1wNWALtl4"
    openai.api_key = os.getenv("OPENAI_API_KEY")

    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": f"""You are a professional supporter for foreigners who have just arrived in Japan.
I would like to go to {prompt} in Japan.
1.Please list what I need to prepare.
2.Who should I ask if I have any questions?
3.If I can choose more than one facility, which one is the most accessible to foreigners?
4.What are the advantages de/merits of each facility, respectively?
5.Please also include a GoogleMap url where we can see the route to the nearest facility
6.Please answer step by step."""}
       ])
    res = json.loads(str(completion.choices[0].message))["content"]
    print(res)
    return res

app.run(host="0.0.0.0", port=8000)
