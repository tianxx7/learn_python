import json

open("")

def get_sum(a, b):
    return a + b


#如果没有这一行,其他文件import时会执行下面代码
if __name__ == '__main__':
    print(get_sum(1, 3))