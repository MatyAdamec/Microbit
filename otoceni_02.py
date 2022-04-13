S = (2, 2)
led.plot_brightness(2, 2, 100)


body =  [[0,0], [1,1]]  #uhlopricne body
body2 = [[2,0], [2,1]]  #horizontalni body

def on_forever():
    basic.clear_screen()
    for bod1 in body:   #vypocitat nasledujici body
        x = -1 * (bod1[1] - S[1]) + S[0]
        y =  1 * (bod1[0] - S[0]) + S[1]
        bod1[0] = x
        bod1[1] = y

    for c in body:  #vykreslit body
        led.plot(c[0], c[1])
    
    led.plot_brightness(S[0], S[1], 50)
    pause(500)
    basic.clear_screen()
    
    for bod2 in body2:  #vypocitat nasledujici body
        t = -1 * (bod2[1] - S[1]) + S[0]
        o =  1 * (bod2[0] - S[0]) + S[1]
        bod2[0] = t
        bod2[1] = o

    for g in body2: #vykreslit body
        led.plot(g[0], g[1])
    
    led.plot_brightness(S[0], S[1], 50)
    pause(500)
forever(on_forever)
