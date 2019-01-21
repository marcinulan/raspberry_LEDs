import time

import pigpio


def blink():
    red_pin = 17
    green_pin = 22
    blue_pin = 24

    default_sleep = 0.09

    pi = pigpio.pi()

# try:
    r = pi.get_PWM_dutycycle(red_pin)
    g = pi.get_PWM_dutycycle(green_pin)
    b = pi.get_PWM_dutycycle(blue_pin)

    def pik():
        pi.set_PWM_dutycycle(red_pin, 0)
        pi.set_PWM_dutycycle(green_pin, 255)
        pi.set_PWM_dutycycle(blue_pin, 0)
        time.sleep(default_sleep)
        pi.set_PWM_dutycycle(red_pin, r)
        pi.set_PWM_dutycycle(green_pin, g)
        pi.set_PWM_dutycycle(blue_pin, b)
        time.sleep(default_sleep)

    pik()
    pik()
    pi.stop()
