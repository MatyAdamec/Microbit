S = (2, 2)  #stred
trojuhelnik = [[0,0], [2,0], [1,2]] # trojuhelnik

for bod0 in trojuhelnik:    #vykresli trojuhelnik
    led.plot(bod0[0], bod0[1])
led.plot_brightness(S[0], S[1], 50) #vykresli stred

def on_button_pressed_a():
    basic.clear_screen()
    for forward in trojuhelnik: #vypocitek ptrojuhelnik +90°
        x = -1 * (forward[1] - S[1]) + S[0]
        y =  1 * (forward[0] - S[0]) + S[1]
        forward[0] = x
        forward[1] = y

    for bod1 in trojuhelnik:    #vykresli trojuhelnik
        led.plot(bod1[0], bod1[1])
    led.plot_brightness(S[0], S[1], 50) #vykresli stred
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    basic.clear_screen()
    for reverse in trojuhelnik: #vypocitek ptrojuhelnik -90°
        x =  1 * (reverse[1] - S[1]) + S[0]
        y = -1 * (reverse[0] - S[0]) + S[1]
        reverse[0] = x
        reverse[1] = y

    for bod2 in trojuhelnik:    #vykresli trojuhelnik
        led.plot(bod2[0], bod2[1])
    led.plot_brightness(S[0], S[1], 50) #vykresli stred
input.on_button_pressed(Button.B, on_button_pressed_b)
