from flask import Flask
from flask_cors import CORS

import woz_data_opvragen
import felix
import Tizz

app = Flask(__name__)
CORS(app)

@app.route("/")
def helloWorld():
  return "Root Mount WOZ"

@app.route("/eigenaren/allen")
def eigenaren_allen():
  return woz_data_opvragen.toon_alle_eigenaren()


@app.route("/huizen/allen")
def huizen_allen():
  return woz_data_opvragen.toon_alle_huizen()


@app.route("/cbs/woz_per_regio_en_steden")
def woz_per_regio_en_steden():
  return woz_data_opvragen.woz_per_regio_en_steden()

@app.route("/felixvoorbeeld")
def felixvoorbeeld():
  return felix.mijnmethode()

@app.route("/stijn")
def StijnDank():
  return Tizz.mijnmethode()
