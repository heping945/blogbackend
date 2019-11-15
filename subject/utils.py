import time
import random
import hashlib


# 计算文件的md5
def getFileMd5(file):
    md5Obj = hashlib.md5()
    for chunk in file.chunks():
        md5Obj.update(chunk)
    return md5Obj.hexdigest()


# 检测文件类型
# 备用  用于 Filefield的md格式文件验证
def judgeFileType(file):
    ext = file.split('.')[-1]
    MdType = "md"
    if ext == MdType:
        return True
    return False



def rename(file):
    times = time.strftime('%Y%m%d%H%M%S')
    ran = random.randint(0, 1000)
    name = "{}-{}".format(times, ran)
    return name
