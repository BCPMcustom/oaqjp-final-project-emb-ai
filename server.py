"""
Server module for the Sentiment Analysis application.
Provides endpoints for web rendering and emotion analysis.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("emotionDetector")

@app.route("/emotionDetector")
def sent_analyzer():
    """
    Analyzes the input text and returns the detected sentiment label and score.
    """
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Pass the text to the sentiment_analyzer function and store the response
    response = emotion_detector(text_to_analyze)

    #Transform the dictionary into a printable list of pairs
    # Create a list of string pairs, excluding the dominant emotion key
    pairs = [f"'{key}': {val}" for key, val in response.items() if key != 'dominant_emotion']

    # Glue them together with a comma and space
    clean_scores = ", ".join(pairs)
        
    #Return a formatted string with the response
    output_text = f"For the given statement, the system response is {clean_scores}. The dominant emotion is <strong>{response['dominant_emotion']}</strong>."
    return output_text


@app.route("/")
def render_index_page():
    """
    Renders the main HTML index page for the user interface.
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
