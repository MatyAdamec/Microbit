S = [2,2] #stred
ctverec = [[0,3],[0,2],[1,3],[1,2]] #ctverec
odraz = [[1,0],[1,1],[2,0],[2,1]]   #odraz ctverce

def odrz():
    global ctverec, odraz, S
    for i in range(len(ctverec)):
        for e in range(0,2):
            odraz[i][e] = ctverec[i][e] + 2*(S[e] - ctverec[i][e])  #prevrati bod kolem stredu

def kresli():   # vykresli ctverec a odraz
    global ctverec, odraz,S
    led.plot_brightness(S[0], S[1], 50)
    for x in ctverec:
        led.plot(x[0],x[1])
    for z in odraz:
        led.plot(z[0],z[1])
odrz()
kresli()
def on_button_pressed_a(): #zvetsi ctverec
    ctverec[1][1] -=1
    ctverec[2][0] +=1
    ctverec[3][0] +=1
    ctverec[3][1] -=1
    if ctverec[1][1] <0:    #resetuje ctverec
        ctverec[1] = [0,2]
        ctverec[2] =[1,3]
        ctverec[3] =[1,2]
    odrz()
    basic.clear_screen()
    kresli()
input.on_button_pressed(Button.A, on_button_pressed_a)
