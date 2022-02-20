from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    message = request.form['message']
    text = message.lower()
    return render_template('index.html', prediction=text)


@app.route('/predict_delete', methods=['POST'])
def predict_delete():
    return render_template('index.html', prediction="")


if __name__ == '__main__':
    app.run(debug=True)
