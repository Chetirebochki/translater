from flask import Flask, render_template, request
import torch
from transformers import T5ForConditionalGeneration, T5Tokenizer

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
# text='hello, my dear friend'
# from transformers import FSMTForConditionalGeneration, FSMTTokenizer
#
# mname = "facebook/wmt19-ru-en"
# tokenizer = FSMTTokenizer.from_pretrained(mname)
# model = FSMTForConditionalGeneration.from_pretrained(mname)
#
# def generate(text):
#     input_ids = tokenizer.encode(text, return_tensors="pt")
#     outputs = model.generate(input_ids)
#     decoded = tokenizer.decode(outputs[0], skip_special_tokens=True)
#     return decoded

app = Flask(__name__)




@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    lang = request.form['select']
    if lang == 'Russian':
       string = enru
    elif lang == 'English':
       string = ruen
    message = request.form['message']
    trans = generate(string + sep + message)
    return render_template('index.html', prediction=trans, text_pred=message)

if __name__ == '__main__':
    app.run(debug=True)
