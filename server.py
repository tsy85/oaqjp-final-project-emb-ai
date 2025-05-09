"""
server.py
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/")
def render_index_page():
    """
    render_index_page
    """
    return render_template('index.html')

@app.route("/emotionDetector")
def sent_emotion():
    """
    sent_emotion
    """
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)

    if request['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant = response['dominant_emotion']

    result = f"For the given statement, the system response is 'anger': {anger}, "
    result += f"'disgust': {disgust}, 'fear': {fear}, 'joy': {joy} and 'sadness': {sadness}. "
    result += f"The dominant emotion is {dominant}."

    return result

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
