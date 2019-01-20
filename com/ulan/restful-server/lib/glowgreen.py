import time
import pigpio


def greenglow():
    green_pin = 22
    default_sleep = 0.00005
    start_time = time.time()

    pi = pigpio.pi()

    brightness = 0.0

    while True:
        while brightness < 220:
            brightness += 1
            pi.set_PWM_dutycycle(green_pin, brightness)
            time.sleep(default_sleep)

        while brightness > 0:
            brightness -= 1
            pi.set_PWM_dutycycle(green_pin, brightness)
            time.sleep(default_sleep)

        current_time = time.time()
        if (current_time - start_time) > 10:
            break

    pi.stop()



