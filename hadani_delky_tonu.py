odpocet_start = 0
odpocet_konec = 0
ton = 0
input.on_button_pressed(Button.A, a)
input.on_button_pressed(Button.B, b)
input.on_logo_event(TouchButtonEvent.TOUCHED, dotyk_start)
input.on_logo_event(TouchButtonEvent.RELEASED, dotyk_konec)

def b():
    global ton
    basic.show_icon(IconNames.QUARTER_NOTE)
    ton = randint(600, 5000)
    music.play_tone(Note.C, ton)
    basic.clear_screen()

def a():
    if ton != 0:
        basic.show_icon(IconNames.QUARTER_NOTE)
        music.play_tone(Note.C, ton)
    basic.clear_screen()

def dotyk_start():
    global odpocet_start
    odpocet_start = control.millis()
    
def dotyk_konec():
    global odpocet_konec, ton
    odpocet_konec = control.millis()
    if ton-500<=odpocet_konec-odpocet_start:
        if odpocet_konec-odpocet_start >= ton+500:
            basic.show_icon(IconNames.NO)
            basic.clear_screen()
        else:
            basic.show_icon(IconNames.YES)
            basic.pause(250)
            basic.show_arrow(ArrowNames.EAST)
            basic.clear_screen()
            basic.pause(250)
            basic.show_arrow(ArrowNames.EAST)
            basic.clear_screen()
            ton = 0
    else:
        basic.show_icon(IconNames.NO)
        basic.clear_screen()
