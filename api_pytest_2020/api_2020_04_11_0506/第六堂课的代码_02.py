import requests


def qq_get(key, qq):
    url = "http://japi.juhe.cn/qqevaluate/qq"
    querystring = {
        "key": key,
        "qq": qq
    }
    r = requests.get(url, params=querystring)
    print(r.text)
    return r


def test_qq_1():
    '''用例描述：qq号码-1.必填项key,输入正确keyid,请求成功'''

    r = qq_get(key="8dbee1fcd8627fb6699bce7b986adc45",
               qq="12345678")
    assert r.json()["error_code"] == 0
    assert r.json()["reason"] == "success"


def test_qq_2():
    '''用例描述： qq-2.必填项key为空，请求失败，提示：KEY ERROR'''
    r = qq_get(key="",
               qq="12345678")
    assert r.json()["error_code"] == 10001
    assert r.json()["reason"] == "KEY ERROR!"


# qq_get("8dbee1fcd8627fb6699bce7b986adc45",12345678)