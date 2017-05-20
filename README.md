# Slackmojify

## Description
We all know how awesome emojis are. They can lighten the mood :laughing: or start a conversation . Many people believe they are the :key: to any good relationship. And some have even gone as far as to say they are the windows to the soul :eyes:. I'm not sure if all of that is true. But, I do believe that they make Slack a whole lot more entertaining. So, its awesome that Slack let's you add custom emojis. But, sometimes it can be annoying figuring out how to compress an image to just the right amount so it meets Slack's custom emoji requirements. Slackmojify is a python package that can be used as a CLI to easily compress an image so that it is easy to upload as a custom emoji to Slack.

## Rules of The Duel
Images can be JPG, GIF, or PNG, up to 128 pixels in width and height, and a maximum 64KB file size. We recommend using a small, square picture, as Slack will resize the image to fit neatly inside a row of text.

## Install
* Install from pip3
```
$ pip3 install slackmojify
```

## Getting started
* The pip install should configure slackmojify to work as a command line utility so you should be able to run it directly in terminal
```
$ slackmojify ...
```
* To see the usage description
```
$ slackmojify.py -h
```
* To compress an image run (where <path/to/image> is the image you want to compress)
```
$ slackmojify.py <path/to/image>
```
* You can also specify where you would like to save the image
```
$ slackmojify.py <path/to/image> -s <location/to/save/image>
```
* Generate a gif from images in the directory <path/to/folder> (images must be same size)
```
$ slackmojify.py <path/to/folder> -s <location/to/save/image>
```

# Example
* Find an image that you want to slackmojify
![Picking](/assets/picking.gif)
* Open a terminal session specify the image and where you want to save it
![Running](/assets/run.gif)
* Done :wink:
![Done](/assets/done.gif)
