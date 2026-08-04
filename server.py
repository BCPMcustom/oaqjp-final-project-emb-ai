"""
Server module for the Sentiment Analysis application.
Provides endpoints for web rendering and emotion analysis.
"""

from flask import Flask, render_template, request
from SentimentAnalysis.sentiment_analysis import sentiment_analyzer

app = Flask("sentimentAnalyzer")

@app.route("/emotionDetector")
def sent_analyzer():
    """
    Analyzes the input text and returns the detected sentiment label and score.
    """
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Pass the text to the sentiment_analyzer function and store the response
    response = sentiment_analyzer(text_to_analyze)

    # Extract the label and score from the response
    label = response['label']
    score = response['score']

    # Return a formatted string with the sentiment label and score

    if label is None:
        return "Invalid Input!  Try Again."

    return f"The given text has been identified as {label.split('_')[1]} with a score of {score}."


@app.route("/")
def render_index_page():
    """
    Renders the main HTML index page for the user interface.
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
