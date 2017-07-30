import sys
import nltk
import pickle
import csv
import sentiwordnet_analysis as swn

count=0
i=0
senti_row = []
senti_row2 = []
senti_output = []
#, encoding="utf-8
with open('fake_sentiment_short.csv', 'r', encoding='utf8') as f:
    #outCSV=(line for line in csv.reader(f, dialect='excel'))
    reader = csv.reader(f)
    for row in reader:
        #print(("row: ", row))
   
        count = count + 1
        senti_row = swn.sentiment(row)
        #print("senti_row: ", senti_row)
        senti_str = ''.join(str(senti_row))
        #print("senti_str: ", senti_str)
       # writer.writerow(senti_str)
##        senti_row2 = senti_row#+list('\n')
        senti_output.append(senti_row)

header = ['text', 'sentiment']        
        
#for row in writer:
with open('senti_fake_sentiment_short.csv', 'w') as p:
    writer = csv.writer(p, delimiter='/')
#senti_str = ''.join(str(e) for e in senti_output)
#senti_str = ','.join(map(str, senti_output))
#senti_str = ''.join(str(senti_output))
##with open('senti_fake_sentiment.csv', 'w') as p:
##    #fieldnames = ['Text', 'Sentiment']
##    writer = csv.writer(p, delimiter=',')
##    #writer.writeheader()
    for line in senti_output: 
      writer.writerow([line])
####        #while(i < count):

##with open('senti_fake_sentiment.txt', 'w') as p:
##    #fieldnames = ['Text', 'Sentiment']
##    for line in senti_str:
##        p.write(line)

##fid = cfile('senti_fake_sentiment.txt', 'w')
##for c in fid:
##    fid.wl(senti_str)
##fid.close()
##    
         #   i =  i + 1
print("C: ", count)   
