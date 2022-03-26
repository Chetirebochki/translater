from unittest import TestCase, main
from app import generate, predict
import torch
from transformers import T5ForConditionalGeneration, T5Tokenizer

model_name = "cointegrated/rut5-base-multitask"
tokenizer = T5Tokenizer.from_pretrained(model_name)
model = T5ForConditionalGeneration.from_pretrained(model_name)
ruen = 'translate ru-en'
enru = 'translate en-ru'
sep = ' | '



class UnitTests(TestCase):
    def test_ruen_translation(self):
        self.assertEqual(generate(ruen + sep + 'Привет'), 'Hello')

    def test_enru_translation(self):
        self.assertEqual(generate(enru + sep + 'Hello'), 'Привет')

    def test_lang(self):
        self.assertTrue(predict, 'Привет')


if __name__ == '__main__':
    main()
