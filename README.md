# Plotting in real time the most popular Twitter hashtags with SparkStreaming.

Simple application that plots out the popularity of tags associated with incoming tweets streamed live from Twitter.

## Quick Start

First of all, you need to setup a Developer API acocunt with Twitter and create an application to get credentials. Just visit [Twitter Developer Platform](https://apps.twitter.com/).

Once you have that, you also need to install **tweepy**, a python library to connect your Python to the twitter dev account. Also, **matplotlib** and **pandas** will be needed.

Then, run only the first 8 cells of the jupyter notebook *TwitterSparkStreaming.ipynb*.

Now, run the *twitterScanner.py* file. Make sure to add your own IP Adress and your credential keys (note that I have cleared mine from *twitterScanner.py*). Use the following command:

```bash
$ python3 twitterScanner.py
```
Now, run the next 3 cells of the jupyter notebook sequentially.

To finish the streaming, run the last cell of the jupyter notebook. You can then see how the display of tweets containing the specified word or string per console also terminates.

## How it works

This is an example of the graphics shown for when scanning tweets which contain the word ***'art'***. You can see the most popular hastags that follow that word in real time: <p align="center"> <img src="/img/img1.PNG"/>

## Acknowledgements

Thanks to [Jose Portilla](https://www.linkedin.com/in/jmportilla/), as this project has been developed in the framework of *Spark and Python for Big Data with PySpark* course.
