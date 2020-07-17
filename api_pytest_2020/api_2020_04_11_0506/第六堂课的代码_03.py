import requests


def test_qq_1():
    '''用例描述：qq号码-1.必填项key,输入正确keyid,请求成功'''
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


def test_qq_2():
    '''用例描述： qq-2.必填项key为空，请求失败，提示：KEY ERROR'''
    url = "http://japi.juhe.cn/qqevaluate/qq"
    querystring = {
        "key": "",
        "qq": "12345678"
    }
    r = requests.get(url, params=querystring)
    print(r.text)

    error_code = r.json()["error_code"]
    reason = r.json()["reason"]

    assert error_code == 10001
    assert reason == "KEY ERROR!"
