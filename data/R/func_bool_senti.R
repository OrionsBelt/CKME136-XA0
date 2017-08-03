#Function to set boolean value for each level of sentiment

ddf = data.frame(fake_norm_red_lines_senti$domain_rank, fake_norm_red_lines_senti$spam_score, 
                 fake_norm_red_lines_senti$comments, fake_norm_red_lines_senti$type, 
                 fake_norm_red_lines_senti$Sentiment,
                 "obj"=rep(0), "pos"=rep(0), "neg"=rep(0)) 

for(i in 6:8)   ddf[grep(names(ddf)[i],ddf[,5]),i]=1
