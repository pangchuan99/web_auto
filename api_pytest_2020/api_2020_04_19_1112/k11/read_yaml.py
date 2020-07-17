import os
import yaml






def get_yaml_data(yamlpath):
    f = open(yamlpath, "r", encoding='utf-8')
    yamldata = f.read()
    print(yamldata)
    # print(type(yamldata))
    # yaml文件读取出来的是 str字符串类型的    需要进行转换成字典
    d = yaml.load(yamldata,Loader=yaml.FullLoader)
    print(d)
    f.close()#关闭
    # print(d["test_info_params"])
    # print(type(d))
    return d



if __name__ == '__main__':
    # 获取当前文件的上一层路径,上一层路径
    curpath = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    print(curpath)
    #然后在获取某一个文件的绝对路径
    yamlpath = os.path.join(curpath,"k12", "update_infoy11.yml")
    print(yamlpath)
    a = get_yaml_data(yamlpath)
    print("获取到的信息",a)


