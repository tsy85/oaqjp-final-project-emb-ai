import requests
import json
def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = { "raw_document": { "text": text_to_analyse } }
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    response = requests.post(url, json = myobj, headers=header)
    if (response.status_code == 400):
        anger_score, disgust_score, fear_score, joy_score, sadness_score, dominant_emotion = (None, None, None, None, None, None)
    else:
        formatted_response = json.loads(response.text)
        anger_score = formatted_response['emotionPredictions'][0]['emotion']['anger']
        disgust_score = formatted_response['emotionPredictions'][0]['emotion']['disgust']
        fear_score = formatted_response['emotionPredictions'][0]['emotion']['fear']
        joy_score = formatted_response['emotionPredictions'][0]['emotion']['joy']
        sadness_score = formatted_response['emotionPredictions'][0]['emotion']['sadness']
        dominant_emotion = "anger"
        dominant_score = anger_score
        if dominant_score < disgust_score:
            dominant_emotion = "disgust"
            dominant_score = disgust_score
        if dominant_score < fear_score:
            dominant_emotion = "fear"
            dominant_score = fear_score
        if dominant_score < joy_score:
            dominant_emotion = "joy"
            dominant_score = joy_score
        if dominant_score < sadness_score:
            dominant_emotion = "sadness"
            dominant_score = sadness_score

    return {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant_emotion
    }