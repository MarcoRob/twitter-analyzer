# Twitter Analyzer 

## Project for Programming Languages Course

### Purpose 
> Generate a Filter-Map-Reduce implementation from Tweets that are obtained from Twitter in certain time. And presente the information using graphs, diagrams, tables or any visual resource for explanation purpose.

### Project
> This project consists in 2 parts, the backend/gather data part and the ui/server presentation part

> If you want to gather data from Twitter (go to twitter-mapreduce folder), set your twitter tokens in tweet-script.py, the run the following commands
```
python3 tweet-script.py [hashtag for querie]
```

> To process the word-count run the following commands *note: you should have installed hadoop
```# Copy textfile to the hdfs job folder
hdfs dfs -copyFromLocal -f fetched_tweets.txt /tweet-wordcounter-job

# Remove completed-wordcount directory from past completed jobs
hdfs dfs -rm -r -f /completed-wordcount

# MapReduce Job
hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.7.3.jar -mapper "python3 mapper.py" -reducer "python3 reducer.py" -input /tweet-wordcounter-job/fetched_tweets.txt -output /completed-wordcount 

# Copy completed-wordcount directory to local directory
hdfs dfs -copyToLocal /completed-wordcount
```

> Once you have finished, you can run the server in order to see the table word count
> You should have installed nodejs
```
npm install
``` 
and 
```
npm start
```

> Go to the browser and enter to localhost:3000/api/counts, to see the table generated
