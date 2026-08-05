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


    # If the response status code is 200, extract the label and score from the response
    if response.status_code == 200:
        emotions_list = ['anger', 'disgust', 'fear', 'joy', 'sadness']
        # Parse the response from the API
        formatted_response = json.loads(response.text)
        feels = formatted_response["emotionPredictions"][0]["emotion"]
        extracted_emotions = {emo: feels[emo] for emo in emotions_list}
        dominant_emotion = max(extracted_emotions, key=extracted_emotions.get)
        # Add the dominant emotion straight into your dictionary
        extracted_emotions['dominant_emotion'] = dominant_emotion
        
        return extracted_emotions
        
    # If the response status code is 500, set label and score to None
    #elif response.status_code == 500:
        #label = None
        #score = None
    # For any other unexpected status codes, set label and score to None
    else:
        # Return blank fields so the frontend doesn't crash on failure
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None
        }

    # Return the label and score in a dictionary
    return dominant_emotion