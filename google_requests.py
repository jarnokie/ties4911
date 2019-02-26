from google.cloud import language
from google.cloud.language import enums, types

import requests

def create_client():
    return language.LanguageServiceClient()

def get_entities(client, url):
    #html = requests.get("https://www.jyu.fi/en/current/archive/2019/02/pekka-neittaanmaki-appointed-as-unesco-chair").text
    html = requests.get(url).text
    document = types.Document(content=html, type=enums.Document.Type.HTML)
    return client.analyze_entities(document=document).entities

