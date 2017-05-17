# Slackmojify

## Description
We all know how awesome emojis. They can lighten the mood :laughing: or start a conversation . Many people believe they are the :key: to any good relationship. And some have even gone as far as to say they are the windows to the soul :eyes:. I'm not sure if all of that is true. But, I do believe that they make Slack a whole lot more entertaining. So, its awesome that Slack let's you add custom emojis. But, sometimes it can be annoying figuring out how to compress an image to just the right amount so that you can upload them. Slackmojify is a python package that can be used as a CLI to easily compress an image so that it is easy to upload as a custom emoji to Slack.

## Rules of The Duel
Images can be JPG, GIF, or PNG, up to 128 pixels in width and height, and a maximum 64KB file size. We recommend using a small, square picture, as Slack will resize the image to fit neatly inside a row of text. (not yet supporting GIF's)


## Install
* Make sure you have pip
* Install dependencies
```
$ pip install -r requirements.txts
```

## Getting started
* Run
```
$ python3 slackmojify.py <path/to/image>
```
