from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
import pickle
#Lemmatize words
#Use WordNet to Lemmantize words
lemmatizer = WordNetLemmatizer()

lemmatize_list = []

def lemmatize_words(text):
    lemmatize_list.clear()
    #words = word_tokenize(str(text))
    words = text
    #print("words: ", words)  
    for w in words:
        lem_word = lemmatizer.lemmatize(w)
        lemmatize_list.append(lem_word)

    save_lemmatize_words = open("pickle/lemmatize.pickle","wb")
    pickle.dump(lemmatize_list, save_lemmatize_words)
    save_lemmatize_words.close()

    return(lemmatize_list)


