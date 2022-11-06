# 二值数组转二值图像

import numpy
from PIL import Image

bmtx = numpy.load("./save_bmtx.npy")
for i in range(bmtx.shape[0]):
    for j in range(bmtx.shape[1]):
        if bmtx[i, j] == 1:
            bmtx[i, j] = 255
img = Image.fromarray(bmtx)
img.save("./save_bmtx_png.png")
