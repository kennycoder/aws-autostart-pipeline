from os import environ
from flask import Flask
from flask import jsonify
from flask import request
from aws_xray_sdk.core import xray_recorder
from aws_xray_sdk.ext.flask.middleware import XRayMiddleware
from aws_xray_sdk.core.sampling.local.sampler import LocalSampler
from aws_xray_sdk.core import patch_all
import logging

app = Flask(__name__)

logging.basicConfig(level='WARNING')
logging.getLogger('aws_xray_sdk').setLevel(logging.DEBUG)

xray_recorder.configure(service='scale-to-zero-pipeline', sampling=False)
XRayMiddleware(app, xray_recorder)
patch_all()

@app.route("/")
@xray_recorder.capture('Welcome route')
def hello():
    retval = {
        "message": "Hello from Fargate :)"
    }

    return jsonify(retval)

if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host='0.0.0.0', debug=True, port=80)
