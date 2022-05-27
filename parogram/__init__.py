# Parogram Class
import requests

# Telegram API URL
url = 'https://api.telegram.org/'

class Parogram:    

    def __init__(self,token,parse_mode=None):
        self.token = token
        self.parse_mode = parse_mode

    # Basic Methods Of Telegram Bot API

    def send_message(self,chat_id, text, parse_mode=None):

        parse_mode = self.parse_mode if parse_mode is None else parse_mode
    
        full_url = f"{url}bot{self.token}/sendmessage?chat_id={chat_id}&text={text}&parse_mode={parse_mode}"

        requests.get(full_url)