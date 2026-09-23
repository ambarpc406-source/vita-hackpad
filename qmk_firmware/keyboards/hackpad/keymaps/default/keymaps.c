#include QMK_KEYBOARD_H


const uint16_t PROGMEM keymaps[][MATRIX_ROWS][MATRIX_COLS] = {

    [0] = LAYOUT(
        KC_Q, KC_W, KC_E,
        KC_A, KC_S, KC_D
    )

};




#if defined(ENCODER_MAP_ENABLE)

const uint16_t PROGMEM encoder_map[][NUM_ENCODERS][NUM_DIRECTIONS] = {

    [0] = {
        ENCODER_CCW_CW(
            MS_WHLD,
            MS_WHLU
        )
    }

};

#endif




void keyboard_post_init_user(void) {

    rgblight_enable_noeeprom();

    /*
     * LED 1
     * RED
     */
    rgblight_setrgb_at(
        255,
        0,
        0,
        0
    );


    /*
     * LED 2
     * GREEN
     */
    rgblight_setrgb_at(
        0,
        255,
        0,
        1
    );


    /*
     * LED 3
     * BLUE
     */
    rgblight_setrgb_at(
        0,
        0,
        255,
        2
    );


    /*
     * LED 4
     * PURPLE
     */
    rgblight_setrgb_at(
        180,
        0,
        255,
        3
    );
}