#Normalization Script and Plot of Outliers

View(fake_infowars)
fake_infowars
# Num of rows
rowsum(fake_infowars)

#unique site url (244)
unique(fake_infowars$site_url)
#count number of unique rows
length(unique(fake_infowars$site_url))

#unique domain rank instances (134)
unique(fake_infowars$domain_rank)
length(unique(fake_infowars$domain_rank))

head(fake_infowars)
str(fake_infowars)
summary(fake_infowars)
# Summary shows high correlation between likes and shares, remove shares
# Remove uid and language column, all language in english and uid unncessary for analysis
# Make type, order in thread and domain rank factors however lets analyze the relationship further
# domain rank orders the sites based on web traffic, the lower the rank the higher the traffic (webhose.io)

# create subset of sites ...
fake_sub <- subset(fake_infowars, select=c(site_url, domain_rank, type))
fake_sub <- unique(fake_sub)
fake_sub_ord <- fake_sub[order(fake_sub$domain_rank, na.last = TRUE, decreasing = FALSE), ]

fake_sub$domain_rank <- as.factor(fake_sub$domain_rank)
fake_sub_ord_ord <- fake_sub[order(fake_sub$domain_rank, na.last = TRUE, decreasing = FALSE), ]

#Make type factor
fake_sub$type <- as.factor(fake_sub$type)
fake_sub_ord_type <- fake_sub[order(fake_sub$type, na.last = TRUE, decreasing = FALSE), ]
#Print levels for type
levels(fake_sub$type)

#Remove shares uuid ord_in_thread author crawled
fake_infowars <- subset(fake_infowars, select=-c(uuid))
fake_infowars <- subset(fake_infowars, select=-c(shares))
fake_infowars <- subset(fake_infowars, select=-c(ord_in_thread))
fake_infowars <- subset(fake_infowars, select=-c(author))
fake_infowars <- subset(fake_infowars, select=-c(crawled))
fake_infowars <- subset(fake_infowars, select=-c(language))
fake_infowars <- subset(fake_infowars, select=-c(published, title, text, country, thread_title, main_img_url))

# omit na
fake_infowars <- na.omit(fake_infowars)

#Make domain rank, order in thread type and spam score factors
#fake_infowars$ord_in_thread<-as.factor(fake_infowars$ord_in_thread)
fake_infowars$type<-as.factor(fake_infowars$type)

#Normalize domain rank to have the same ratio as spam_score
fake_infowars$domain_rank<-fake_infowars$domain_rank/max(na.omit(fake_infowars$domain_rank))
summary(fake_infowars)

#Find order of type (bs, bias, conspiracy, hate, satire, state, junksci, fake)
summary(fake_infowars$type)

#Write to csv file
write.csv(fake_infowars, file = "fake_norm_infowars.csv")



