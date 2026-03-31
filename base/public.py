#系统路径库
import os
def filePath(*filename):

    return os.path.join(os.path.dirname(os.path.dirname(__file__)),
                        *filename
                        )
#将文件名和项目根目录（文件上一级base的上一级TestProj）拼接
#os.path.dirname上一级文件夹的路径
#os.path.join拼接
                        
