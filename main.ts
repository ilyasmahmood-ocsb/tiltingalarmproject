input.onGesture(Gesture.TiltLeft, function on_gesture_tilt_left() {
    basic.showIcon(IconNames.Angry)
    music.playTone(262, music.beat(BeatFraction.Whole))
})
input.onGesture(Gesture.TiltRight, function on_gesture_tilt_right() {
    basic.showIcon(IconNames.Angry)
    music.playTone(262, music.beat(BeatFraction.Whole))
})
input.onGesture(Gesture.ScreenUp, function on_gesture_screen_up() {
    basic.clearScreen()
})
