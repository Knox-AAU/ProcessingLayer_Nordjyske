import requests
from exceptions import HttpException

GET_TIMEOUT = 5

def fetch_tokens(api_url, limit, offset):
    tokens = []
    word_ratios = http_get(api_url + 'word-ratios?limit=' + str(limit) + '&offset=' + str(offset))
    for word_ratio in word_ratios:
        for a in range(word_ratio['amount']):
            tokens.append(word_ratio['word'])
    return tokens

def http_get(url):
    r = requests.get(url, timeout=GET_TIMEOUT)
    if r.status_code != 200:
        raise HttpException('Post. Code: ' + str(r.status_code) + ' || Response: ' + r.text)
    else:
        return r.json()
    