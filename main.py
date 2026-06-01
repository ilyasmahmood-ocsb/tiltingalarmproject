def on_gesture_tilt_left():
    basic.show_icon(IconNames.ANGRY)
    music.play_tone(262, music.beat(BeatFraction.WHOLE))
input.on_gesture(Gesture.TILT_LEFT, on_gesture_tilt_left)

def on_gesture_tilt_right():
    basic.show_icon(IconNames.ANGRY)
    music.play_tone(262, music.beat(BeatFraction.WHOLE))
input.on_gesture(Gesture.TILT_RIGHT, on_gesture_tilt_right)

def on_gesture_screen_up():
    basic.clear_screen()
input.on_gesture(Gesture.SCREEN_UP, on_gesture_screen_up)