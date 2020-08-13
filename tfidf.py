from db import returnElementsFromCL
from db import returnElements
from sklearn.feature_extraction.text import TfidfVectorizer
 
import spacy
nlp = spacy.load('en_core_web_sm')

class LemmaTokenizer(object):
    def __call__(self, text):
        doc=nlp(text)
        tokens=[]
        for token in doc:
            if(token.text.isalpha() and len(token.text)>=2):
                tokens+=[token]
        return [t.lemma_ for t in tokens if t not in nlp.Defaults.stop_words]
X=returnElements("")
print(X[:2])
model = TfidfVectorizer(stop_words=nlp.Defaults.stop_words,tokenizer=LemmaTokenizer(),sublinear_tf=True,max_features=300)
Y = model.fit(X)
vector = model.transform([X[0]])

print(vector.toarray())