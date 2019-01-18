from flask import Flask
from flask_restful import Resource, Api
from lib import glowgreen
from lib import flashred
from lib import rainbow

# from lib import flash-red

app = Flask(__name__)
api = Api(app)

glowing = 0
flashing = 0


class GlowGreen(Resource):
    def get(self):
        glowgreen.greenglow()
        return 200


class FlashRed(Resource):
    def get(selfself):
        flashred.redflash()
        return 200

class Rainbow(Resource):
    def get(selfself):
        rainbow.rainbow()
        return 200


api.add_resource(GlowGreen, '/GlowGreen')
api.add_resource(FlashRed, '/FlashRed')
api.add_resource(Rainbow, '/Rainbow')

if __name__ == '__main__':
    app.run(port='5002')
