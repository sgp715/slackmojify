# Slackmojify

## Description
We all know how awesome emojis are. They can lighten the mood :laughing: or start a conversation . Many people believe they are the :key: to any good relationship. And some have even gone as far as to say they are the windows to the soul :eyes:. I'm not sure if all of that is true. But, I do believe that they make Slack a whole lot more entertaining. So, its awesome that Slack let's you add custom emojis. But, sometimes it can be annoying figuring out how to compress an image to just the right amount so it meets Slack's custom emoji requirements. Slackmojify is a python package that can be used as a CLI to easily compress an image so that it is easy to upload as a custom emoji to Slack.

## Rules of The Duel
Images can be JPG, GIF, or PNG, up to 128 pixels in width and height, and a maximum 64KB file size. We recommend using a small, square picture, as Slack will resize the image to fit neatly inside a row of text. (not yet supporting GIF's)


## Install
* Developed in Python 3
* Make sure you have pip3
* Install dependencies
```
$ pip3 install -r requirements.txt
```
* Pull submodules
```
$ git submodule update
```
* If you want to run it without specifying python, simply give it executable perms
```
$ chmod +x slackmojify.py
```
* Then either add its location to your path or add somewhere in your existing path
* Or do something like alias...you know the drill


## Getting started
* To see the usage description
```
$ python3 slackmojify.py -h
```
* To compress an image run (where <path/to/image> is the image you want to compress)
```
$ python3 slackmojify.py <path/to/image>
```
* You can also specify where you would like to save the image
```
$ python3 slackmojify.py <path/to/image> -s <location/to/save/image>
```
* Coming soon: generated a gif from images in <path/to/folder>
```
$ python3 slackmojify.py <path/to/folder> -s <location/to/save/image>
