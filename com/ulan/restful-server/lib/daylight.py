import time

import pigpio


def switch_lights():
    red_pin = 17
    green_pin = 22
    blue_pin = 24

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

    def switch_off():
        b, g, r = get_brightness()
        while b > 0:
            b -= 1
            pi.set_PWM_dutycycle(blue_pin, b)
            time.sleep(default_sleep)
        while g > 0:
            g -= 1
            pi.set_PWM_dutycycle(green_pin, g)
            time.sleep(default_sleep)

        while r > 0:
            r -= 1
            pi.set_PWM_dutycycle(red_pin, r)
            time.sleep(default_sleep)

    def switch_on():
        b, g, r = get_brightness()
        while b < 200:
            b += 1
            pi.set_PWM_dutycycle(blue_pin, b)
            time.sleep(default_sleep)
        while g < 200:
            g += 1
            pi.set_PWM_dutycycle(green_pin, g)
            time.sleep(default_sleep)
        while r < 255:
            r += 1
            pi.set_PWM_dutycycle(red_pin, r)
            time.sleep(default_sleep)

    if is_light:
        switch_off()
    else:
        switch_on()

    pi.stop()
