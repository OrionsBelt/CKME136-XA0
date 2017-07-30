import sentiwordnet_analysis as swn
import pickle

##print(swn.sentiment("This movie was awesome! The acting was great, plot was wonderful, and there were pythons...so yea!"))
##print(swn.sentiment("This movie was utter junk. There were absolutely 0 pythons. I don't see what the point was at all. Horrible movie, 0/10"))
##
##word_features5k_f = open("pickled_algos/word_features5

##word_features5k_f.close()
##print(word_features)

from nltk.corpus import sentiwordnet

##print(sentiwordnet.senti_synset("wonderful.a.01"))
print(swn.sentiment("wonderful"))
##from nltk.tag import pos_tag
##print("P:", nltk.pos_tag("wonderful"))
