#!/usr/bin/env python3

print('Rrr')

import requests  
import datetime

class BotHandler:

    def __init__(self, token):
        self.token = token
        self.api_url = "https://api.telegram.org/bot{}/".format(token)

    def get_updates(self, offset=None, timeout=30):
        method = 'getUpdates'
        params = {'timeout': timeout, 'offset': offset}
        resp = requests.get(self.api_url + method, params)
        result_json = resp.json()['result']
        return result_json

    def send_message(self, chat_id, text):
        params = {'chat_id': chat_id, 'text': text}
        method = 'sendMessage'
        resp = requests.post(self.api_url + method, params)
        return resp

    def get_last_update(self):
        get_result = self.get_updates()

        if len(get_result) > 0:
            last_update = get_result[-1]
        else:
            last_update = get_result[len(get_result)]

        return last_update
				
greet_bot = BotHandler('1295661558:AAHpKhyN7o5Pw2XM5uhaPKzgKqZXd_QzhuI')  
greetings = ('здравствуй', 'привет', 'ку', 'здорово')  
now = datetime.datetime.now()

print(now)

def main():  
    new_offset = None
    today = now.day
    hour = now.hour
	
    greet_bot.get_updates(new_offset)
	
    last_update = greet_bot.get_last_update()
	
    last_update_id = last_update['update_id']
    last_chat_text = last_update['message']['text']
    last_chat_id = last_update['message']['chat']['id']

    last_chat_name = last_update['message']['chat']['first_name']
	
    #greet_bot.send_message(last_chat_id, 'Добрый вечер, {}'.format(last_chat_text))

    lst = last_chat_text.split('+')
    print(int(lst[0]) + int(lst[1]))

    #greet_bot.send_message(last_chat_id, '{}'.format(lst[0]))

if __name__ == '__main__':  
    try:
        main()
    except KeyboardInterrupt:
        exit()		