import requests
from pprint import pprint

subscription_key = "<##Check with Sambit for key and secret##>"
text_analytics_base_url = "<##Check with Sambit for key and secret##>"


sentiment_url = text_analytics_base_url + "sentiment"

documents = {"documents": [
    {"id": "Statement 1", "language": "en",
        "text": "I had a wonderful experience yesterday! The MPF workshop was helpful."},
    {"id": "Statement 2", "language": "en",
        "text": "I had a terrible time yesterday. The döner at Bërlin was awful."},
    {"id": "Statement 3", "language": "es",
     "text": "La carretera estaba atascada. Había mucho tráfico el día de ayer."},
    {"id": "Statement 4", "language": "de",
     "text": "Leider verstehe ich kein deutsch."}
]}

headers = {"Ocp-Apim-Subscription-Key": subscription_key}
response = requests.post(sentiment_url, headers=headers, json=documents)
sentiments = response.json()
pprint(documents)
pprint(sentiments)






############ END

############ Determine Language

#language_api_url = text_analytics_base_url + "languages"
#pprint(language_api_url)
#documents = {"documents": [
#    {"id": "1", "text": "This is a document written in English."},
#    {"id": "2", "text": "Este es un document escrito en Español."},
#    {"id": "3", "text": "这是一个用中文写的文件"}
#]}

#headers = {"Ocp-Apim-Subscription-Key": subscription_key}
#response = requests.post(language_api_url, headers=headers, json=documents)
#languages = response.json()
#pprint(languages)
