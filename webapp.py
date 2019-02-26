from flask import Flask, render_template, request
import json
import watson_requests

app = Flask(__name__)

with open("apikey.txt", "r") as f:
    api_key = f.read().strip()
nlu = watson_requests.make_nlu(api_key)
#url = "https://www.nytimes.com/2019/02/25/movies/oscars-moments-best-worst.html"

def make_html(json):
    elems = []
    for key in json.keys():
        if key == "keywords":
            for keyword in json[key]:
                elems.append("%s, relevance %.2f" % (keyword["text"], keyword["relevance"]))
    return elems

@app.route("/", methods=["GET"])
def main_page():
    return render_template("index.html")

@app.route("/", methods=["POST"])
def main_post():
    url = request.form["url"]
    json_result = watson_requests.analyze(nlu, url)
    s = make_html(json_result)
    return render_template("index.html", content=s)


