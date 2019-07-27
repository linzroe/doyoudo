import requests

url = "http://www.doyoudo.com/api/user/sign/"

headers = {
    'host': "www.doyoudo.com",
    'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0",
    'accept': "application/json, text/plain, */*",
    'accept-language': "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
    'accept-encoding': "gzip, deflate",
    'referer': "http://www.doyoudo.com/chatroom",
    'token': "1ff30009-3779-4469-a8de-c2247a82b887",
    'connection': "keep-alive",
    'cookie': "dyd-token=xxxxxxxxxxxxxxxxxxxxxxxxx",
	# cookie 把上面的Cookie替换成自己的,然后每天定时跑这个脚本就好了
    'content-length': "0"
    }

response = requests.request("POST", url, headers=headers)

print(response.text)