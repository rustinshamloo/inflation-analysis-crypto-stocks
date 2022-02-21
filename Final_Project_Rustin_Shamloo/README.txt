
What my code entails:

My project consists of data collected from Coinbase's API, S&P500 ETF $SPY data collected from AlphaVantage's Stocks API, and scraped data from BLS.gov's Consumer Price Index webpage (HTML). The goal was to gather the data, visualize them individually, and then think of ways to compare/contrast them against each other to determine from the point of view of someone investing $1,000 in 2016, which investment would provide the best return (ROI) to hedge against inflation by now, in 2021. There is still progress to be made; however, the visualizations and analysis already done should provide some relevant insights as a starting point. Please reference the Project Description PDF in the accompanied folder if you would like to get a better high-level idea of my project before running the code.


How to run the code:

Simply run it from the command line by getting into the proper folder (Final_Project_Rustin_Shamloo)
Then, from the command line, enter: 
>> python Final_Project_Rustin_Shamloo.py (for Default mode)
>> python Final_Project_Rustin_Shamloo.py --static (for Static mode, pulling a few lines from the .csv files in the folder)


* * * PLEASE NOTE: * * *

You may see a JSONDecodeError. This happens when running the code for the first time, or when running between different Modes. Please disregard the error message and run the script again until it runs. It should work; the most I've had to do this was twice until it ran again perfectly. Also note that the rest of the code will not run until you close the plots. Not sure exactly why this is, but it compiles one plot at a time. Perhaps because it is reading one line at a time.
* * *



Extensibility:

Ideally, with more time, I would like to merge the datasets (join on "date" with the same granularity, if possible) and superimpose the graphs.
This would allow for easier local analysis and ROI calculations to determine which asset provides the best hedge against inflation, and to see at what point in time there were inflection points in the respective graphs. This will likely be done through a pandas data frame, since they already are all in that format, or creating a master SQL database to house all of the data and then join and query the data there. I also acknowledge that my code could be more efficient. For example, for the Scrape Mode functions (ie. "scrape_coinbase_head()"), I copied the "scrape_coinbase()" function and changed the print(df) to print(df.head()). The same was done for the other two functions. This was to ensure that the code ran properly, but I do recognize that this may add to latency and runtime unnecessarily. Going forward, I will try to re-do this in a way that yields a better Big-O and more elegant code.


Maintainability:

As stated above, there may be a JSONDEcodeError. Please disregard and run again at least once; it should work. I tried this over 10 times and never saw that error again after running it a second or third time. This may be due to reactions time between requests. Additionally, the code will fail if the API is down for some reason, or if the connection is lost between the API or Beautiful Soup. Other than that, I personally have not run into any other errors. If any issues arise, please contact me so I can help or provide you with what the Jupiter Notebook of what my code looks like when run.




