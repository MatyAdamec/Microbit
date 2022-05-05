delka = randint(3, 10)*1000
klic = False
klic_zacatek = False
klic_whole = True
hudba = False

def zacatek():
    global klic_zacatek
    global delka, klic , hudba
    doba_zacatek = input.running_time()
    if doba_zacatek >= delka:
        basic.show_icon(IconNames.DIAMOND)
        klic_zacatek = True
        klic = True
        hudba = True
        basic.clear_screen()

def restart():
    if input.logo_is_pressed():
        control.reset()

def hudba_loop():
    global hudba
    if hudba:
        music.play_tone(262, 1500)

def hra():
    global klic, klic_zacatek, klic_whole, hudba
    if klic_whole == True:
        if klic_zacatek == False:
            zacatek()
            control.in_background(hudba_loop)
        if klic == True:
            if input.pin_is_pressed(TouchPin.P1):
                basic.show_number(1)
                klic_whole = False
            elif input.pin_is_pressed(TouchPin.P2):
                basic.show_number(2)
                klic_whole = False
            elif input.pin_is_pressed(TouchPin.P1) and input.pin_is_pressed(TouchPin.P2):
                basic.show_string("R")
                klic_whole = False
        else:
            if input.pin_is_pressed(TouchPin.P1):
                basic.show_string("B")
                klic_whole = False
            elif input.pin_is_pressed(TouchPin.P2):
                basic.show_string("A")
                klic_whole = False
            elif input.pin_is_pressed(TouchPin.P1) and input.pin_is_pressed(TouchPin.P2):
                basic.show_string("C")
                klic_whole = False
    else:
        pause(3000)
        control.reset()
forever(hra)
