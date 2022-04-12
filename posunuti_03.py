O = [1,0] 
P = [0,1] 

roll = False
def on_forever():
    global roll
    led.plot(O[0],O[1])
    led.plot(P[0],P[1])

    if input.button_is_pressed(Button.AB): #input z tlacitka
        roll = True

    if roll: #kazde 3 vteriny se usecka posune diagonalně doprava dolu

        P[0] += 1
        O[0] += 1
        P[1] += 1
        O[1] += 1
        basic.pause(3000)
        basic.clear_screen()
forever(on_forever)
