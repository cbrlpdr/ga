import numpy as np
from sklearn.decomposition import NMF
from db import returnElementsFromCL
from db import returnElements
from sklearn.feature_extraction.text import TfidfVectorizer
 
import spacy
nlp = spacy.load('en_core_web_sm')

def matrixSimplifier(mat):
    for j in range(len(mat)):
        max=0
        for i in range(len(mat[j])):
            if mat[j][i]>max:
                max=mat[j][i]
        for i in range(len(mat[j])):
            if(mat[j][i]!=max):
                mat[j][i]=0
            else:
                mat[j][i]=1
    return mat

class LemmaTokenizer(object):
    def __call__(self, text):
        doc=nlp(text)
        tokens=[]
        for token in doc:
            if(token.text.isalpha() and len(token.text)>=2):
                tokens+=[token]
        return [t.lemma_ for t in tokens if t not in nlp.Defaults.stop_words]
X=returnElements("")
for cldescription in X[:10]:
    print(cldescription)
    print("****************************************")
model = TfidfVectorizer(stop_words=nlp.Defaults.stop_words,tokenizer=LemmaTokenizer(),sublinear_tf=True,max_features=300)

limiter=150
Y = model.fit(X[:limiter])
vector = []
for i in range(len(X[:limiter])):
    a=model.transform([X[i]])
    vector.append(a.toarray()[0])




#NMF ----------------------
#X = np.array([[154,20],[100,10],[2,3],[2,5],[147,20],[321,50],[15,1],[7,145],[105,5],[285,1]])

nmfModel = NMF(n_components=3, init='random', random_state=0,shuffle=False)
W = nmfModel.fit_transform(vector)
H = nmfModel.components_
print(W)
print(matrixSimplifier(W)) #Maior peso na linha vira 1, os outros pesos viram 0
