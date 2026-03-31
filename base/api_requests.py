import requests #导入request库
from base.log import logger

import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)#防警告

class Apirequest(object):
    def __init__(self):
        pass




    
    def send_requests(self, method, url, data=None, params=None, headers=None, cookies=None, 
                      json=None, files=None, auth=None, timeout=None, proxies=None, 
                      verify=False, cert=None):
        res = requests.request(method=method, url=url, data=data, params=params, headers=headers, 
                              cookies=cookies, json=json, files=files, auth=auth, timeout=timeout, 
                              proxies=proxies, verify=verify, cert=cert) #调用requests库的request功能，用传进来的参数进行http请求
        
    
    