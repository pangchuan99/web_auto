import requests

url = "http://japi.juhe.cn/qqevaluate/qq"
querystring = {
    "key": "8dbee1fcd8627fb6699bce7b986adc45",
    "qq": "12345678"
}
r = requests.get(url, params=querystring)
print(r.text)

error_code = r.json()["error_code"]
reason = r.json()["reason"]

assert error_code == 0
assert reason == "success"

conclusion = r.json()["result"]["data"]["conclusion"]
print(conclusion)