from flask import Flask, render_template
import json
import watson_requests

app = Flask(__name__)

with open("apikey.txt", "r") as f:
    api_key = f.read().strip()
nlu = watson_requests.make_nlu(api_key)
url = "https://www.nytimes.com/2019/02/25/movies/oscars-moments-best-worst.html"

@app.route("/")
def main_page():
    json_result = watson_requests.analyze(nlu, url)
    c = json.dumps(json_result)
    return render_template("mainpage.html", content=c)
