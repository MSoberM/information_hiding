# 索引序列的生成

import random
import numpy

arr = list(range(0, 80))
for i in range(0, 80):
    arr[i] -= 40

random.shuffle(arr)
numpy.save("./randomseq_x", arr)
random.shuffle(arr)
numpy.save("./randomseq_y", arr)
