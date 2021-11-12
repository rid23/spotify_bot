
import sys
from time import sleep
import requests


	
def solve2(url):
	sitekey = "6LeO36obAAAAALSBZrY6RYM1hcAY7RLvpDDcJLy3"
	api_key = "56f31606ba22e5c37454dbd6f213354c"

	form = {
	"method":"userrecaptcha",
	"googlekey":sitekey,
	"key":api_key,
	"pageurl":url,
	"json":1
	}

	response = requests.post('http://2captcha.com/in.php',data=form)
	request_id = response.json()['request']

	url = f"http://2captcha.com/res.php?key={api_key}&action=get&id={request_id}&json=1"

	status = 0
	while not status:
	    res = requests.get(url)
	    if res.json()['status']==0:
	        sleep(3)
	    else:
	        requ = res.json()['request']

	        return requ
	        status = 1



