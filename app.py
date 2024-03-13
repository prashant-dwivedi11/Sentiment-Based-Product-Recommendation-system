from flask import Flask, request, render_template
from model import ProdRecommender

app = Flask(__name__)

sentiment_recommendation_model = ProdRecommender()


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    # Get the username as input
    user_name_input = request.form['username'].lower()
    sentiment_recommendation_output = sentiment_recommendation_model.top5_recommendations(user_name_input)

    if not (sentiment_recommendation_output is None):
        return render_template("index.html", output=sentiment_recommendation_output)
    else:
        return render_template("index.html",
                               message_display="This User Name doesn't exist. Please provide a valid user name!")


if __name__ == '__main__':
    app.run()
