from flask import Flask, render_template
from opcua_reader import OPCUAReader
import config

app = Flask(__name__)
reader = OPCUAReader(config.SERVER_ENDPOINT)
MACHINE_LIST = config.MACHINE_LIST

@app.route("/")
def dashboard():
    reader.connect()
    data = reader.read_values(MACHINE_LIST)
    reader.disconnect()
    return render_template("dashboard.html", data=data)
