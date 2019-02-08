import cv2
import os

def read(log):
    open(log, "a")
    with open(log, "r") as f:
        return f.read().rstrip().split("\n")

def write(img_viewed, log):
    with open(log, "w") as f:
        for _ in img_viewed:
            f.write(_ + "\n")

def search(path):
    imgs = []
    for root, dirs, files in os.walk(path):
        for name in files:
            imgs.append(os.path.join(root, name))
        for name in dirs:
            imgs.append(os.path.join(root, name))
    return imgs

def view(path, log, screen, rate):
    img_viewed = read(log)
    imgs = search(path)
    i = 0
    while i < (len(imgs)):
        name = imgs[i]
        img = cv2.imread(name)
        if name in img_viewed or img is None:
            i += 1
            continue
        while len(img) >= screen[1] or len(img[0]) >= screen[0]:
            img = cv2.resize(img, (int(len(img[0]) * rate), int(len(img) * rate)))
        cv2.imshow(name, img)
        cv2.moveWindow(name, 0, 0)
        cv2.waitKey(0)
        img_viewed.append(name)
        write(img_viewed, log)
        cv2.destroyWindow(name)
        i += 1
    cv2.destroyAllWindows()

if __name__ == '__main__':
    path = "D:\\ljt\\Spider\\03\\konachan\\girls_und_panzer"   # enter the path
    screen = (1600, 900)    # enter the maximum screen size
    rate = 3 / 4
    log = "viewed.txt"
    view(path, log, screen, rate)
