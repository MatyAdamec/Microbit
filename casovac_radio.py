RunComp.set_light_level()
radio.set_group(974)
casStart=0
casStop=0
cycle = False
cycleend = True

def on_button_pressed_a():
    global casStart, casStop
    basic.show_number(casStart-casStop/1000)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_light_drop():
    global cycle, cycleend
    if cycleend:
        if cycle ==False:
            radio.send_number(1)
            cycle = True
        else:
            radio.send_number(2)
            cycleend=False
RunComp.on_light_drop(on_light_drop)

def on_received_number(receivedNumber):
    global casStart, casStop
    if receivedNumber == 1:
        casStart=control.millis()
    if receivedNumber == 2:
        casStop = control.millis()
radio.on_received_number(on_received_number)
