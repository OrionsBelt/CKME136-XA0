#Number of likes per country
country_likes<-aggregate(fake2$likes, by=fake2["country"], FUN=sum)

# Load in `ggplot2`
library(ggplot2)

summary(fake2$type)

#Number of bias per country
country_bias<-aggregate(fake2$type, by=fake2["country"], FUN=length)
country_bias<-aggregate(fake2$type=='bias', by=fake2["country"], FUN=length)

# Plot the sales per department
ggplot(data=aggregate(Mydf$Qty,by=Mydf["DepPC"],FUN=sum), aes(x=DepPC, y=x)) +
  geom_point()+
  ggtitle("Sales per department - All")

# select bias only for like=1
like <- fake2[fake2$likes!=0,]
# number of countries likes recorded for tweet
unique(like$country)
# Number of bias if tweet liked for country
country_bias_liked<-aggregate(like$type, by=like["country"], FUN=length)
# assign name to column
country_bias_liked<- merge(country_bias_liked, country_codes, by.x="country", by.y = "CODES")
names(country_bias_liked)[2]<-'Number of Bias w/ Likes'
country_bias_liked

#Number of bias per country by type
fake3<-unique(fake2$type)
country_bias_by_type<-aggregate(fake2$type, by=fake2["country"], FUN= subset(fake2, type == 'bias', select = type))
subset(fake2, type == 'bias', select = type)
country_bias[,'bias']<- length((fake2$type=='bias'))
# Plot the sales by department
ggplot(data=aggregate(Y$Qty,by=Y["DepPC"],FUN=sum), aes(x=DepPC, y=x)) +
  geom_point()+
  ggtitle("Sales per department - Delivered")


#Bias category per country
bias <- fake2[fake2$type=='bias',]
#number of bias news tweets per country
country_bias_bias<-aggregate(bias$type, by=bias["country"], FUN=length)
names(country_bias_bias)[2]<- 'bias_cat'
#merge(country_bias_bias, country_codes, by.x="country", by.y = "CODES")

#Bs category per country
bs <- fake2[fake2$type=='bs',]
#number of bs news tweets per country
country_bias_bs<-aggregate(bs$type, by=bs["country"], FUN=length)
names(country_bias_bs)[2]<- 'bs_cat'
#Merge above table
country_bias_bs<-merge(country_bias_bias, country_bias_bs, by.x="country", by.y = "country", all = TRUE)

#Conspiracy category per country
con <- fake2[fake2$type=='conspiracy',]
#number of bs news tweets per country
country_bias_con<-aggregate(con$type, by=con["country"], FUN=length)
names(country_bias_con)[2]<- 'con_cat'
#Merge above table
country_bias_con<-merge(country_bias_bs, country_bias_con, by.x="country", by.y = "country", all = TRUE)

#Fake category per country
fake <- fake2[fake2$type=='fake',]
#number of bs news tweets per country
country_bias_fake<-aggregate(fake$type, by=fake["country"], FUN=length)
names(country_bias_fake)[2]<- 'fake_cat'
#Merge above table
country_bias_fake<-merge(country_bias_con, country_bias_fake, by.x="country", by.y = "country", all = TRUE)

#Hate category per country
hate <- fake2[fake2$type=='hate',]
#number of bs news tweets per country
country_bias_hate<-aggregate(hate$type, by=hate["country"], FUN=length)
names(country_bias_hate)[2]<- 'hate_cat'
#Merge above table
country_bias_hate<-merge(country_bias_fake, country_bias_hate, by.x="country", by.y = "country", all = TRUE)

#Junksci category per country
junksci <- fake2[fake2$type=='junksci',]
#number of junksci news tweets per country
country_bias_junksci<-aggregate(junksci$type, by=junksci["country"], FUN=length)
names(country_bias_junksci)[2]<- 'junksci_cat'
#Merge above table
country_bias_junksci<-merge(country_bias_hate, country_bias_junksci, by.x="country", by.y = "country", all = TRUE)

#Satire category per country
satire <- fake2[fake2$type=='satire',]
#number of satire news tweets per country
country_bias_satire<-aggregate(satire$type, by=satire["country"], FUN=length)
names(country_bias_satire)[2]<- 'satire_cat'
#Merge above table
country_bias_satire<-merge(country_bias_junksci, country_bias_satire, by.x="country", by.y = "country", all = TRUE)

