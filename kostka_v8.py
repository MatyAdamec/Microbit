key = False
change = False

def adds():
    global key, change
    if input.button_is_pressed(Button.A):
        key = True
        basic.show_icon(IconNames.YES)
    if input.logo_is_pressed():
            if change:
                change = False
                sest()
            else:
                change = True
                deset()
basic.forever(adds)

def main():
    global key, change
    if input.is_gesture(Gesture.SHAKE) and key:
        if change:
            hod = randint(1, 10)
        else:
            hod = randint(1, 6)
        if hod ==1 :
            basic.show_leds("""
                . . . . .
                . . . . .
                . . # . .
                . . . . .
                . . . . .
            """)
        elif hod==2 :
            basic.show_leds("""
                    . . . . .
                    . . . # .
                    . . . . .
                    . # . . .
                    . . . . .
                """)
        elif hod==3 :
            basic.show_leds("""
                    . . . . .
                    . . . # .
                    . . # . .
                    . # . . .
                    . . . . .
                """)
        elif hod==4 :
            basic.show_leds("""
                    . . . . .
                    . # . # .
                    . . . . .
                    . # . # .
                    . . . . .
                """)
        elif hod==5 :
            basic.show_leds("""
                    . . . . .
                    . # . # .
                    . . # . .
                    . # . # .
                    . . . . .
                """)
        elif hod==6 :
            basic.show_leds("""
                    . . . . .
                    . # . # .
                    . # . # .
                    . # . # .
                    . . . . .
                """)
        elif hod==7 :
            basic.show_leds("""
                    . . . . .
                    . # . # .
                    . # # # .
                    . # . # .
                    . . . . .
                """)
        elif hod==8 :
            basic.show_leds("""
                    . . . . .
                    . # # # .
                    . # . # .
                    . # # # .
                    . . . . .
                """)
        elif hod==9 :
            basic.show_leds("""
                    . . . . .
                    . # # # .
                    . # # # .
                    . # # # .
                    . . . . .
                """)
        elif hod==10 :
            basic.show_leds("""
                    . . # . .
                    . # # # .
                    . # # # .
                    . # # # .
                    . . . . .
                """)
        for i in range(hod):
            music.play_tone(Note.C, music.beat())
            music.rest(music.beat(4))
        key = False
basic.forever(main)

def sest():
    basic.show_leds("""
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            # # # # #
    """)
    basic.show_leds("""
            . . . . .
            . . . . .
            . . . . .
            # # # # #
            # . . . .
        """)
    basic.show_leds("""
            . . . . .
            . . . . .
            # # # # #
            # . . . .
            # # # # #
        """)
    basic.show_leds("""
            . . . . .
            # # # # #
            # . . . .
            # # # # #
            # . . . #
        """)
    basic.show_leds("""
            # # # # #
            # . . . .
            # # # # #
            # . . . #
            # # # # #
        """)

def deset():
    basic.show_leds("""
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            # . # # #
    """)
    basic.show_leds("""
            . . . . .
            . . . . .
            . . . . .
            # . # # #
            # . # . #
        """)
    basic.show_leds("""
            . . . . .
            . . . . .
            # . # # #
            # . # . #
            # . # . #
        """)
    basic.show_leds("""
            . . . . .
            # . # # #
            # . # . #
            # . # . #
            # . # . #
        """)
    basic.show_leds("""
            # . # # #
            # . # . #
            # . # . #
            # . # . #
            # . # # #
        """)
