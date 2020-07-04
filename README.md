# README

How to use env vars efficiently in your severless & python project.

One of the technique about Serverless Framewrok (sls) that I often see "Use <stage>.yml to manage stage specific configuration".

Personally, I'm a bit skeptical about such as that separate template only for stage separation (e.g prod.yml).

(Template file separation should be used to separate the system component. Don't need to use for handling stage-specific variable.)

Here indicates another approach.

# About this example

Shows system architecture as below;

> lambda(MyJobFunction) -> sqs(my-queue) -> lambda(MyConsumerFunction)

MyJobFunction send messages to SQS queue. MyConsumerFunction receives and processes messages from queue.

MyConsumerFunction notify a message (the message-data is based received from queue) to slack.

# Important point

I'll write sometime in english...

see also: [Serverless Framework & Python 環境変数の使い方](https://www.practicalcloudpython.com/2020/07/04/30/)

# Why I've published this code?

The serverless world is awesome. But I feel many engineers have confused.

What should serverless-beginners choose (and use) techniques to make themselves enhancement? I'm also confused to feel the same too. It seems the information is few.

So I publish techniques I've knew that based on my work experience.

I wish serverless-funs able to step to the next.