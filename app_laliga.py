from flask import Flask, render_template, send_from_directory
import sqlite3
import pathlib
import os

base_path = pathlib.Path(r"")

app = Flask(__name__)

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')
    
@app.route("/")
def index():
    players = get_db_players("database/pd_laliga.db")
    
    return render_template("index.html", players=players)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/team")
def team():
    return render_template("team.html")

@app.route("/data")
def data():
    players = get_db_players("database/pd_laliga.db")
    
    return render_template("index.html", players=players)

def get_db_players(dbpath):
    conn = sqlite3.connect("database/pd_laliga.db") 
    cur = conn.cursor()
    players = cur.execute("SELECT * FROM pd_players").fetchall()
    conn.close()
    
    return players

if __name__ == "__main__":
    app.run(debug = True)
    
    
