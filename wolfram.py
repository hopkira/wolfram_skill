#
# Wolfram Mathmatica API Python Client
#
import requests
from secrets import *
    req_dict = {}
    req_dict['units'] = args.get('units')
    req_dict['geolocation'] = args.get('geolocation')
    if args.get('appid'):
        req_dict['appid'] = args.get('appid')
    else:
        return {'result':'Query not authorised'}
    # Are we in a conversation? If so then direct to correct host
    # and the right conversation
    url_base = "http://api.wolframalpha.com/v1/conversation.jsp"
    if args.get('host'):
        url_base = args.get('host')
        req_dict['conversationID'] = args.get('conversationID')
    if args.get('i'):
        req_dict['i'] = args.get('i')
    else"
        return {"result":"I did not hear a query"}
    try:
        r = requests.get(url_base, params=req_dict)
        return r.json()
    except Exception:
        return {"result":"I do not know the answer"}

if __name__ == '__main__':
    empty_dict={}
    main(empty_dict)