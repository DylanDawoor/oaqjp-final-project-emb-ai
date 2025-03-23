import requests
import json

def emotion_detector(text_to_analyse):
    # URL of the emotion detector service
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

    # Constructing the request payload in the expected format
    myobj = { "raw_document": { "text": text_to_analyse } }

    # Custom header specifying the model ID for the sentiment analysis service
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    # Sending a POST request to the sentiment analysis API
    response = requests.post(url, json=myobj, headers=headers)

    # Parsing the JSON response from the API
    formatted_response = json.loads(response.text)

    # Extracting emotions score from the response
    emotions = formatted_response['emotionPredictions'][0]['emotion']
    
    # Extracting emotions dominant emotion from the response
    dominant_emotion = max(emotions, key=emotions.get)

    #formatting the results
    result = {
    'anger': emotions.get('anger', 0),
    'disgust': emotions.get('disgust', 0),
    'fear': emotions.get('fear', 0),
    'joy': emotions.get('joy', 0),
    'sadness': emotions.get('sadness', 0),
    'dominant_emotion': dominant_emotion
    }

    # Returning the result
    return result

