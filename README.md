# Graphing in real time the most popular Twitter hashtags with SparkStreaming 

Simple application that plots out the popularity of tags associated with incoming tweets streamed live from twitter.

In order to simplify the task, [Cloud9](https://c9.io) has been used, in which I have worked with **node.js** and **express** framework to build the server.

## Quick Start

As I didn't upload the *node_modules* folder, which must contain dependencies, If you want to install them just run the following command:

```bash
$ npm install
```
  Note that ***package.json*** is supposed to update automatically (please, check it out anyway).
  
Also, a **join_us** database must be created. You can do it through MySQL CLI using:

```bash
$ mysql-ctl cli
```

## How it works

This is what we visualize when we enter the URL: <p align="center"> <img src="/imgs/screenshot1.PNG"/>
  
Then, we can proceed to enter an email address: <p align="center"> <img src="/imgs/screenshot2.PNG"/>
  
And, once we press *Join Now*, the count of members who have joined the cult increases unitarily in an interactive way: <p align="center"> <img src="/imgs/screenshot3.PNG"/>

## Acknowledgements

Thanks to [Colt Steele](https://github.com/Colt), as this project has been developed in the framework of *The Ultimate MySQL Bootcamp: Go from SQL Beginner to Expert* course.
