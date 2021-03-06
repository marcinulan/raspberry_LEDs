import time
import pigpio


def switch_lights(level_red, level_green, level_blue):
    red_pin = 17
    green_pin = 22
    blue_pin = 24

    try:
        level_red_int = int(level_red)
    except TypeError:
        level_red_int = 0

    try:
        level_green_int = int(level_green)
    except TypeError:
        level_green_int = 0

    try:
        level_blue_int = int(level_blue)
    except TypeError:
        level_blue_int = 0

    default_sleep = 0.0001

    pi = pigpio.pi()

    def get_brightness():
        brightness_red = pi.get_PWM_dutycycle(red_pin)
        brightness_green = pi.get_PWM_dutycycle(green_pin)
        brightness_blue = pi.get_PWM_dutycycle(blue_pin)
        return brightness_blue, brightness_green, brightness_red


    def switch_on():
        b, g, r = get_brightness()
        while b < level_blue_int:
            b += 1
            pi.set_PWM_dutycycle(blue_pin, b)
            time.sleep(default_sleep)
        while g < level_green_int:
            g += 1
            pi.set_PWM_dutycycle(green_pin, g)
            time.sleep(default_sleep)
        while r < level_red_int:
            r += 1
            pi.set_PWM_dutycycle(red_pin, r)
            time.sleep(default_sleep)

    def reset_light():
        pi.set_PWM_dutycycle(red_pin, 0)
        pi.set_PWM_dutycycle(green_pin, 0)
        pi.set_PWM_dutycycle(blue_pin, 0)

    reset_light()
    switch_on()

    pi.stop()
