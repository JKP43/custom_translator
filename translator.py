import requests, uuid, json

# Add your key and endpoint
key = 'TRANSLATOR_API_KEY'
endpoint = "https://api.cognitive.microsofttranslator.com"

# location, also known as region.
# required if you're using a multi-service or regional (not global) resource. It can be found in the Azure portal on the Keys and Endpoint page.
location = 'TRANSLATOR_API_KEY'

path = '/translate'
constructed_url = endpoint + path


def translate_text(text, from_language, to_language):
    headers = {
        'Ocp-Apim-Subscription-Key': key,
        'Ocp-Apim-Subscription-Region': location,
        'Content-Type': 'application/json'
    }
    params = {
        'api-version': '3.0',
        'from': from_language,
        'to' : to_language
    }
    body = [{
        'text': text
    }]
    response = requests.post(constructed_url, params=params, headers=headers, json=body)
    response.raise_for_status()
    translation = response.json()

    translated_text = translation[0]["translations"][0]["text"]
    return translated_text