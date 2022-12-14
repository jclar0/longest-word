# longest-word

A Python script that, when run, will tell you the longest word that can be displayed on a seven-segment display. I won't spoil it here though. This is based off [a video](https://www.youtube.com/watch?v=zp4BMR88260) by Tom Scott, however, he wrote it in JavaScript and I wrote it in Python. It's not particularly fast or impressive.

For the purpose of a seven-segment display, I have chosen to exclude any word with the letters below. You can easily modify the script yourself if you feel I'm being too strict (or too lenient) on which letters work on a seven-segment display:

```python
# Define a regular expression to exclude words with letters that cannot be displayed on a seven segment display
regex = re.compile(r'[gikmoqsvwxz]')
```

You can also use a different dictionary if you feel like. I'm using the same file as Tom Scott - [words.txt by dwyl](https://github.com/dwyl/english-words/blob/master/words.txt)