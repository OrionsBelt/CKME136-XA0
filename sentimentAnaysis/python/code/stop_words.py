from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import pickle

#Can find corpus for stop words in /Users/./AppDAta/Roaming/ntlk_data/corpora/stopwords
stop_words = set(stopwords.words("english"))
filtered_sentence = []
def stop_words(text):
    filtered_sentence.clear()
    words = word_tokenize(str(text))
    for w in words:
        if w != stop_words:
            filtered_sentence.append(w)
    #print("filtered:", filtered_sentence)

    save_stop_words = open("pickle/stop_words.pickle","wb")
    pickle.dump(filtered_sentence, save_stop_words)
    save_stop_words.close()
            
    return(filtered_sentence)


