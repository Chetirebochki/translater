from flask import Flask, render_template, request
import torch
from transformers import T5ForConditionalGeneration, T5Tokenizer

'''
model_name = "cointegrated/rut5-base-multitask"
tokenizer = T5Tokenizer.from_pretrained(model_name)
model = T5ForConditionalGeneration.from_pretrained(model_name)


def generate(text, **kwargs):
    inputs = tokenizer(text, return_tensors='pt')
    with torch.no_grad():
        hypotheses = model.generate(**inputs, num_beams=5, **kwargs)
    return tokenizer.decode(hypotheses[0], skip_special_tokens=True)


ruen = 'translate ru-en'
enru = 'translate en-ru'
sep = ' | '
'''

text = 'hello, my dear friend'
from transformers import FSMTForConditionalGeneration, FSMTTokenizer

mname1 = "facebook/wmt19-ru-en"
mname2 = "facebook/wmt19-en-ru"
tokenizer1 = FSMTTokenizer.from_pretrained(mname1)
tokenizer2 = FSMTTokenizer.from_pretrained(mname2)
model1 = FSMTForConditionalGeneration.from_pretrained(mname1)
model2 = FSMTForConditionalGeneration.from_pretrained(mname2)


def generateruen(text):
    input_ids = tokenizer1.encode(text, return_tensors="pt")
    outputs = model1.generate(input_ids)
    decoded = tokenizer1.decode(outputs[0], skip_special_tokens=True)
    return decoded


def generateenru(text):
    input_ids = tokenizer2.encode(text, return_tensors="pt")
    outputs = model2.generate(input_ids)
    decoded = tokenizer2.decode(outputs[0], skip_special_tokens=True)
    return decoded


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    message = request.form['message']
    lang = request.form['select']
    if lang == 'Russian':
        trans = generateenru(message)
    elif lang == 'English':
        trans = generateruen(message)

    print('Я перевел')
    return render_template('index.html', prediction=trans, text_pred=message)


if __name__ == '__main__':
    app.run(debug=True)
