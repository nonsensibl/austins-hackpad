import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation

keyboard = KMKKeyboard()

keyboard.col_pins = ()
keyboard.row_pins = (
    board.GP26, board.GP27, board.GP28, board.GP29,
    board.GP6, board.GP7, board.GP0, board.GP1,
)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

keyboard.keymap = [
    [KC.MACRO1, KC.MACRO2, KC.MACRO3, KC.MACRO4,
     KC.MACRO5, KC.MACRO6, KC.MACRO7, KC.MACRO8]
]

if __name__ == '__main__':
    keyboard.go()
