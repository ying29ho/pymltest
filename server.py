from classifier import SizeClassifier
from flask import Flask
from flask import render_template, request
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/survey-results')
def survey_query():
    chest_response = float(request.args.get('chest'))
    shoulder_response = float(request.args.get('sleeve'))
    pred = model.predict([chest_response, shoulder_response])
    return render_template('results.html', prediction=pred, chest=chest_response, shoulder=shoulder_response)


if __name__ == '__main__':
    model = SizeClassifier()
    model.train('data.csv')
    app.run(host='0.0.0.0')
