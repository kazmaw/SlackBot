# SlackBot
This is helloworld slack bot.

## Precondition
- python3.6.3 is installed

## How to use
First of all, clone this repository
```
$ git clone git@github.com:kazmaw/SlackBot.git
```
or 
```
$ git clone https://github.com/kazmaw/SlackBot.git
```

Then, install libraries
```
$ pip install -r requirements.txt
```
(You might need to add `sudo` at the top.)

Rename `setting-sample.toml` to `setting.toml`, and type the following.
Additionally, you have to get api_token of slack API.
Refer to [Slack API 推奨Tokenについて](https://qiita.com/ykhirao/items/3b19ee6a1458cfb4ba21)
The api_token which you got from slack API console is needed to written to `setting.toml`.
After writting api_token, you do the following to get bot_id.
```
python print_bot_id.py
```
Now, you've got a bot id. So, write it down to ``setting.toml``, as well.

Finally, you can run the bot by the following.
```
python src/starterbot.py
```
execute server and you can use slack bot sample.

## Reference
### Set environment for python
[Pythonの仮想環境構築(2017年版) pyenvとpyenv-virtualenvとvirtualenvとvirtualenvwrapperとpyvenvとvenv](https://qiita.com/maskedw/items/aaa2fd7abfd493cf2820)
[Mac(Homebrew)でPython(pyenv/virtualenv)開発環境を作る](https://qiita.com/its/items/24f8b20aa2106819dfb3)

### Slack Bot
[inokappa/slack_bot-python](https://github.com/inokappa/slack_bot-python/blob/master/pika.py)
[Slack API 推奨Tokenについて](https://qiita.com/ykhirao/items/3b19ee6a1458cfb4ba21)
[How to Build Your First Slack Bot with Python](https://www.fullstackpython.com/blog/build-first-slack-bot-python.html)
