from db import returnElementsFromCL
from db import returnElements
from sklearn.feature_extraction.text import TfidfVectorizer
from keras.preprocessing.sequence import pad_sequences
from keras.preprocessing.text import Tokenizer  
import spacy

#X=returnElementsFromCL(17502679)
X=returnElements("")
numWords=5000
tokenizer = Tokenizer(num_words=numWords)
tokenizer.fit_on_texts(X)
maxlen=300
counter=[0 for _ in range(numWords)]
for X_train in X[:2]:
    X_train = tokenizer.texts_to_sequences([X_train])
    X_train = pad_sequences(X_train, padding='post', maxlen=maxlen)
    print(X_train[0])
    for word in X_train[0]:
        counter[word]+=1
    

