import os
from PIL import Image, ImageDraw #Подключим необходимые библиотеки.

kokoko = []
kakaka = []

def bw(height, width, pix, draw, factor = 0):
    for i in range(width):
        for j in range(height):
            a = pix[i, j][0]
            b = pix[i, j][1]
            c = pix[i, j][2]
            if a + b + c > (((255 + factor) / 2) * 3):
                draw.point((i, j), (255, 255, 255))
            elif a + b + c <= (((255 + factor) / 2) * 3):
                draw.point((i, j), (0, 0, 0))
            else:
                print(i, j, a, b, c)

def rol(j, i, pix):
    p = 0
    for k, z in list(([1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1], [0, 1])):
        if pix[j + k, i + z][0] == 0:
            p += 1
    return p

def bfs(j, i, pix, draw):
    global kokoko
    l = [[j, i]]
    visit = [i * 4000 + j]
    chek = [[j, i]]
    while chek:
        q = chek.pop()
        p = 0
        for k, z in list(([1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1], [0, 1])):
            if pix[q[0] + k, q[1] + z][0] in [0, 100]:
                p += 1
        if p >= 5:
            for k, z in list(([1, 0], [0, -1], [-1, 0], [0, 1])):
                if pix[q[0] + k, q[1] + z][0] == 0 and (q[1]+z) * 4000 + q[0]+k not in visit:
                    visit.append((q[1]+z) * 4000 + q[0]+k)
                    chek.append([q[0]+k, q[1]+z])
            kokoko[q[1]//330] += 1
            draw.point((q[0], q[1]), (100, 0, 0))
            l.append([q[0], q[1]])
    return [len(l), l]

def drawer(l, draw):
    for q in l:
        draw.point(q, (200, 0, 100))

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

def plot2(pix, width, t):
    h2 = 0
    all2 = 0
    for i in range(81, width - 11):
        for j in range(t * 330, (t + 1) * 330):
            if pix[i, j][2] in [0, 255]:
                all2 += 1
            if pix[i, j][2] == 0:
                h2 += 1
    return h2/all2, all2, h2

def plot12(pix, width):
    plot_12_2 = []
    h12 = 0
    all12 = 0
    for i in range(6):
        pl2 = plot2(pix, width, i)
        plot_12_2.append(pl2[0])
        all12 += pl2[1]
        h12 += pl2[2]
    plot_12_2.append(h12/all12)
    return plot_12_2



def all(nam):
    # mode = int(input('mode:')) #Считываем номер преобразования.
    image1 = Image.open(os.getcwd() + "\\" + nam + ".png") #Открываем изображение.
    image = image1.convert("RGB")
    draw = ImageDraw.Draw(image) #Создаем инструмент для рисования.
    width = image.size[0] #Определяем ширину.
    height = image.size[1] #Определяем высоту.
    pix = image.load() #Выгружаем значения пикселей.

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
                                if rol(x, y, pix) >= 5:
                                    draw.point((x, y), (100, 0, 0))
                                    le, l = bfs(x, y, pix, draw)
                                    if le >= 200:
                                        print(le, end=" ")
                                        # drawer(l, draw)
            else:
                if smallchek(j, i, pix, gran):
                    for i1 in range(10):
                        y = i+i1
                        for j1 in range(10):
                            x = j+j1
                            if pix[x, y][0] == 0:
                                if rol(x, y, pix) >= 5:
                                    draw.point((x, y), (100, 0, 0))
                                    le, l = bfs(x, y, pix, draw)
                                    if le >= 200:
                                        print(le, end = " ")
                                        #drawer(l, draw)
    for i in range(width):
        if pix[i, 10][1] == 0:
            g = 0
            for j in range(5, height):
                if pix[i, j][1] == 0:
                    g += 1
                else:
                    break
            if g > height-100:
                for j in range(height):
                    draw.point((i, j), (0, 0, 100))
    fin = os.getcwd() + "\\final\\"
    if not os.path.exists(fin):
        os.mkdir(fin)
    image.save(fin + nam + "_final.png")
    for i in range(6):
        kakaka[i] -= 1650
    print()
    plot = plot12(pix, width)
    S = 7751700
    s = 1291950
    plotV2 = list((kakaka[i]-kokoko[i])/(s-kokoko[i]) for i in range(6))
    plotV2.append((sum(kakaka)-sum(kokoko))/(S-sum(kokoko)))
    print(nam)
    time = list(["0-2", "2-4", "4-6", "6-8", "8-10", "10-12", "0-12"])
    for p in range(7):
        print(time[p] + "\t\t{0:.5f}".format(plot[p]))
    print()
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


