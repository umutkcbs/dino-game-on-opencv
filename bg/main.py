import cv2
import time
import ctypes   
import random
import keyboard
import numpy as np

fps = 10000
time_delta = 1./fps

global yukseklik
yukseklik = 300
kaktuskonum = 920
kaktushiz = 20
puan = 0

dino = cv2.imread("dino.jpg")
dino = np.array(dino)
print(dino.shape)
#time.sleep(10)
dino = cv2.resize(dino, (100,100))

cactus = cv2.imread("cac.png")
cactus = np.array(cactus)
cactus = cv2.resize(cactus ,(50,100))

bgcount = 1
while True:
    if bgcount > 63:
        bgcount = 1
    imgname = 'bg/bg' + '1' + '.jpg' #str(int(bgcount / 1))
    print(imgname) 
    img = cv2.imread(imgname)
    img = np.array(img)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    w, h, c = img.shape

    if keyboard.is_pressed("space"):
        yukseklik = yukseklik - 45
    
    if yukseklik < 20:
        yukseklik = 300

    if yukseklik < 350:
        yukseklik = yukseklik + 10

    #340,462    380, 480    
    img[yukseklik:yukseklik + 100, 150:250] = dino
    #img = cv2.circle(img, (300 ,yukseklik), 50, (255, 0, 0), 15)

    kaktuskonum = kaktuskonum - kaktushiz
    if kaktuskonum > 0:
        img[350:450, kaktuskonum:kaktuskonum + 50] = cactus
        #img = cv2.circle(img, (kaktuskonum ,400), 50, (0, 0, 255), 15)
    else:
        kaktuskonum = 920
        kaktushiz = random.randint(15,25)
        puan = puan + 1

    if kaktuskonum < 215 and kaktuskonum > 185 and yukseklik > 270:
        cv2.destroyAllWindows()
        gameover = ctypes.windll.user32.MessageBoxW(0, str(puan), "Score:", 5)
        if gameover == 4:
            puan = 0
            kaktuskonum = 920
        else:
            break

    img = cv2.putText(img, str(puan), (50, 80), cv2.FONT_HERSHEY_SIMPLEX, 3, (0,0,0), 5)

    print(kaktuskonum, yukseklik)
    cv2.imshow("dinodino", img)
    cv2.waitKey(1)

    bgcount = bgcount + 1

    t0 = time.clock()               ###########
    #time.sleep(time_delta / 2)     # EASY MODE
    t1 = time.clock()               ###########

    if keyboard.is_pressed("q"):
        break