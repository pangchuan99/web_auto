
import json
import websocket


def send(url,data):
    '''websocket建立连接接收消息'''
    ws = websocket.create_connection(url)              # 创建连接
    # ws.send(json.dumps(data))   # json转化为字符串，必须转化
    results = []
    while True:
        receive = ws.recv()    # 服务器响应数据
        results.append(json.loads(receive))

    ws.close()
    return results

url = "ws://123.207.136.134:9010/ajaxchattest"
data={

}
a1=send(url,data)
print("s f sf ",a1)











