from flask import Flask,render_template
import requests
import os 
import json

app = Flask(__name__, template_folder="templates")

@app.route("/home")
def index():
    try:
        r = requests.get(f"{os.getenv('BACKEND_API')}/person/")
        if r.status_code == 200:
            return render_template("index.html",persons=r.json())
        else:
            return "Error"
    except Exception as error:
        return f"ERROR {error}"

app.run()