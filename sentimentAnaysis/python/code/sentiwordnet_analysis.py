import nltk
import pickle
import collections
import stop_words as stp
import lemmatize_words as lemm
import pos_tagging as pos
#import pos_tag as post
from nltk.corpus import sentiwordnet
from collections import Counter

###Part of Speech tagging w/ PunktSentenc Tokenizer

# list of tuples with POS tagged text in SentiWordNet notation
pno_body_txt_tagged = []
pno_tags_ret = []
pno_tags = []
pos_l = []
neg_l = []
obj_l = []
#index = 0
#idx = 0
text = []
mode_list = []
mode_list_v = []
w = []
wd = []
pno_tags_clean = []
    
# Function to replace tags in tuple
def replace_at_index1(tup, ix, val):
    lst = list(tup)
    lst[ix] = val
    return tuple(lst)

def process_content(text2, indx):
        pno_tags.clear()
        # Assign count to next tuple in index
        count = indx
        error = 0
        # Assign text to global var
  
        while (count < (len(text2))):
            try:
                
                # Assign i to global var
                #idx = indx
                # Synset summary
                pn_score = sentiwordnet.senti_synset(text2[indx][0]+"."+text2[indx][1]+".01")
                
                #print(pn_score)
                #Obtain breakdown of each score
                pos = pn_score.pos_score()
                pos_l = [("/pos", pos)]
                neg = pn_score.neg_score()
                neg_l = [("/neg", neg)]
                obj = pn_score.obj_score()
                obj_l = [("/obj", obj)]
                #Set to obj if pos/neg 0.0
                if(pos == 0.0 and neg == 0.0):
                    pno_list = obj_l
                elif(pos != 0.0 or neg != 0.0):
                     pno_list = (pos_l+neg_l)
                else:
                    pno_list = (pos_l+neg_l+obj_l)
                #Sort list by pos/neg/obj score
                pno_list_sort =sorted(pno_list, key=lambda pno: pno[1], reverse=True)
                
                #Substitute pos/neg/obj value in tuple for old POS value
                text_tup = replace_at_index1(text2[indx], 1, pno_list_sort[0][0])
        
                #Append to list of pos/neg/obj tags
                pno_tags.append(text_tup)
                #Remove tuples with no word value
                pno_tags_clean = [i for i in pno_tags if i[0] != '']    
                #Increment count and indx
                count = count + 1
                indx = indx + 1
            except Exception as e:
                #print("Error: %", (e.args[0]))
                #Substitute objective value for word not found
                pno_tags.append(('',"/obj"))
                #Increment count and indx
                if(count == (len(text2) - 1) and (error==count)):
                    pno_tags_clean = [('',"/obj")]
                error = error+1
                count = count + 1
                indx = indx + 1
        return(pno_tags_clean)

# Function to find mode of senti tagged list
def mode_senti_sc(senti_txt):
        mode_list.clear()
        mode_list_v.clear()
        w.clear()
        nonzero_c = 0
        value2 =0
        #Take mode of senti score tag and apply that to body of text
        mode = Counter(elem[1] for elem in senti_txt)
        #Determine if non-zero in list
   
        del mode['/obj']
        for k,v in mode.items():  
            if(v != 0):
                nonzero_c = nonzero_c +1
                w.append(v)
            else:
                 w.append('/obj')
                 nonzero_c = nonzero_c +1

        mode_list.append(sorted(mode, key=mode.get, reverse=True))
        if(nonzero_c > 1):
            new_list = ['/']
            if(w[0] == w[1]):
                mu = mode_list 
            else:
                mu = mode_list[0][0]
        else:
            mu = '/obj'    
       # #print("m_list: ", i)
           
        return(mu)
    
# Function to perform sentiWordNet Senti analysis over body of text
def sentiwordnet_analysis(text):
    pno_body_txt_tagged.clear() # Dont clear any tags
    ##print sentiword breakdown
    ##print("t: ", text)
    # Return list of tuples with pos/neg/obj tags
    
    pno_tags_ret = process_content(text, 0)  #changed index from a hard 0 to 'index' 

    # Return mode of pos/net/obj
    mode_ret = mode_senti_sc(pno_tags_ret)
   
    #Create list of words from senti tagged list
    words = [x[0] for x in pno_tags_ret]
    
    #Create tuple with mode of senti tagged to body of text
    pno_body_txt_tagged.append((words,mode_ret))
    ##print("pno_body: ", pno_body_txt_tagged)
    
    #Pickle to serialize function
    save_pno_body_txt_tagged = open("pickle/senti.pickle","wb")
    pickle.dump(pno_body_txt_tagged, save_pno_body_txt_tagged)
    save_pno_body_txt_tagged.close()
        
    return(pno_body_txt_tagged)

# Function to input tweet and run analysis
def sentiment(tweet):

    #Read in tweet to stop words function
    stop_tweets = stp.stop_words(tweet)
    
    #Load pickle serialized data stream
    open_file = open("pickle/stop_words.pickle", "rb")
    stop_words_ser = pickle.load(open_file)
    open_file.close()

    #Lemmatize stop words
    lemma_tweets = lemm.lemmatize_words(stop_words_ser)
    #print("lem_tweets: ", lemma_tweets)
    
    #Load lemmatized serialized data stream
    open_file = open("pickle/lemmatize.pickle", "rb")
    lemmatize_words = pickle.load(open_file)
    open_file.close()

    #POS tagging
    POS_tweets = pos.pos_tag(lemmatize_words)

    #Load POS serialized data stream
    open_file = open("pickle/pos_tag.pickle", "rb")
    pos_tag_words = pickle.load(open_file)
    open_file.close()

    #SentiwordNet POS tagging
    POS_tweets_senti = pos.pos_tagging(pos_tag_words)

    #Load senti POS serialized data stream
    open_file = open("pickle/pos_tagging.pickle", "rb")
    pos_tag_senti_words = pickle.load(open_file)
    open_file.close()
    
    #Senti Analysis
    senti_tweets = sentiwordnet_analysis(pos_tag_senti_words)

    #Load Senti serialized data stream
    open_file = open("pickle/senti.pickle", "rb")
    senti_words = pickle.load(open_file)
    open_file.close()

    sent_w = senti_words
    
    # Return list of tuples with pos/neg/obj tag to add to table
   
    return(sent_w) 
