# 水印转二值数组

import numpy
from PIL import Image

image = Image.open("./seu.png")
image = image.convert("L")  # 灰度图像
# image.save("./grey.png")
bmtx = numpy.array(image)  # 二维数组

for i in range(bmtx.shape[0]):
    for j in range(bmtx.shape[1]):
        # print(bmtx[i,j]
        if bmtx[i, j] > 127:
            bmtx[i, j] = 1
        else:
            bmtx[i, j] = 0
numpy.save("./save_bmtx", bmtx)
# load_arr=numpy.load("./save_bmtx")
