#pip install transformers
#pip install torch torchvision torchaudio
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

ruen='translate ru-en'
enru='translate en-ru'
sep=' | '
text=get_text()
if vybor.get_value()=='en-ru':
 print(generate(
    enru+sep+text))
if vybor.get_value()=='ru-en':
 print(generate(
    ruen+sep+text))
