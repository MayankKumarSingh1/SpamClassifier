import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
import pickle
import string
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
ps=PorterStemmer()
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('stopwords')

def transform_text(text):
  text=text.lower()
  text=nltk.word_tokenize(text)

  y=[]

  for i in text:
    if i.isalnum():
      y.append(i)

  text=y[:]
  y.clear()

  for i in text:
    if i not in stopwords.words('english') and i not in string.punctuation:
      y.append(i)

  text=y[:]
  y.clear()

  for i in text:
    y.append(ps.stem(i))

  return " ".join(y)

tfidf= pickle.load(open(r'vectorizer.pkl','rb'))
model=pickle.load(open(r'model.pkl','rb'))

st.title('SMS spam classification')
input_sms= st.text_input("Enter the message")
if st.button('Predict'):

    transformed_sms= transform_text(input_sms)

    vector_input= tfidf.transform([transformed_sms])

    result=model.predict(vector_input)[0]

    if(result ==1):
        st.header("Spam")
    else:
        st.header("Not Spam")
