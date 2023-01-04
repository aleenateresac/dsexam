import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
from nltk import ngrams
from nltk import pos_tag
from nltk import sent_tokenize
Ng = ngrams(sequence=sent_tokenize('Sun rises in the east'), n=1)
for grams in Ng:
    # pos_tag(Ng)
    print(grams)
