from bs4 import BeautifulSoup
import requests

# Strips tags from HTML, returning regular text.
def strip_tags(html):
    soup = BeautifulSoup(html, features="html.parser")
    # Select only p-tags
    text = " ".join([p.text for p in soup.select('p')])
    return text

def read_url(url):
    response = requests.get(url)
    return strip_tags(response.content)

def analyze(url, api_key):
    content = read_url(url)
    # Maximum length of document is 5000 characters
    # https://docs.microsoft.com/bs-latn-ba/azure/cognitive-services/text-analytics/how-tos/text-analytics-how-to-keyword-extraction
    content = content[0:5000]
    headers = {
        # Request headers
        'Ocp-Apim-Subscription-Key': api_key
    }
    documents = { 'documents': [
        { 'id': '1', 'language': 'en', 'text': content },
    ]}
    text_analytics_base_url = "https://northeurope.api.cognitive.microsoft.com/text/analytics/v2.0/"
    key_phrase_api_url = text_analytics_base_url + "keyPhrases"
    response  = requests.post(key_phrase_api_url, headers=headers, json=documents, timeout=30)
    return response.json()
