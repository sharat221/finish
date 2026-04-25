from flask import Flask, jsonify , render_template
from flask_cors import CORS   # FIX 2: import CORS
import csv

app = Flask(__name__)
CORS(app)                     # FIX 2: allow browser requests from any origin

def load_incidents():
    incidents = []
    # FIX 1: file is incidents.txt, not incidents.csv
    with open("incidents.txt", newline='', encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            incidents.append({
                "type": row["IncidentType"],
                "location": row["Location"],
                "severity": row["Severity"],
                "resource": row["AssignedResource"],
                "coords": [float(row["Latitude"]), float(row["Longitude"])]
            })
    return incidents
def index():
    return render_template("frontend.html")

@app.route("/incidents", methods=["GET"])
def get_incidents():
    return jsonify(load_incidents())

if __name__ == "__main__":
    app.run(debug=True)