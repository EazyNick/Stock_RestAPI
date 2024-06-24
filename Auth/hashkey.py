# def hashkey(datas):
#   PATH = "uapi/hashkey"
#   URL = f"{url_base}/{path}"
#   headers = {
#     'content-Type' : 'application/json',
#     'appKey' : app_key,
#     'appSecret' : app_secret,
#     }
#   res = requests.post(URL, headers=headers, data=json.dumps(datas))
#   hashkey = res.json()["HASH"]

#   return hashkey