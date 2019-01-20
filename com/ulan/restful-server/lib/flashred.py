import time
import pigpio


def redflash():
    # The Pins. Use Broadcom numbers.
    red_pin = 17
    green_pin = 22
    blue_pin = 24

    default_sleep = 0.2
    start_time = time.time()

    pi = pigpio.pi()

    pi.set_PWM_dutycycle(red_pin, 0)
    pi.set_PWM_dutycycle(green_pin, 0)
    pi.set_PWM_dutycycle(blue_pin, 0)
    time.sleep(1)
    current_time = time.time()

    while (current_time - start_time) < 15:
        pi.set_PWM_dutycycle(red_pin, 255)
        time.sleep(default_sleep)
        pi.set_PWM_dutycycle(red_pin, 0)
        time.sleep(default_sleep)

        current_time = time.time()
        if (current_time - start_time) > 3:
            break

    pi.stop()
