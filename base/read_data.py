import xlrd
from base.public import filePath
from ruamel import yaml
# ✅ 关键修复：导入全局logger实例，而不是Logger类
from base.log import logger

class ReadYaml:
    """初始化文件"""
    def __init__(self, *file_name):
        #传参相对路径+文件名
        self.file = file_name
        self.all_data = None

    def read_data(self):
        """返回文件数据"""
        #读取文件
        with open(filePath(*self.file), "r", encoding="utf-8") as docs:
            try:
                # ✅ 修复yaml弃用警告，使用标准safe_load
                self.all_data = yaml.safe_load(docs)
            except yaml.YAMLError as exc:
                print(exc)
        # ✅ 关键修复：使用全局logger实例，而不是Logger类
        logger.info("读取的文件数据:\n"+str(self.all_data))
        return self.all_data

# 读取excel表数据
class OperationExcel(ReadYaml):
    #获取shell表
    def get_shell(self):
        book = xlrd.open_workbook(filePath(*self.file))
        return book.sheet_by_index(0)

    #以列表形式读取传入文件的数据
    def get_excel_data(self):
        data = []
        for row in range(1, self.get_shell().nrows):
            row_value = self.get_shell().row_values(row)
            data.append(row_value)
        return data