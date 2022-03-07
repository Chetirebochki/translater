from flask import Flask, render_template, request
import torch
from transformers import T5ForConditionalGeneration, T5Tokenizer

model_name = "cointegrated/rut5-base-multitask"
tokenizer = T5Tokenizer.from_pretrained(model_name)
model = T5ForConditionalGeneration.from_pretrained(model_name)


from transformers import FSMTForConditionalGeneration, FSMTTokenizer

mname = "facebook/wmt19-ru-en"
tokenizer = FSMTTokenizer.from_pretrained(mname)
model = FSMTForConditionalGeneration.from_pretrained(mname)

def generate(text):
    input_ids = tokenizer.encode(text, return_tensors="pt")
    outputs = model.generate(input_ids)
    decoded = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return decoded

app = Flask(__name__)
string = str
if value == eng:
    string = enru
elif value == ru:
    string = ruen


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    message = request.form['message']
    trans = generate(message)
    return render_template('index.html', prediction=trans)


@app.route('/predict_delete', methods=['POST'])
def predict_delete():
    return render_template('index.html', prediction="")


if __name__ == '__main__':
    app.run(debug=True)
