import time
import pigpio


def switch_lights(level):
    red_pin = 17
    green_pin = 22
    blue_pin = 24

    level_int = int(level)

    default_sleep = 0.0001

    pi = pigpio.pi('192.168.1.31')

    def get_brightness():
        brightness_red = pi.get_PWM_dutycycle(red_pin)
        brightness_green = pi.get_PWM_dutycycle(green_pin)
        brightness_blue = pi.get_PWM_dutycycle(blue_pin)
        return brightness_blue, brightness_green, brightness_red

    def get_lights():
        brightness_blue, brightness_green, brightness_red = get_brightness()
        brightness = (brightness_red + brightness_green + brightness_blue)
        return brightness

    if get_lights() > 100:
        is_light = 1
        print("{} and {}".format(get_lights(), is_light))
    else:
        is_light = 0
        print("{} and {}".format(get_lights(), is_light))

    if level_int > 255:
        level_int = 255
    else:
        if level_int < 0:
            level_int = 0

    def switch_on():
        b, g, r = get_brightness()
        while b < level_int:
            b += 1
            pi.set_PWM_dutycycle(blue_pin, b)
            time.sleep(default_sleep)
        while g < level_int:
            g += 1
            pi.set_PWM_dutycycle(green_pin, g)
            time.sleep(default_sleep)
        while r < level_int:
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
