# Bitly url shortener

This script generates a short link (bitlink) to your long link and also counts a number of clicks if given a bitlink.

### How to install

Python3 should be already installed. 
Then use `pip` (or `pip3`, if there is a conflict with Python2) to install dependencies:
```
pip install -r requirements.txt
```

Also you need to create ".env" file in the directiory with the script and set an environement variable BITLY_TOKEN, the value for that variable you can find if you register on [api.bitly.com](https://app.bitly.com/settings/api/), generate your token there and assign it to BITLY_TOKEN as a string with `export` as this: 

```export BITLY_TOKEN = 'sdfsdfsfs14324dsad'```

### Script execution example

The result of script execution is like this ![script execution example](https://bit.ly/3EvY8I2)

### Project Goals

The code is written for educational purposes on online-course for web-developers [dvmn.org](https://dvmn.org/).
