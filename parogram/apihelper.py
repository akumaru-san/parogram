import parogram
import requests

def send_request(token, method_name, http_method='get', params=None, files=None):
    request_url = parogram.url + 'bot' +  token + method_name
    result = requests.request(http_method, request_url, params=params, files=files)

    if result.status_code != 200:
        raise ApiException(method_name, result)
    
    try:
        result_json = result.json()
        if not result_json['ok']:
            raise Exception()
    except:
        raise ApiException(method_name, result)

    return result_json['result']

class ApiException(Exception):
    def __init__(self, func_name, result):
        super(ApiException,self).__init__(f"{func_name} failed. Result: {result}")
        self.func_name = func_name
        self.result = result