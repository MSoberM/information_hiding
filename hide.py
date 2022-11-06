import numpy
import random
from PIL import Image
from numpy.lib.npyio import load

# pixel = im.getpixel((w,h))
# im.putpixel((w,h)(a,b,c))
# RGB一样，8位，0-255
# 128*128  索引14位  1位校验 1位信息  共两个pixel来存放一个水印的二值像素
# bmp为720*480 平均下来 一个bmp放6*4个二值像素 900帧 共放21600个
# 默认255，255，255白色

# randlist 随机顺序（水印隐藏时的像素点位置）
arr = list(range(0, 128 * 128))
random.shuffle(arr)
randlist = []
for i in range(0, 128 * 128):
    randlist.append((int(arr[i] / 128), arr[i] % 128))

# hidex：水印二值数组
hidex = load("./save_bmtx.npy")
n = 0
nn = 0

randomseqx = numpy.load("./randomseq_x.npy")
randomseqy = numpy.load("./randomseq_y.npy")


# 偶校验位r
def getcheck(num):
    r = 0
    while num > 0:
        r ^= num % 2
        num = int(num / 2)
    return r


# randomseqx[nn]在载体中嵌入的偏移位置
# (x,y)该帧所隐藏水印信息坐标,hidex[x,y]该点二值
# info
# num1
for k in range(1, 901):
    s = "./rawbmp/" + str(k) + ".bmp"
    im = Image.open(s)
    for i in (60, 180, 300, 420, 540, 660):
        for j in (60, 180, 300, 420):
            (x, y) = randlist[n]
            n = (n + 1) % (128 * 128)
            info = (x * 128 + y)*2 + hidex[x, y]
            info = info * 2 + getcheck(info)
            num1 = int(info / 256)
            num2 = info % 256
            im.putpixel((i + randomseqx[nn], j + randomseqy[nn]), (num1, num1, num1))
            im.putpixel((i + 1 + randomseqx[nn], j + 1 + randomseqy[nn]), (num2, num2, num2))
            nn = (nn + 1) % 80

    im.save("./hidebmp2/" + str(k) + ".bmp")
    im.close()
    print(k)
