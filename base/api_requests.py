#发送请求模块

import requests #导入request库
from base.log import logger

import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)#防警告

class Apirequest(object):
    def __init__(self):
        pass


#method：方法，如get、post，写入后request变成对应功能，就不用再request.get（）
#url：接口地址
#data：表单格式参数
#params：url后面拼接的参数

    
    def send_requests(self, method, url, data=None, params=None, headers=None, cookies=None, 
                      json=None, files=None, auth=None, timeout=None, proxies=None, 
                      verify=False, cert=None):
        res = requests.request(method=method, url=url, data=data, params=params, headers=headers, 
                              cookies=cookies, json=json, files=files, auth=auth, timeout=timeout, 
                              proxies=proxies, verify=verify, cert=cert) #调用requests库的request功能，用传进来的参数进行http请求
        logger.debug(res) #响应结果发到日志

        return res#返回结果给调用方

if __name__ == '__main__':#若模块被直接执行__name__就会变成__main__,若是被引用__name__就是它自身的名字
    pass                  #所以这里面应写入被引用时不想执行的内容，即只有直接运行该模块时才执行的内容


        
    
    