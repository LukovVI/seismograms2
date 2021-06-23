import os
import cv2
from PIL import Image, ImageDraw


def rol(x, y, pix):
    p = 0
    for i, j in list(([1, 0], [0, -1], [-1, 0], [0, 1])):
        if pix[x + i, y + j][0] == 0:
            p += 1
    return p


def bfs(x, y, pix, draw):
    l = [[x, y]]
    visit = [y * 2000 + x]
    check = [[x, y]]
    while check:
        q = check.pop()
        p = 0
        for i, j in list(([1, 0], [0, -1], [-1, 0], [0, 1])):
            if pix[q[0] + i, q[1] + j][0] in [0, 100]:
                p += 1
        if p >= 3:
            for i, j in list(([1, 0], [0, -1], [-1, 0], [0, 1])):
                if pix[q[0] + i, q[1] + j][0] == 0 and (q[1]+j) * 2000 + q[0]+i not in visit:
                    visit.append((q[1]+j) * 2000 + q[0]+i)
                    check.append([q[0]+i, q[1]+j])
            draw.point((q[0], q[1]), (100, 0, 0))
            l.append([q[0], q[1]])
    return [len(l), l]


def drawer(l, draw):
    for q in l:
        draw.point(q, (200, 0, 100))


def smallchek(x, y, pix, threshold):
    p = 0
    for i in range(x, x+10):
        for j in range(y, y+10):
            if pix[i, j][0] == 0:
                p += 1
    if p < threshold:
        return False
    for i in range(x, x+10):
        for j in range(y, y+10):
            if pix[i, j][0] == 0:
                if rol(i, j, pix) >= 3:
                    return list([i, j])
    return False


def plot2(pix, width, t):
    black2 = 0
    all2 = 0
    for i in range(81, width - 11):
        for j in range(t * 330, (t + 1) * 330):
            if pix[i, j][2] in [0, 255]:
                all2 += 1
            if pix[i, j][2] == 0:
                black2 += 1
    return black2/all2, all2, black2


def plot12(pix, width):
    plot_12_2 = []
    black12 = 0
    all12 = 0
    for i in range(6):
        pl2 = plot2(pix, width, i)
        plot_12_2.append(pl2[0])
        all12 += pl2[1]
        black12 += pl2[2]
    plot_12_2.append(black12/all12)
    return plot_12_2


def all(name):
    image1 = Image.open(os.getcwd() + "\\" + name + ".png")
    image = image1.convert("RGB")
    draw = ImageDraw.Draw(image)
    width = image.size[0]
    height = image.size[1]
    pix = image.load()

    threshold = 95
    for i in range(5, height - 10, 10):
        for j in range(5, width - 10, 10):
            check_point = smallchek(j, i, pix, threshold)
            if check_point:
                le, l = bfs(check_point[0], check_point[1], pix, draw)
                if le >= 200:
                    print(le, end = " ")
                    drawer(l, draw)
    for i in range(80, 3991, 782):
        for j in range(0, 2000):
            draw.point((i, j), (0, 0, 100))
    fin = os.getcwd() + "\\final\\"
    if not os.path.exists(fin):
        os.mkdir(fin)
    image.save(fin + name + "_final.png")
    print()
    plot = plot12(pix, width)
    print(name)
    time = list(["0-2", "2-4", "4-6", "6-8", "8-10", "10-12", "0-12"])
    for p in range(7):
        print(time[p] + "\t\t{0:.5f}".format(plot[p]))
    print()
    del draw


def main():
    for i in list(map(lambda x: x[0:-4], list(filter(lambda x: x.endswith(".png"), os.listdir())))):
        all(i)
    input("нажмине Enter для закрытия консоли")



if __name__ == '__main__':
    main()


