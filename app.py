from flask import Flask
import logging

app = Flask(__name__)

@app.route("/")
def hello():
    app.logger.info('Main request successfull')
    return "Hello World!"

@app.route("/status")
def status():
    app.logger.info('Status request successfull')
    return { "result": "OK - healthy"}

@app.route("/metrics")
def metrics():
    app.logger.info('Metrics request successfull')
    return { "data": {"UserCount": 140, "UserCountActive": 23}}

if __name__ == "__main__":
    logging.basicConfig(filename="app.log",level=logging.DEBUG,format='%(asctime)s, %(message)s')
    app.run(host='0.0.0.0')
