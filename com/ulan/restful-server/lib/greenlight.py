import pigpio


def switch_lights():
    red_pin = 17
    green_pin = 22
    blue_pin = 24

    pi = pigpio.pi('192.168.1.31')

    def get_brightness():
        brightness_blue = pi.get_PWM_dutycycle(green_pin)
        return brightness_blue

    def switch_on():
        pi.set_PWM_dutycycle(red_pin, 0)
        pi.set_PWM_dutycycle(blue_pin, 0)
        pi.set_PWM_dutycycle(green_pin, 250)

    def switch_off():
        pi.set_PWM_dutycycle(red_pin, 0)
        pi.set_PWM_dutycycle(blue_pin, 0)
        pi.set_PWM_dutycycle(green_pin, 0)

    if get_brightness() > 100:
        is_light = 1
        print("{} and {}".format(get_brightness(), is_light))
    else:
        is_light = 0
        print("{} and {}".format(get_brightness(), is_light))

    if is_light:
        switch_off()
    else:
        switch_on()