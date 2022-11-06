import numpy
import random
from PIL import Image
from numpy.lib.npyio import load

randomseqx = numpy.load("./randomseq_x.npy")
randomseqy = numpy.load("./randomseq_y.npy")
nn = 0


def getcheck(num):
    r = 0
    while (num > 0):
        r ^= num % 2
        num = int(num / 2)
    return r


bmtx = numpy.zeros((128, 128))
for i in range(bmtx.shape[0]):
    for j in range(bmtx.shape[1]):
        bmtx[i, j] = 1

for k in range(601, 901):
    s = "./hidebmp2/" + str(k) + ".bmp"
    im = Image.open(s)
    for i in (60, 180, 300, 420, 540, 660):
        for j in (60, 180, 300, 420):
            pix1 = im.getpixel((i + randomseqx[nn], j + randomseqy[nn]))
            pix2 = im.getpixel((i + 1 + randomseqx[nn], j + 1 + randomseqy[nn]))
            nn = (nn + 1) % 80

            # 判断信息是否受损
            if not (pix1[0] == pix1[1] == pix1[2]) or not (pix2[0] == pix2[1] == pix2[2]):
                continue
            info = pix1[0] * 256 + pix2[0]
            if getcheck(info) == 1:
                continue
            info = int(info / 2)
            recover = info % 2
            info = int(info / 2)
            (x, y) = (int(info / 128), info % 128)
            bmtx[x, y] = recover
    im.close()
    print(k)

for i in range(bmtx.shape[0]):
    for j in range(bmtx.shape[1]):
        if bmtx[i, j] == 1:
            bmtx[i, j] = 255
img = Image.fromarray(bmtx)
img = img.convert("RGB")
img.save("./recover_last10s.png")
