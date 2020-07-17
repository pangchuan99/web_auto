import pytest

# 期望结果都是固定的一个
# username "", 123, "aaaaaa"
# psw      "", 234,  "bbbb"


@pytest.mark.parametrize("psw", ["", 234, "bbbb"])#然后在执行这个
@pytest.mark.parametrize("username", ["", 123, "aaaaaa"])#先执行这个 有里到外
def test_eval(username, psw):
    print("\n账号和密码组合：%s, %s"%(username, psw))
