import board
import digitalio
import neopixel
import usb_hid

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners.keypad import KeysScanner
from kmk.extensions import Extension

from adafruit_hid.mouse import Mouse




KEY_PINS = (
    board.D0,
    board.D1,
    board.D2,
    board.D3,
    board.D8,
    board.D7,
)



keyboard = KMKKeyboard()


keyboard.matrix = KeysScanner(
    pins=KEY_PINS,
    value_when_pressed=False,
)




keyboard.keymap = [
    [
        KC.Q,    # SW1
        KC.W,    # SW2
        KC.E,    # SW3

        KC.A,    # SW4
        KC.S,    # SW5
        KC.D,    # SW6
    ]
]




RGB_PIN = board.D10

NUM_LEDS = 4

pixels = neopixel.NeoPixel(
    RGB_PIN,
    NUM_LEDS,
    brightness=0.15,
    auto_write=True,
)


# Different colour for each LED

pixels[0] = (255, 0, 0)       # LED 1 = RED
pixels[1] = (0, 255, 0)       # LED 2 = GREEN
pixels[2] = (0, 0, 255)       # LED 3 = BLUE
pixels[3] = (180, 0, 255)     # LED 4 = PURPLE




encoder_a = digitalio.DigitalInOut(board.D4)
encoder_b = digitalio.DigitalInOut(board.D5)

encoder_a.direction = digitalio.Direction.INPUT
encoder_b.direction = digitalio.Direction.INPUT

encoder_a.pull = digitalio.Pull.UP
encoder_b.pull = digitalio.Pull.UP




encoder_button = digitalio.DigitalInOut(board.D9)

encoder_button.direction = digitalio.Direction.INPUT
encoder_button.pull = digitalio.Pull.UP




mouse = Mouse(usb_hid.devices)



class ScrollEncoder(Extension):

    def __init__(self):
        self.last_a = encoder_a.value
        self.last_button = encoder_button.value

    def during_bootup(self, keyboard):
        pass

    def before_matrix_scan(self, keyboard):
        pass

    def after_matrix_scan(self, keyboard):

        

        current_a = encoder_a.value

        if current_a != self.last_a:

            if encoder_b.value != current_a:

                # Clockwise
                mouse.move(wheel=1)

            else:

                # Counter-clockwise
                mouse.move(wheel=-1)

        self.last_a = current_a


        
        current_button = encoder_button.value

        if self.last_button and not current_button:

            # Encoder press = left mouse click
            mouse.click(Mouse.LEFT_BUTTON)

        self.last_button = current_button

    def after_hid_send(self, keyboard):
        pass




keyboard.extensions.append(
    ScrollEncoder()
)




keyboard.go()