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
    
    /* Open Sources Description from their website*/\
    
    My Description:  Open source has a large database of information from both unreliable news sources. By using a variety of methods to determine if a site is unreliable open source will classify the site with one of the categories listed above.  See below for a description of 'OPEN sOURCE' by Open Source:
    
    Who we are:

OpenSources is a curated resource for assessing online information sources, available for public use. Websites in this resource range from credible news sources to misleading and outright fake websites. Headed by Melissa Zimdars of Merrimack College, our research team is dedicated to preserving the integrity and enhancing the transparency of information on the internet.
Mission:

Our mission is to empower people to find reliable information online.

To this end, we provide a continuously updated database of information sources for developers to leverage in the fight against fake, false, conspiratorial, and misleading news. Our database is maintained by professionals who have analyzed each source, looking for overall inaccuracy, extreme biases, lack of transparency, and other kinds of misinformation.
Tags:

Open Sources uses combinations of the following tags to classify each website we assess.

Fake News (tag fake) Sources that entirely fabricate information, disseminate deceptive content, or grossly distort actual news reports

Satire (tag satire) Sources that use humor, irony, exaggeration, ridicule, and false information to comment on current events.

Extreme Bias (tag bias) Sources that come from a particular point of view and may rely on propaganda, decontextualized information, and opinions distorted as facts.

Conspiracy Theory (tag conspiracy): Sources that are well-known promoters of kooky conspiracy theories.

Rumor Mill (tag rumor) Sources that traffic in rumors, gossip, innuendo, and unverified claims.

State News (tag state) Sources in repressive states operating under government sanction.

Junk Science (tag junksci) Sources that promote pseudoscience, metaphysics, naturalistic fallacies, and other scientifically dubious claims.

Hate News (tag hate) Sources that actively promote racism, misogyny, homophobia, and other forms of discrimination.

Clickbait (tag clickbait) Sources that provide generally credible content, but use exaggerated, misleading, or questionable headlines, social media descriptions, and/or images.

Proceed With Caution (tag unreliable) Sources that may be reliable but whose contents require further verification.

Political (tag political) Sources that provide generally verifiable information in support of certain points of view or political orientations.

Credible (tag reliable) Sources that circulate news and information in a manner consistent with traditional and ethical practices in journalism (Remember: even credible sources sometimes rely on clickbait-style headlines or occasionally make mistakes. No news organization is perfect, which is why a healthy news diet consists of multiple sources of information).
Our Methods:

Step 1: Title/Domain Analysis. If “.wordpress” “.com.co” appear in the title -- or any slight variation on a well known website-- this is usually a sign there is a problem.

Step 2: About Us Analysis. Google every title/domain name/anyone listed in the “About Us” section to see if anyone has previously reported on the website (snopes, hoax-slayer, factcheck.org, etc.) or whether it has a Wikipedia page with citations or something similar detailing its background. This is useful for identifying and correctly categorizing lesser known and/or new websites that may be on the up-and-up, such as satirical sources or websites that are explicit about their political orientation.

Step 3: Source Analysis. Does the website mention/link to a study or source? Look up the source/study. Is it being accurately reflected and reported? Are officials being cited? Can a primary source be located for its quotations? Some media literacy and critical scholars call this triangulation: Verify details, facts, quotes, etc. with multiple sources.

Step 4: Writing Style Analysis. Does the website follow AP Style Guide? Typically, lack of style guide use signifies questionable, more opinion-oriented practices, and may indicate an overall lack of editing or fact-checking process. Does it frequently use ALL CAPS in headlines and/or body text? Does the headline or body of the text use phrases like "WOW!!!!"? This stylistic practice and these types of hyperbolic word choices are often used to create emotional responses with readers that is avoided in more traditional journalism and isn’t something that would be permitted or encouraged by the AP Style Guide

Step 5: Aesthetic Analysis. Like the style-guide, many fake and questionable news sites utilize very bad design. Are screens are cluttered and they use heavy-handed photo-shopping or born digital images?

Step 6: Social Media Analysis. Look up the website on Facebook. Do the headlines and posts rely on sensational or provocative language (aka click-bait) in order to attract attention and encourage likes, click-throughs, and shares? Do the headlines and social media descriptions match or accurately reflect the content of the linked article? (this step isn’t particularly good at helping us find fake news, but it can help us identify other misleading news sources)

By considering all of these areas of information we can determine which category or categories a website may occupy, although all categorizations are by necessity open to discussion and revision. For more information about analyzing the credibility of sources, please see this resource.

Disclaimer The information contained in this site is for informational and educational purposes only. We have made every attempt to ensure that the information contained in this site and in our downloadable data is reliable; however, we are not responsible for any errors, or for the results obtained from the use of this information. All information in this site is provided “as is” and “as available,” with no guarantee of accuracy, reliability, completeness, or of the services or results obtained from the use of this information. By using OpenSources, you expressly agree that the use of OpenSources and its data is at your sole risk. 



