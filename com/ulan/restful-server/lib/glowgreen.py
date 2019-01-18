import time
import pigpio


def greenglow():
    # The Pins. Use Broadcom numbers.
    RED_PIN = 17
    GREEN_PIN = 22
    BLUE_PIN = 24

    # Number of color changes per step (more is faster, less is slower).
    # You also can use 0.X floats.
    STEPS = 1
    default_sleep = 0.0005
    startTime = time.time()

    pi = pigpio.pi('192.168.1.31')

    PIN = GREEN_PIN
    BRIGHTNESS = 0.0

    while True:
        while BRIGHTNESS < 220:
            BRIGHTNESS += 1
            pi.set_PWM_dutycycle(GREEN_PIN, BRIGHTNESS)
            time.sleep(default_sleep)

        while BRIGHTNESS > 0:
            BRIGHTNESS -= 1
            pi.set_PWM_dutycycle(GREEN_PIN, BRIGHTNESS)
            time.sleep(default_sleep)

        currentTime = time.time()
        if (currentTime - startTime) > 10:
            break

    pi.stop()



