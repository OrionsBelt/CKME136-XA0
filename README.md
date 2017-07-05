# CKME136-XA0
CAPSTONE Project
University CAPSTONE project.
Theme will be Classification and Sentiment Analysis.
The intention is to use Twitter feeds to build Opionion mining sentiment analysis engine to determine the polarity of twitter tweets using ngrams.  These ngrams will be compared to a database of known phrases and words that have been previously assigned sentiment.  Further evaluation will determine the validity of the tweets (only news sources/articles will be used from tweets) to access the probablity of the article/news/tweet being false or fake news.  Results will be displayed graphically.

fake-news.zip // Compressed file of fake news data including classifications of bs, 
              // Text and metadata from fake news sites:
              // Classification datasets in csv file
              //uuid: unique identifier
              //ord_in_thread
              //author: author of story
              //published: date published
              //title: title of story
              //text: text of story
              //language: data from webhose.io
              //crawled: date the story was archived
              //site_url: site URL from BS detector
              //country: data from webhose.io
              //domain_rank: data from webhose.io
              //thread_title
              //spam_score: data from webhose.io
              //main_img_url: image from story
              //replies_count: number of replies
              //participants_count: number of participants
              //likes: number of Facebook likes
              //comments: number of Facebook comments
              //shares: number of Facebook shares
              //type: type of website (label from BS detector)
              
              /*BS Detectgor - used by fake-news.zip to classify data into categories related to fake news sources*/
B.S. Detector is a rejoinder to Mark Zuckerberg's dubious claims that Facebook is unable to substantively address the proliferation of fake news on its platform. A browser extension for both Chrome and Mozilla-based browsers, B.S. Detector searches all links on a given webpage for references to unreliable sources, checking against a manually compiled list of domains. It then provides visual warnings about the presence of questionable links or the browsing of questionable websites:

bs-detector-alert

The B.S. Detector is powered by OpenSources, a professionally curated list of unreliable or otherwise questionable sources. We no longer maintain our own dataset. Neither the B.S. Detector nor the Self Agency LLC assume liability for the accuracy of OpenSources' data. To suggest or dispute a site's inclusion, file an issue with OpenSources.

Example domain classifications (in flux) include:

    Fake News: Sources that fabricate stories out of whole cloth with the intent of pranking the public.
    Satire: Sources that provide humorous commentary on current events in the form of fake news.
    Extreme Bias: Sources that traffic in political propaganda and gross distortions of fact.
    Conspiracy Theory: Sources that are well-known promoters of kooky conspiracy theories.
    Rumor Mill: Sources that traffic in rumors, innuendo, and unverified claims.
    State News: Sources in repressive states operating under government sanction.
    Junk Science: Sources that promote pseudoscience, metaphysics, naturalistic fallacies, and other scientifically dubious claims.
    Hate Group: Sources that actively promote racism, misogyny, homophobia, and other forms of discrimination.
    Clickbait: Sources that are aimed at generating online advertising revenue and rely on sensationalist headlines or eye-catching pictures.
    Proceed With Caution: Sources that may be reliable but whose contents require further verification.



