'''
This module connects the server to the IBM API
'''
import json
import requests


def emotion_detector(text_to_analyse):
    '''
    This function connects to the API and check the connection status
    '''
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    myobj = { "raw_document": { "text": text_to_analyse } }
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    response = requests.post(url, json = myobj, headers=header, timeout=10)


    # Parse the response from the API
    formatted_response = json.loads(response.text)

    return formatted_response
