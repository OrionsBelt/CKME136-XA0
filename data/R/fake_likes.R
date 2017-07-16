#Number of likes per country
aggregate(Mydf$Qty, by=Mydf["DepPC"], FUN=sum)

# Load in `ggplot2`
library(ggplot2)

# Plot the sales per department
ggplot(data=aggregate(Mydf$Qty,by=Mydf["DepPC"],FUN=sum), aes(x=DepPC, y=x)) +
  geom_point()+
  ggtitle("Sales per department - All")

# select only for delivered=True
Y <- Mydf[Mydf$Delivered==TRUE,]

# Plot the sales by department
ggplot(data=aggregate(Y$Qty,by=Y["DepPC"],FUN=sum), aes(x=DepPC, y=x)) +
  geom_point()+
  ggtitle("Sales per department - Delivered")
