import tensorflow as tf
import json
from transformers import DistilBertTokenizerFast, TFDistilBertForSequenceClassification


tokenizer = DistilBertTokenizerFast.from_pretrained('C:\\Users\\ACER\\Project\\Sentiment Analysis\\Save_Model')
model = TFDistilBertForSequenceClassification.from_pretrained('C:\\Users\\ACER\\Project\\Sentiment Analysis\\Save_Model')


def get(text):
    pred = tokenizer.encode(text, truncation=True, padding=True, return_tensors="tf")
    output = model(pred)[0]
    pred = tf.argmax(output, axis=1).numpy()[0]
    return pred