#State category per country
state <- fake2[fake2$type=='state',]
#number of state news tweets per country
country_bias_state<-aggregate(state$type, by=state["country"], FUN=length)
names(country_bias_state)[2]<- 'state_cat'
country_bias_state<-merge(country_bias_satire, country_bias_state, by.x="country", by.y = "country", all = TRUE)
country_bias_total<-merge(country_bias_state, country_codes, by.x="country", by.y = "CODES")

#Number of likes per countries w/ bias
country_bias_liked_liked<-merge(country_bias_state,country_bias_liked, by.x="country", by.y = "country", all = TRUE)
country_bias_liked_liked<-merge(country_bias_liked_liked, country_codes, by.x="country", by.y = "CODES")

#Number of likes per type
# select bias only for like>1
like <- fake2[fake2$likes!=0,]
# number of countries likes recorded for tweet
unique(like$country)
# Number of likes per type
bias_liked<-aggregate(like$likes, by=like["type"], FUN=length)

# Number of likes per site with likes
site_likes<-aggregate(like$likes, by=like["site_url"], FUN=sum)
site_likes_all<-aggregate(fake2$likes, by=fake2["site_url"], FUN=sum)


####################################################################################
#Same as above for urls
###########################################################################
#Bias category per country
bias <- fake2[fake2$type=='bias',]
#number of bias news tweets per country
url_bias_bias<-aggregate(bias$type, by=bias["site_url"], FUN=length)
names(url_bias_bias)[2]<- 'bias_cat'
#merge(country_bias_bias, country_codes, by.x="country", by.y = "CODES")

#Bs category per country
bs <- fake2[fake2$type=='bs',]
#number of bs news tweets per country
url_bias_bs<-aggregate(bs$type, by=bs["site_url"], FUN=length)
names(url_bias_bs)[2]<- 'bs_cat'
#Merge above table
url_bias_bs<-merge(url_bias_bias, url_bias_bs, by.x="site_url", by.y = "site_url", all = TRUE)

#Conspiracy category per country
con <- fake2[fake2$type=='conspiracy',]
#number of bs news tweets per country
url_bias_con<-aggregate(con$type, by=con["site_url"], FUN=length)
names(url_bias_con)[2]<- 'con_cat'
#Merge above table
url_bias_con<-merge(url_bias_bs,url_bias_con, by.x="site_url", by.y = "site_url", all = TRUE)

#Fake category per country
fake <- fake2[fake2$type=='fake',]
#number of bs news tweets per country
url_bias_fake<-aggregate(fake$type, by=fake["site_url"], FUN=length)
names(url_bias_fake)[2]<- 'fake_cat'
#Merge above table
url_bias_fake<-merge(url_bias_con,url_bias_fake, by.x="site_url", by.y = "site_url", all = TRUE)

#Hate category per country
hate <- fake2[fake2$type=='hate',]
#number of bs news tweets per country
url_bias_hate<-aggregate(hate$type, by=hate["site_url"], FUN=length)
names(url_bias_hate)[2]<- 'hate_cat'
#Merge above table
url_bias_hate<-merge(url_bias_fake, url_bias_hate, by.x="site_url", by.y = "site_url", all = TRUE)

#Junksci category per country
junksci <- fake2[fake2$type=='junksci',]
#number of junksci news tweets per country
url_bias_junksci<-aggregate(junksci$type, by=junksci["site_url"], FUN=length)
names(url_bias_junksci)[2]<- 'junksci_cat'
#Merge above table
url_bias_junksci<-merge(url_bias_hate, url_bias_junksci, by.x="site_url", by.y = "site_url", all = TRUE)

#Satire category per country
satire <- fake2[fake2$type=='satire',]
#number of satire news tweets per country
url_bias_satire<-aggregate(satire$type, by=satire["site_url"], FUN=length)
names(url_bias_satire)[2]<- 'satire_cat'
#Merge above table
url_bias_satire<-merge(url_bias_junksci, url_bias_satire, by.x="site_url", by.y = "site_url", all = TRUE)

#State category per country
state <- fake2[fake2$type=='state',]
#number of state news tweets per country
url_bias_state<-aggregate(state$type, by=state["site_url"], FUN=length)
names(url_bias_state)[2]<- 'state_cat'
url_bias_state<-merge(url_bias_satire, url_bias_state, by.x="site_url", by.y = "site_url", all = TRUE)


#Number of likes per countries w/ bias
country_bias_liked_liked<-merge(country_bias_state,country_bias_liked, by.x="country", by.y = "country", all = TRUE)
country_bias_liked_liked<-merge(country_bias_liked_liked, country_codes, by.x="country", by.y = "CODES")

