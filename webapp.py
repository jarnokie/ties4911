from flask import Flask, render_template, request
import json
import watson_requests

app = Flask(__name__)

with open("apikey.txt", "r") as f:
    api_key = f.read().strip()
nlu = watson_requests.make_nlu(api_key)
#url = "https://www.nytimes.com/2019/02/25/movies/oscars-moments-best-worst.html"

def get_keywords_watson(json):
    """
    Return list of (keywords, relevance from watson json result
    """
    keywords = []
    for key in json.keys():
        if key == "keywords":
            for keyword in json[key]:
                keywords.append((keyword["text"], keyword["relevance"]))
    return keywords

@app.route("/", methods=["GET"])
def main_page():
    return render_template("index.html")

@app.route("/", methods=["POST"])
def main_post():
    # get url from post form
    url = request.form["url"]
    # Analyze url with watson
    json_result = watson_requests.analyze(nlu, url)
    # get keyword array from json
    s = get_keywords_watson(json_result)
    # render page
    return render_template("index.html", watson_keywords=s, url=url)


