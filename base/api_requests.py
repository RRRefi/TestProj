import requests
# 从base.log导入全局logger，而不是错误的Logger类
from base.log import logger
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class ApiRequest(object):
    def __init__(self):
        pass

    """封装http请求,根据实际情况传参"""
    def send_requests(self, method, url, data=None, params=None, headers=None, cookies=None, json=None, files=None,
                      auth=None, timeout=None, proxies=None, verify=False, cert=None):
        # 禁用SSL证书验证verify=False
        res = requests.request(method=method, url=url, data=data, params=params, headers=headers, cookies=cookies,
                              json=json, files=files, auth=auth, timeout=timeout, proxies=proxies, verify=verify,
                              cert=cert)
        logger.debug(f"请求响应: {res}")
        return res
    
    