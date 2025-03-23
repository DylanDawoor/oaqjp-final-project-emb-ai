"""
This module contains the Flask application to analyze emotions from a given text input.
It uses the EmotionDetection package to perform sentiment analysis and return the dominant emotion.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

# Initiate the flask app
app = Flask(__name__)

@app.route('/emotionDetector', methods=['GET'])
def sent_analyzer():
    """
    This function handles the GET request for analyzing emotions from a text input.
    It returns a formatted string with emotion scores or an error message if input is invalid.
    """
    text_to_analyze = request.args.get('textToAnalyze', '')

    # Empty input handler
    if not text_to_analyze.strip():  # If text is empty
        return "Invalid text! Please try again!", 400

    # Call emotion detector function emotion_detector
    response = emotion_detector(text_to_analyze)

    # When dominant emotion is None
    if not response.get('dominant_emotion'):
        return "Invalid text! Please try again!", 400

    # Formatting the response
    formatted_response = (
        f"For the given statement, the system response is "
        f"'anger': {response['anger']}, "
        f"'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, "
        f"'joy': {response['joy']}, "
        f"and 'sadness': {response['sadness']}. "
        f"The dominant emotion is {response['dominant_emotion']}."
    )
    return formatted_response

@app.route("/")
def render_index_page():
    """
    This function initiates the rendering of the main application
    page over the Flask channel.
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
