import pigpio


def switch_lights():
    red_pin = 17
    green_pin = 22
    blue_pin = 24

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

    def switch_on():
        pi.set_PWM_dutycycle(red_pin, 0)
        pi.set_PWM_dutycycle(blue_pin, 0)
        pi.set_PWM_dutycycle(green_pin, 250)

    def switch_off():
        pi.set_PWM_dutycycle(red_pin, 0)
        pi.set_PWM_dutycycle(blue_pin, 0)
        pi.set_PWM_dutycycle(green_pin, 0)

    if get_lights() > 100:
        is_light = 1
        print("{} and {}".format(get_lights(), is_light))
    else:
        is_light = 0
        print("{} and {}".format(get_lights(), is_light))

    if is_light:
        switch_off()
    else:
        switch_on()