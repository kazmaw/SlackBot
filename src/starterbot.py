# -*- coding: utf-8 -*-
import time
from slackclient import SlackClient
import toml
import logging
import json

SETTING = toml.load(open('setting.toml'))

BOT_ID = SETTING['slack']['bot_id']
AT_BOT = '<@' + BOT_ID + '>'
EXAMPLE_COMMAND = SETTING['common']['example_command']

stream_log = logging.StreamHandler()
stream_log.setLevel(logging.DEBUG)
stream_log.setFormatter(logging.Formatter('%(asctime)s %(levelname)s %(message)s'))
logging.getLogger().addHandler(stream_log)
logging.getLogger().setLevel(logging.DEBUG)

slack_client = SlackClient(SETTING['slack']['api_token'])

def handle_command(command, channel):
  response = u'*' + EXAMPLE_COMMAND + u'* を付けてメッセージを送信してください'
  if command.startswith(EXAMPLE_COMMAND) or command.startswith(': ' + EXAMPLE_COMMAND):
    response = u'Hello world!として言えません。ごめんなさい。'
  slack_client.api_call(
    "chat.postMessage", 
    channel=channel,
    text=response,
    as_user=True
  )

def parse_slack_output(slack_rtm_output):
  logging.info(slack_rtm_output)
  output_list = slack_rtm_output
  if output_list and len(output_list) > 0:
    for output in output_list:
      if output and 'text' in output and AT_BOT in output['text']:
        return output['text'].split(AT_BOT)[1].strip().lower(), output['channel']
  return None, None

if __name__ == "__main__":
    READ_WEBSOCKET_DELAY = SETTING['common']['interval']
    if slack_client.rtm_connect():
        logging.info('bot を開始しました...')
        while True:
            command, channel = parse_slack_output(slack_client.rtm_read())
            if command and channel:
                handle_command(command, channel)
            time.sleep(READ_WEBSOCKET_DELAY)
    else:
        logging.warn('slack への接続に失敗しました.')

