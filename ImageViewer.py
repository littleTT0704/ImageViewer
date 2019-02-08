import cv2
import os

open("viewed.txt", "a")
with open("viewed.txt", "r") as f:
    img_viewed = f.read().rstrip().split("\n")
imgs = []
path = ""   # enter the path
for root, dirs, files in os.walk(path):
    for name in files:
        imgs.append(os.path.join(root, name))
    for name in dirs:
        imgs.append(os.path.join(root, name))

screen = (1600, 900)    # enter the maximum screen size
i = 0
while i < (len(imgs)):
    name = imgs[i]
    img = cv2.imread(name)
    if name in img_viewed or img is None:
        i += 1
        continue
    while len(img) >= screen[1] or len(img[0]) >= screen[0]:
        img = cv2.resize(img, (len(img[0]) * 3 // 4, len(img) * 3 // 4))
    cv2.imshow(name, img)
    cv2.moveWindow(name,10,10)
    cv2.waitKey(0)
    img_viewed.append(name)
    with open("viewed.txt", "w") as f:
        for _ in img_viewed:
            f.write(_ + "\n")
    cv2.destroyWindow(name)
    i += 1

cv2.destroyAllWindows()
