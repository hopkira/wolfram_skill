#
# Wolfram Mathmatica API Python Client
#
import requests
from secrets import *

def main():
    s = None
    base_url = "http://api.wolframalpha.com/v1/conversation.jsp"
    append_url = "/api/v1/conversation.jsp"
    conversationID = None
    while True:
        i = input("\nWhat is your question?\n")
        if i == "quit": break
        response = ask_question(i, base_url, conversationID, s)
        if "conversationID" in response:
            conversationID = response["conversationID"]
        if "host" in response:
            base_url = "http://" + response["host"] + append_url
        if "s" in response:
            s = response["s"]
        if "result" in response:
            print("\n",response["result"],"\n")

def ask_question(question_string, base_url, conversationID = None, s = None):
    req_dict =  {}
    req_dict ['i'] = question_string
    req_dict['geolocation'] = geolocation
    req_dict['appid'] = appid
    req_dict['units'] = "metric"
    req_dict['host'] = base_url
    if conversationID is not None:
        req_dict['conversationID'] = conversationID
    if s is not None:
        req_dict ['s'] = s
    # Are we in a conversation? If so then direct to correct host
    # and the right conversation
    r = requests.get(base_url, params = req_dict)
    # print(r.json())
    result = r.json()
    if 'error' in result :
        result['result'] = "I do not know the answer"
    if "Wolfram" in result['result']:
        result['result'] = "My name is K9. That question is irrelevant."
    # print(result)
    return result
    #except Exception:
    #    req_dict['result'] = "I do not know the answer"
    #    return req_dict

if __name__ == '__main__':
    main()