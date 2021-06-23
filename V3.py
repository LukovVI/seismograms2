import os
from PIL import Image, ImageDraw #Подключим необходимые библиотеки.

kokoko = []
kakaka = []

def rol(j, i, pix):
    p = 0
    for k, z in list(([1, 0], [0, -1], [-1, 0], [0, 1])):
        if pix[j + k, i + z][0] == 0:
            p += 1
    return p

def bfs(j, i, pix, draw):
    global kokoko
    l = 1
    visit = [i * 4000 + j]
    chek = [[j, i]]
    while chek:
        q = chek.pop()
        p = 0
        for k, z in list(([1, 0], [0, -1], [-1, 0], [0, 1])):
            if pix[q[0] + k, q[1] + z][0] in [0, 100]:
                p += 1
        if p >= 3:
            for k, z in list(([1, 0], [0, -1], [-1, 0], [0, 1])):
                if pix[q[0] + k, q[1] + z][0] == 0 and (q[1]+z) * 4000 + q[0]+k not in visit:
                    visit.append((q[1]+z) * 4000 + q[0]+k)
                    chek.append([q[0]+k, q[1]+z])
            kokoko[q[1]//330] += 1
            draw.point((q[0], q[1]), (100, 0, 0))
            l += 1
    return l

def smallchek(x, y, pix, lim):
    p = 0
    for i in range(x, x+10):
        for j in range(y, y+10):
            if pix[i, j][0] == 0:
                p += 1
    return p > lim

def smallchek_(x, y, pix, lim):
    global kakaka
    p = 0
    for i in range(x, x+10):
        for j in range(y, y+10):
            if pix[i, j][1] == 0:
                if j//330 == 6:
                    j -= 100
                kakaka[j // 330] += 1
                if pix[i, j][0] == 0:
                    p += 1
    return p > lim

def all(nam):
    image1 = Image.open(os.getcwd() + "\\" + nam + ".png")
    image = image1.convert("RGB")
    draw = ImageDraw.Draw(image)
    width = image.size[0]
    height = image.size[1]
    pix = image.load()

    #bw(height, width, pix, draw)
    gran = 95


    for i in range(5, height - 20, 5):
        for j in range(81, width - 10, 5):
            if i % 10 == 5 and j % 10 == 1:
                if smallchek_(j, i, pix, gran):
                    for i1 in range(10):
                        y = i + i1
                        for j1 in range(10):
                            x = j + j1
                            if pix[x, y][0] == 0:
                                if rol(x, y, pix) >= 3:
                                    draw.point((x, y), (100, 0, 0))
                                    l = bfs(x, y, pix, draw)
                                    print(l, end=" ")
            else:
                if smallchek(j, i, pix, gran):
                    for i1 in range(10):
                        y = i+i1
                        for j1 in range(10):
                            x = j+j1
                            if pix[x, y][0] == 0:
                                if rol(x, y, pix) >= 3:
                                    draw.point((x, y), (100, 0, 0))
                                    l = bfs(x, y, pix, draw)
                                    print(l, end = " ")
    for i in range(6):
        kakaka[i] -= 1650
    print()
    S = 7751700
    s = 1291950
    plotV2 = list((kakaka[i]-kokoko[i])/(s-kokoko[i]) for i in range(6))
    plotV2.append((sum(kakaka)-sum(kokoko))/(S-sum(kokoko)))
    print(nam)
    time = list(["0-2", "2-4", "4-6", "6-8", "8-10", "10-12", "0-12"])
    for p in range(7):
        print(time[p] + "\t\t{0:.5f}".format(plotV2[p]))
    del draw

def main():
    global kokoko
    global kakaka
    for i in list(map(lambda x: x[0:-4], list(filter(lambda x: x.endswith(".png"), os.listdir())))):
        kokoko = [0, 0, 0, 0, 0, 0]
        kakaka = [0, 0, 0, 0, 0, 0]
        all(i)
    input("нажмине Enter для закрытия консоли")

if __name__ == '__main__':
    main()


