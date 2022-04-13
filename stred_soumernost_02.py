S = [2,2]   #stred
obdelnik = [[1,0], [3,0], [1,1], [3,1]] #obdelnik
odraz = [[0,0], [0,0], [0,0], [0,0]]    #odraz

def odrz():
    global obdelnik, odraz, S
    for i in range(len(obdelnik)):
        for f in range(0,2):
            odraz[i][f] = obdelnik[i][f] + 2*(S[f] - obdelnik[i][f])  #prevrati bod kolem stredu

def kresli():   # vykresli obdelnik a odraz
    global obdelnik, odraz,S
    led.plot_brightness(S[0], S[1], 50)
    for x in obdelnik:
        led.plot(x[0],x[1])
    for z in odraz:
        led.plot(z[0],z[1])
odrz()
kresli()

def on_forever():   #postupně men pozici obdelniku
    basic.pause(1000)
    for y in range(3):
        obdelnik[0][1] +=1
        obdelnik[1][1] +=1
        obdelnik[2][1] +=1
        obdelnik[3][1] +=1
        odrz()
        basic.clear_screen()
        kresli()
        basic.pause(1000)
    for x in range(3):
        obdelnik[0][1] -=1
        obdelnik[1][1] -=1
        obdelnik[2][1] -=1
        obdelnik[3][1] -=1
        odrz()
        basic.clear_screen()
        kresli()
        basic.pause(1000)    
    
forever(on_forever)
