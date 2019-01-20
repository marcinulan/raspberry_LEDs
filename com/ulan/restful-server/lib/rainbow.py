import random
import time
import pigpio


def rainbow():
    # The Pins. Use Broadcom numbers.
    red_pin = 17
    green_pin = 22
    blue_pin = 24

    default_sleep = 0.01
    start_time = time.time()

    pi = pigpio.pi()

    def reset_light():
        pi.set_PWM_dutycycle(red_pin, 0)
        pi.set_PWM_dutycycle(green_pin, 0)
        pi.set_PWM_dutycycle(blue_pin, 0)

    reset_light()
    time.sleep(1)
    current_time = time.time()
    random.seed()

    def blink():
        pin = green_pin
        brightness = random.randrange(255)
        which_pin = random.randrange(3)
        if which_pin == 1:
            pin = green_pin
        if which_pin == 2:
            pin = red_pin
        if which_pin == 3:
            pin = blue_pin
        pi.set_PWM_dutycycle(pin, brightness)

    def blink2():
        reset_light()
        for x in range(1, random.randrange(255)):
            pi.set_PWM_dutycycle(red_pin, x)
            time.sleep(default_sleep)

        brightness = 0

        while brightness < 255:
            brightness += 1
            pi.set_PWM_dutycycle(blue_pin, brightness)
            time.sleep(default_sleep)

        brightness = 0

        while brightness < 255:
            brightness += 1
            pi.set_PWM_dutycycle(green_pin, brightness)
            time.sleep(default_sleep)

        while brightness > 0:
            brightness -= 1
            pi.set_PWM_dutycycle(green_pin, brightness)
            pi.set_PWM_dutycycle(red_pin, brightness)
            pi.set_PWM_dutycycle(blue_pin, brightness)

    def increaseColor(color, expected_brightness):
        starting_brightness = pi.get_PWM_dutycycle(color)
        while starting_brightness < expected_brightness:
            starting_brightness += 1
            pi.set_PWM_dutycycle(color, starting_brightness)
            time.sleep(default_sleep)

    def decreaseColor(color, expected_brightness):
        starting_brightness = pi.get_PWM_dutycycle(color)
        while starting_brightness > expected_brightness:
            starting_brightness -= 1
            pi.set_PWM_dutycycle(color, starting_brightness)
            time.sleep(default_sleep)

    def blink3():
        reset_light()
        increaseColor(red_pin, 222)
        increaseColor(green_pin, 100)
        decreaseColor(red_pin, 33)
        increaseColor(blue_pin, 66)
        decreaseColor(green_pin, 33)
        increaseColor(red_pin, 200)

    while current_time - start_time < 15:
        blink3()
        blink3()
        blink3()
        current_time = time.time()
        time.sleep(default_sleep)
    reset_light()
    pi.stop()
