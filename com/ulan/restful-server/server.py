from flask import Flask
from flask_restful import Resource, Api
from lib import glowgreen
from lib import flashred
from lib import rainbow
from lib import daylight
from lib import blinkgreen

app = Flask(__name__)
api = Api(app)

glowing = 0
flashing = 0
error_message = '404 - Raspberry Pi not found'


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


api.add_resource(GlowGreen, '/GlowGreen')
api.add_resource(FlashRed, '/FlashRed')
api.add_resource(Rainbow, '/Rainbow')
api.add_resource(Daylight, '/SwitchLights')
api.add_resource(Notifier, '/Notify')

if __name__ == '__main__':
    app.run('0.0.0.0', '5002')
