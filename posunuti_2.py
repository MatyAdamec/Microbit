O = [0,0] #start
P = [0,4] #end

M1 = [0,0]  #stred z O a P
M2 = [0,0]  #stred z O a M1
M3 = [0,0]  #stred z M1 a P

#vypocitani stredu usecky
M1[1] = Math.round((O[1]+P[1])/2)
M1[0] = Math.round((P[0]+O[0])/2)
M2[1] = Math.round((O[1]+M1[1])/2)
M2[0] = Math.round((M1[0]+O[0])/2)
M3[1] = Math.round((M1[1]+P[1])/2)
M3[0] = Math.round((P[0]+M1[0])/2)

roll = False
def on_forever():
    global O, P, M1, M2, M3, roll
    led.plot(O[0],O[1])
    led.plot(P[0],P[1])
    led.plot(M1[0],M1[1])
    led.plot(M2[0],M2[1])
    led.plot(M3[0],M3[1])

    if input.button_is_pressed(Button.B): #input z tlacitka
        roll = True

    if roll: #kazde 3 vteriny se usecka posune vodorovne doprava
        M1[0] += 1
        M2[0] += 1
        M3[0] += 1
        P[0] += 1
        O[0] += 1
        basic.pause(3000)
        basic.clear_screen()
forever(on_forever)
