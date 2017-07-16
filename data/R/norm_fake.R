#Normalization Script and Plot of Outliers

View(fake)
fake
# Num of rows
rowsum(fake)

#unique site url (244)
unique(fake$site_url)
#count number of unique rows
length(unique(fake$site_url))

#unique domain rank instances (134)
unique(fake$domain_rank)
length(unique(fake$domain_rank))

head(fake)
str(fake)
summary(fake)
# Summary shows high correlation between likes and shares, remove shares
# Remove uid and language column, all language in english and uid unncessary for analysis
# Make type, order in thread and domain rank factors however lets analyze the relationship further
# domain rank orders the sites based on web traffic, the lower the rank the higher the traffic (webhose.io)

# create subset of sites ...
fake_sub <- subset(fake, select=c(site_url, domain_rank, type))
fake_sub <- unique(fake_sub)
fake_sub_ord <- fake_sub[order(fake_sub$domain_rank, na.last = TRUE, decreasing = FALSE), ]

fake_sub$domain_rank <- as.factor(fake_sub$domain_rank)
fake_sub_ord_ord <- fake_sub[order(fake_sub$domain_rank, na.last = TRUE, decreasing = FALSE), ]

#Make type factor
fake_sub$type <- as.factor(fake_sub$type)
fake_sub_ord_type <- fake_sub[order(fake_sub$type, na.last = TRUE, decreasing = FALSE), ]
#Print levels for type
levels(fake_sub$type)

#Remove shares uuid
fake2 <- subset(fake, select=-c(uuid))
fake2 <- subset(fake, select=-c(shares))

#Make domain rank, order in thread and type factors
fake2$ord_in_thread<-as.factor(fake2$ord_in_thread)
fake2$type<-as.factor(fake2$type)
fake2$domain_rank<-as.factor(fake2$domain_rank)




