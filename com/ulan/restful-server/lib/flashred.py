import time
import pigpio


def redflash():
    # The Pins. Use Broadcom numbers.
    RED_PIN = 17
    GREEN_PIN = 22
    BLUE_PIN = 24

    # Number of color changes per step (more is faster, less is slower).
    # You also can use 0.X floats.
    STEPS = 1
    default_sleep = 0.2
    startTime = time.time()

    pi = pigpio.pi('192.168.1.31')

    PIN = GREEN_PIN
    BRIGHTNESS = 0.0
    pi.set_PWM_dutycycle(RED_PIN, 0)
    pi.set_PWM_dutycycle(GREEN_PIN, 0)
    pi.set_PWM_dutycycle(BLUE_PIN, 0)
    time.sleep(1)
    current_time = time.time()

    while (current_time - startTime) < 15:
        pi.set_PWM_dutycycle(RED_PIN, 255)
        time.sleep(default_sleep)
        pi.set_PWM_dutycycle(RED_PIN, 0)
        time.sleep(default_sleep)

        current_time = time.time()
        if (current_time - startTime) > 10:
            break

    pi.stop()
