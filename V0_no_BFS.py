import os
from PIL import Image, ImageDraw #Подключим необходимые библиотеки.

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

def main():
    name = ""
    for i in map(lambda x: x[0:-4], list(filter(lambda x: x.endswith(".png"), os.listdir()))):
        name = i
    image1 = Image.open(os.getcwd() + "\\" + name + ".png") #Открываем изображение.
    print(name)
    image = image1.convert("RGB")
    draw = ImageDraw.Draw(image) #Создаем инструмент для рисования.
    width = image.size[0] #Определяем ширину.
    height = image.size[1] #Определяем высоту.
    pix = image.load() #Выгружаем значения пикселей.


    gran = 80
    for i in range(0, width - 10, 5):
        for j in range(0, height - 10, 5):
            p = 0
            for i1 in range(10):
                for j1 in range(10):
                    if pix[i + i1, j + j1][0] == 0:
                        p += 1
            if p > gran:
                x = p
                n = list([j, j + 10, i, i + 10])
                for k in range(4):
                    while x > gran:
                        r = (n[1]-n[0]) * (n[3]-n[2]) * x / 100
                        if k == 0:
                            r1 = 0
                            if n[k] < 1:
                                break
                            for i3 in range(n[2], n[3]):
                                if pix[i3, n[k]-1][0] == 0:
                                    r1 += 1
                            t = (r + r1) *100/((n[1] - n[0] + 1) * (n[3] - n[2]))
                            if t > gran and r1 > (n[3] - n[2])/10:
                                x = t
                                n[k] -= 1
                            else:
                                break
                        if k == 1:
                            r1 = 0
                            if n[k] >= height-1:
                                break
                            for i3 in range(n[2], n[3]):
                                if pix[i3, n[k]+1][0] == 0:
                                    r1 += 1
                            t = (r + r1)*100/((n[1] - n[0] + 1) * (n[3] - n[2]))
                            if t > gran and r1 > (n[3] - n[2])/10:
                                x = t
                                n[k] += 1
                            else:
                                break
                        if k == 2:
                            r1 = 0
                            if n[k] < 1:
                                break
                            for i3 in range(n[0], n[1]):
                                if pix[n[k]-1, i3][0] == 0:
                                    r1 += 1
                            t = (r + r1)*100/((n[1] - n[0]) * (n[3] - n[2] + 1))
                            if t > gran and r1 > (n[1] - n[0])/10:
                                x = t
                                n[k] -= 1
                            else:
                                break
                        if k == 3:
                            r1 = 0
                            if n[k] >= width-1:
                                break
                            for i3 in range(n[0], n[1]):
                                if pix[n[k] + 1, i3][0] == 0:
                                    r1 += 1
                            t = (r + r1) * 100 / ((n[1] - n[0]) * (n[3] - n[2] + 1))
                            if t > gran and r1 > (n[1] - n[0])/10:
                                x = t
                                n[k] += 1
                            else:
                                break
                print(1)
                for i4 in range(n[2], n[3]):
                    for j4 in range(n[0], n[1]):
                        draw.point((i4, j4), (200, 0, 100))
                print(2)

    print(3)
    for i in range(80, 3991, 782):
        for j in range(0, 2000):
            draw.point((i, j), (0, 0, 100))
    print(4)
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

if __name__ == '__main__':
    main()

