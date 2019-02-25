from watson_developer_cloud import NaturalLanguageUnderstandingV1
from watson_developer_cloud.natural_language_understanding_v1 import Features, CategoriesOptions, EntitiesOptions

def make_nlu(api_key, url="https://gateway-lon.watsonplatform.net/natural-language-understanding/api/v1/analyze?version=2018-11-16"):
    return NaturalLanguageUnderstandingV1(version="2018-11-16", iam_apikey=api_key, url=url)

def analyze(nlu, url):
    return nlu.analyze(url=url, features=Features(entities=EntitiesOptions())).get_result()


