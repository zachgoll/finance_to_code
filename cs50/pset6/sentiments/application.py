from flask import Flask, redirect, render_template, request, url_for

import helpers
import os
import sys
from analyzer import Analyzer

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/search")
def search():

    # validate screen_name
    screen_name = request.args.get("screen_name", "").lstrip("@")
    if not screen_name:
        return redirect(url_for("index"))

    # get screen_name's tweets
    userTweets = helpers.get_user_timeline(screen_name)
    if userTweets == None:
        return redirect(url_for("index"))
    
    positive, negative, neutral = 0.0, 0.0, 0.0
    
    # absolute paths to lists
    positives = os.path.join(sys.path[0], "positive-words.txt")
    negatives = os.path.join(sys.path[0], "negative-words.txt")

    # instantiate analyzer
    analyzer = Analyzer(positives, negatives)
    # iterate through the first 50 of the user's tweets
    
    # determine how many tweets the user has
    numTweets = len(userTweets)
    if numTweets > 100:
        numTweets = 100
        
    for i in range(numTweets):
        # analyze tweet
        score = analyzer.analyze(userTweets[i])
        if score > 0.0:
            positive = positive + 1.0
        elif score < 0.0:
            negative = negative + 1.0
        else:
            neutral = neutral + 1.0

    # generate chart
    chart = helpers.chart(positive, negative, neutral)

    # render results
    return render_template("search.html", chart=chart, screen_name=screen_name)
