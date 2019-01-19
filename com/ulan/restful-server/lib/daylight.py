import time

import pigpio


def switch_lights():
    red_pin = 17
    green_pin = 22
    blue_pin = 24

    default_sleep = 0.0001

    pi = pigpio.pi('192.168.1.31')

    def get_lights():
        brightness_blue, brightness_green, brightness_red = get_brightness()
        brightness = (brightness_red + brightness_green + brightness_blue)
        return brightness

    def get_brightness():
        brightness_red = pi.get_PWM_dutycycle(red_pin)
        brightness_green = pi.get_PWM_dutycycle(green_pin)
        brightness_blue = pi.get_PWM_dutycycle(blue_pin)
        return brightness_blue, brightness_green, brightness_red

    if get_lights() > 200:
        is_light = 1
    else:
        is_light = 0

    def switch_off():
        print('test1')
        time.sleep(1)
        b, g, r = get_brightness()
        print(r, g, b)
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

