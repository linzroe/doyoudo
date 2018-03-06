import requests
import sys
import io

#替换自己的个人信息页面，并更换成自己的cookie
url = 'http://www.doyoudo.com/users/4730/edit' 
 
cookies = {
	    'accept-encoding': 'gzip, deflate',
	    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
	    'Referer': 'http://www.doyoudo.com/users/4730/bill', #替换自己的个人信息页面
	    'cookie': '_ga=GA1.2.839643652.1520320634; _gid=GA1.2.1094149315.1520320634; gr_user_id=0b846428-acb3-4666-8240-be3efb32457b; gr_session_id_bacc8fe2f11f198e=6c125241-dcdb-4a1e-aff0-26145cc7cbbe; gr_cs1_6c125241-dcdb-4a1e-aff0-26145cc7cbbe=user%3A%E5%8F%8C%E6%9C%A8_4730; _doyoudo_session=OFZVazF0NGlPNWtaSGZ2bkVVUDFnbUpZQVdnZ3RYVEFuRjVRMXEwcEk0bHRQWkIwSXh6dWJNbE44aHgrVFRMcUdxY1JuVlNySlFHK2hRM2xuYUdNMDhsUGtXdGlQaTNVMlVFaC9uSlZIdTFHNGFHTUs4VUVSSUs1SFZPdzJXL3VZK212bm56S1NBOVVhZlZIVTZ5REY5OTFoUVdlOUdPdU1EMHZKamIreXJPMER5bzRmcnJTS0h1a2ZUelo1aXRCYVZ1a2JFc3NwcjlVWGwzMk9aQm5Sd3NBclFDeGFsQkdJZ2VVUlNDNzgwRkkwd0gyRkl6SkRCU2ZuT0FVUWFudUt6VGhhSkpYaHd0ZmV4Rk02K0t6QTBYVnl3VC9Qc2piSDJ2QXVHVHpMcEU9LS0xcTBHRTIwZE5zaXJxL2FEczJrUmdnPT0%3D--940a468fd773567de7465b6479f00b11eb4c9390; _gat=1',
	}

headers = {'User-agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'}

resp = requests.get(url, headers = headers, cookies = cookies)
body = resp.content.decode('utf-8')   
ccc=body[body.index('class="myinfo-score">')+21:body.index('<img class="myinfo-icecream"')-7]
print('当前雪糕数:'+ccc)
