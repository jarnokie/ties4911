from flask import Flask, render_template, request
import configparser
import json
import watson_requests
import google_requests
import configparser
import azure_requests

app = Flask(__name__)

config = configparser.ConfigParser()
config.read('apikey.txt')
watson_api_key = config.get('APIKEYS', 'WATSON')
azure_api_key = config.get('APIKEYS', 'AZURE')

nlu = watson_requests.make_nlu(watson_api_key)

google_client = google_requests.create_client()

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

def get_keywords_google(entities):
    keywords = []
    for i in range(min(50,len(entities))):
        e = entities[i]
        keywords.append((e.name, e.salience))
    return keywords

def get_keywords_azure(json):
    keywords = []
    if "documents" in json and len(json["documents"]) > 0 and "keyPhrases" in json["documents"][0]:
        keywords = json["documents"][0]["keyPhrases"]
    return [[k, i] for i, k in enumerate(keywords)]

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

    e = google_requests.get_entities(google_client, url)
    g = get_keywords_google(e)
    
    azure_response = azure_requests.analyze(url, azure_api_key)
    azure_keywords = get_keywords_azure(azure_response)

    # render page
    return render_template("index.html", watson_keywords=s, google_keywords=g, \
                           azure_keywords=azure_keywords, url=url)

