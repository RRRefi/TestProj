import subprocess
import pytest
from base.public import filePath

if __name__=='__main__':
    fileName='test_demo.py'
    TestCase = filePath('test_case', fileName)
    markCase ='-m'+'smoke'

    pytest.main(["-s", "-v", TestCase,
                 "--alluredir", "report/result", "--junit-xml", "report/result.xml", "--clean-alluredir",
                 "--durations=0"])

    #allure生成报表,并启动程序
    subprocess.call('allure generate report/result/ -o report/html --clean', shell=True)
    subprocess.call('allure open report/html', shell=True)