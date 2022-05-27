import apihelper
import requests

# Telegram API URL
url = 'https://api.telegram.org/'

# Parogram Class

class Parogram:    

    def __init__(self,token,parse_mode=None):
        self.token = token
        self.parse_mode = parse_mode

    # Basic Methods Of Telegram Bot API

    def get_me(self):
        result = apihelper.send_request(self.token, "getme")

        return result

    def send_message(self, chat_id, text, disable_web_page_preview=None,parse_mode=None, reply_to_message_id=None, reply_markup=None):

        parse_mode = self.parse_mode if parse_mode is None else parse_mode
    
        full_url = f"{url}bot{self.token}/sendmessage?chat_id={chat_id}&text={text}&parse_mode={parse_mode}&reply_to_message_id={reply_to_message_id}&disable_web_page_preview={disable_web_page_preview}&reply_markup={reply_markup}"

        requests.get(full_url)

