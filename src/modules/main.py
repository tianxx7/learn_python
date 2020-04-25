from modules.utils import get_sum
from modules.class_utils import *
# 多次import 后面会覆盖前面,utils.py中的print(get_sum(1, 4))只执行一次
# from modules.utils import get_sum

print(get_sum(1, 2))

encoder = Encoder()
decoder = Decoder()

print(encoder.encode('abcde'))
print(encoder.encode('edcba'))