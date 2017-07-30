import nltk
import pickle
from nltk.tag import pos_tag
from nltk.tokenize import PunktSentenceTokenizer


###Part of Speech tagging w/ PunktSentenc Tokenizer

# list of sentiWordNet tagged notation of POS tagged list
senti_tags = []
# list of tuples with POS tagged text in SentiWordNet notation
tagged_tags = []

# Tagged sentences from corpus for training
tagged_sentences = nltk.corpus.treebank.tagged_sents()
 

# returns tagged 
def untag(tagged_sentence):
    return [w for w, t in tagged_sentence]

def features(sentence, index):
    """ sentence: [w1, w2, ...], index: the index of the word """
    return {
        'word': sentence[index],
        'is_first': index == 0,
        'is_last': index == len(sentence) - 1,
        'is_capitalized': sentence[index][0].upper() == sentence[index][0],
        'is_all_caps': sentence[index].upper() == sentence[index],
        'is_all_lower': sentence[index].lower() == sentence[index],
        'prefix-1': sentence[index][0],
        'prefix-2': sentence[index][:2],
        'prefix-3': sentence[index][:3],
        'suffix-1': sentence[index][-1],
        'suffix-2': sentence[index][-2:],
        'suffix-3': sentence[index][-3:],
        'prev_word': '' if index == 0 else sentence[index - 1],
        'next_word': '' if index == len(sentence) - 1 else sentence[index + 1],
        'has_hyphen': '-' in sentence[index],
        'is_numeric': sentence[index].isdigit(),
        'capitals_inside': sentence[index][1:].lower() != sentence[index][1:]
    }
 
##import pprint 
##pprint.pprint(features(['This', 'is', 'a', 'sentence'], 2))
## 
##{'capitals_inside': False,
## 'has_hyphen': False,
## 'is_all_caps': False,
## 'is_all_lower': True,
## 'is_capitalized': False,
## 'is_first': False,
## 'is_last': False,
## 'is_numeric': False,
## 'next_word': 'sentence',
## 'prefix-1': 'a',
## 'prefix-2': 'a',
## 'prefix-3': 'a',
## 'prev_word': 'is',
## 'suffix-1': 'a',
## 'suffix-2': 'a',
## 'suffix-3': 'a',
## 'word': 'a'}

# Split the dataset for training and testing
cutoff = int(.75 * len(tagged_sentences))
training_sentences = tagged_sentences[:cutoff]
test_sentences = tagged_sentences[cutoff:]
 
#print(training_sentences)   # 2935
#print len(test_sentences)         # 979
 
def transform_to_dataset(tagged_sentences):
    X, y = [], []
 
    for tagged in tagged_sentences:
        for index in range(len(tagged)):
            X.append(features(untag(tagged), index))
            y.append(tagged[index][1])
 
    return X, y
 
X, y = transform_to_dataset(training_sentences)

from sklearn.tree import DecisionTreeClassifier
from sklearn.feature_extraction import DictVectorizer
from sklearn.pipeline import Pipeline
clf = Pipeline([
('vectorizer', DictVectorizer(sparse=False)),
('classifier', DecisionTreeClassifier(criterion='entropy'))
])
clf.fit(X[:10000], y[:10000])   # Use only the first 10K samples if you're running it multiple times. It takes a fair bit :)
print ('Training completed')
X_test, y_test = transform_to_dataset(test_sentences)
print ("Accuracy:", clf.score(X_test, y_test))
# Accuracy: 0.904186083882
# not bad at all :)

# Function to convert POS tagging to sentiWordNet tagging values
def conv_tag(treebank_tag):
    
   if treebank_tag.startswith('J'):
       return 'a'
   elif treebank_tag.startswith('V'):
       return 'v'
   elif treebank_tag.startswith('N'):
       return 'n'
   elif treebank_tag.startswith('R'):
       return 'r'
   else:
       return ''

# Function to replace tags in tuple
def replace_at_index1(tup, ix, val):
    lst = list(tup)
    lst[ix] = val
    return tuple(lst)
    
#sentence = "Iphone6 camera is awesome for low light "
 #Function to perform sentiWordNet POS tagging
def pos_tagging(text):
    senti_tags.clear()
    tagged_tags.clear()
    #token = nltk.word_tokenize(str(text))
    #tagged = nltk.pos_tag(text)
    
    #Draw known named entities
    #namedEnt = nltk.ne_chunk(tagged, binary=True)
    #namedEnt.draw()
   
    #Need to convert this to normal sentiwordnet tags n,v, etc.
    #Using list comprehension to return tagged values
    tags = [x[1] for x in text]

    for t in tags:
        c_tag = conv_tag(t)
        senti_tags.append(c_tag)

    for i in range (len(text)):
        r_tup = replace_at_index1(text[i], 1, senti_tags[i])
        tagged_tags.append(r_tup)

     #Pickle to serialize function
    save_pos_tagging = open("pickle/pos_tagging.pickle","wb")
    pickle.dump(tagged_tags, save_pos_tagging)
    save_pos_tagging.close()
             
    return(tagged_tags)

#Function to perform POS tagging using trained feature set
def pos_tag(sentence):
   # token = nltk.word_tokenize(str(sentence))
    tagged_sentence = []
    tags = clf.predict([features(sentence, index) for index in range(len(sentence))])
    tagged_sentence = [[i, j] for i, j in zip(sentence, tags)]

    #Pickle to serialize function
    save_pos_tag = open("pickle/pos_tag.pickle","wb")
    pickle.dump(tagged_sentence, save_pos_tag)
    save_pos_tag.close()
    return(tagged_sentence)

