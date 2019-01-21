import time

import pigpio
from flask import Flask
from flask_restful import Resource, Api, reqparse
from lib import glowgreen
from lib import flashred
from lib import rainbow
from lib import daylight
from lib import customwhite
from lib import blinkgreen
from lib import greenlight
from lib import redlight
from lib import bluelight

app = Flask(__name__)
api = Api(app)

glowing = 0
flashing = 0
error_message = '404 - Raspberry Pi not found'
red_pin = 17
green_pin = 22
blue_pin = 24

pi = pigpio.pi()
pi.set_PWM_dutycycle(red_pin, 255)
pi.set_PWM_dutycycle(green_pin, 255)
pi.set_PWM_dutycycle(blue_pin, 255)
time.sleep(0.004)
pi.set_PWM_dutycycle(red_pin, 0)
pi.set_PWM_dutycycle(green_pin, 0)
pi.set_PWM_dutycycle(blue_pin, 0)

class GlowGreen(Resource):
    @staticmethod
    def get():
        try:
            glowgreen.greenglow()
            return 200
        except AttributeError:
            return error_message


class FlashRed(Resource):
    @staticmethod
    def get():
        try:
            flashred.redflash()
            return 200
        except AttributeError:
            return error_message


class Rainbow(Resource):
    @staticmethod
    def get():
        try:
            rainbow.rainbow()
            return 200
        except AttributeError:
            return error_message


class Daylight(Resource):
    @staticmethod
    def get():
        try:
            daylight.switch_lights()
            return 200
        except AttributeError:
            return error_message


class Notifier(Resource):
    @staticmethod
    def get():
        try:
            blinkgreen.blink()
            return 200
        except AttributeError:
            return error_message


class GreenLight(Resource):
    @staticmethod
    def get():
        try:
            greenlight.switch_lights()
            return 200
        except AttributeError:
            return error_message


class RedLight(Resource):
    @staticmethod
    def get():
        try:
            redlight.switch_lights()
            return 200
        except AttributeError:
            return error_message


class BlueLight(Resource):
    @staticmethod
    def get():
        try:
            bluelight.switch_lights()
            return 200
        except AttributeError:
            return error_message


class CustomWhite(Resource):
    @staticmethod
    def post():
        try:
            parser = reqparse.RequestParser()
            parser.add_argument("level")
            args = parser.parse_args()
            customwhite.switch_lights(args["level"])
            return 200
        except AttributeError:
            return error_message


api.add_resource(GlowGreen, '/GlowGreen')
api.add_resource(FlashRed, '/FlashRed')
api.add_resource(Rainbow, '/Rainbow')
api.add_resource(Daylight, '/SwitchLights')
api.add_resource(CustomWhite, '/CustomWhite')
api.add_resource(Notifier, '/Notify')
api.add_resource(GreenLight, '/Green')
api.add_resource(RedLight, '/Red')
api.add_resource(BlueLight, '/Blue')

if __name__ == '__main__':
    app.run('0.0.0.0', '5002')
