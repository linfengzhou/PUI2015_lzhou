#first attempt at implementing horizon plots in ggplot2
#pleased with result but code sloppy and inflexible
#as always very open to improvements and forks

require(ggplot2)
require(reshape2)
require(quantmod)
require(PerformanceAnalytics)
require(xtsExtra)

data(edhec)
colnames(allclean) <- c('DJIA','GSPC','SSEC','N225','STI','HSI') 
edhec = allclean/100
origin = 0
horizonscale = 0.05
#get 12 month rolling return of edhec indexes
roc <- as.xts(apply(cumprod(edhec+1),MARGIN=2,ROC,n=12,type="discrete"),order.by=index(edhec))

roc.df <- as.data.frame(cbind(index(roc),coredata(roc)))
roc.melt <- melt(roc.df,id.vars=1)
roc.melt[,1] <- as.Date(roc.melt[,1])  #convert back to a Date


horizon.panel.ggplot <- function(df, title) {
  #df parameter should be in form of date (x), grouping, and a value (y)
  colnames(df) <- c("date","grouping","y")
  #get some decent colors from RColorBrewer
  #we will use colors on the edges so 2:4 for red and 7:9 for blue
  require(RColorBrewer)
  col.brew <- brewer.pal(name="RdBu",n=10)
  
  #get number of bands for the loop
  #limit to 3 so it will be much more manageable
  nbands = 3 
  
  
  #loop through nbands to add a column for each of the positive and negative bands
  for (i in 1:nbands) {
    #do positive
    df[,paste("ypos",i,sep="")] <- ifelse(df$y > origin,
                                          ifelse(abs(df$y) > horizonscale * i,
                                                 horizonscale,
                                                 ifelse(abs(df$y) - (horizonscale * (i - 1) - origin) > origin, abs(df$y) - (horizonscale * (i - 1) - origin), origin)),
                                          origin)
    #do negative
    df[,paste("yneg",i,sep="")] <- ifelse(df$y < origin,
                                          ifelse(abs(df$y) > horizonscale * i,
                                                 horizonscale,
                                                 ifelse(abs(df$y) - (horizonscale * (i - 1) - origin) > origin, abs(df$y) - (horizonscale * (i - 1) - origin), origin)),
                                          origin)
  }
  #melt data frame now that we have added a column for each band
  #this will fit ggplot2 expectations and make it much easier
  df.melt <- melt(df[,c(1:2,4:9)],id.vars=1:2)    
  #name the columns for reference
  #try to be generic
  colnames(df.melt) <- c("date","grouping","band","log_return")
  
  #use ggplot to produce an area plot
  p <- ggplot(data=df.melt) +
    geom_area(aes(x = date, y = log_return, fill=band),
              #alpha=0.9,
              position="identity") +  #this means not stacked
    scale_fill_manual(values=c("ypos1"='#a1d99b',  #assign the colors to each of the bands; colors get darker as values increase
                               "ypos2"='#addd8e',
                               "ypos3"='#31a354',
                               "yneg1"='#fdbb84',
                               "yneg2"='#fc9272',
                               "yneg3"='#de2d26')) +
    ylim(origin,horizonscale) +   #limit plot to origin and horizonscale
    facet_grid(grouping ~ .) +    #do new subplot for each group
    theme_bw() + #this is optional, but I prefer to default
    ggtitle('Stock Market Indexes') +
    theme(plot.title=element_text(size=rel(1.5),family='Helvetica',face='bold.italic'),
          axis.title.x = element_text(size=18),
          axis.title.y = element_text(size=18))
  return(p)
}



horizon.panel.ggplot(roc.melt, "Stock Market Indexes")
