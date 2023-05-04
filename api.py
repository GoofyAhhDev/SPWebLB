#THIS API IS MADE BY https://github.com/apotpvp
#QUESTIONS? DM ME ON DISCORD: Jordy#2411
#version 1.2.10
#
#THIS API IS MADE TO DISPLAY THE TOP 10 PLAYERS OF THE SERVER IN EACH GAMEMODE OF THE MINECRAFT PLUGIN "STRIKE PRACTICE"
#THIS API MAKES USE OF AN MARIA DB DATABASE TO STORE THE PLAYERS STATS SO MAKE SURE TO HAVE ONE
#THIS API RUNS A FLASK SERVER TO DISPLAY THE STATS IN A WEBPAGE (WEBPAGE IS INCLUDED IN THE REPO)
#
#TO ADD NEW STATS TO THE API YOU NEED TO ADD THE COLUMN TO THE DATABASE AND THEN ADD THE FUNCTION TO GET THE STATS AND THE ROUTE TO THE FLASK SERVER YOU ALSO NEED TO UPDATE STATS.HTML TO DISPLAY THE NEW STATS 
#JUST COPY DIV OF CURRENT STATS AND EDIT TO YOUR LIKING, MAKE SURE TO CHANGE THE DIV TO THE ROUTE OF YOUR STATS


#IMPORTS
import mariadb
from flask import Flask, jsonify, render_template
from apscheduler.schedulers.background import BackgroundScheduler
from flask_caching import Cache
from flask import g
import os
from dotenv import load_dotenv

#FLASK APP INIT
app = Flask(__name__)


#LOADING ENVIRONMENT VARIABLES
load_dotenv()


#DISABLE CACHE
cache = Cache(config={'CACHE_TYPE': 'null'})
cache.init_app(app)

#OPENING DB
def get_db():
    if 'db' not in g:
        try:
            g.db = mariadb.connect(
                host=os.environ.get('DB_HOST'),
                user=os.environ.get('DB_USER'),
                password=os.environ.get('DB_PASSWORD'),
                database=os.environ.get('DB_NAME'),
                port=int(os.environ.get('DB_PORT'))
            )
        except mariadb.Error as e:
            print(f"Error connecting to database: {e}")
            return None
    return g.db

#CLOSING DB
def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()

# ELO COLLECTION FUNCTION
def get_stats(column_name):
    try:
        db = get_db()
        if db is None:
            return []
        with db.cursor() as cursor:
            cursor.execute(f"SELECT username, {column_name} FROM stats ORDER BY {column_name} DESC LIMIT 10;")
            rows = cursor.fetchall()

            players = []
            for row in rows:
                players.append({
                    "username": row[0],
                    column_name: row[1]
                })

            while len(players) < 10:
                players.append({
                    "username": "--------",
                    column_name: "--------"
                })

            return players
    except mariadb.Error as err:
        print(f"Error: {err}")
        return []
    finally:
        close_db()

#SEARCH OPTIONS FOR STATS
def get_stats_global():
    return get_stats("global_elo")

def get_stats_nodebuff():
    return get_stats("elo_nodebuffelo")

def get_stats_debuff():
    return get_stats("elo_debuffelo")

def get_stats_boxing():
    return get_stats("elo_boxingelo")

def get_stats_sumo():
    return get_stats("elo_sumoelo")

def get_stats_builduhc():
    return get_stats("elo_builduhcelo")

def get_stats_hcf():
    return get_stats("elo_hcfelo")

def get_stats_gapple():
    return get_stats("elo_gappleelo")

def get_stats_soup():
    return get_stats("elo_soupelo")



# FLASK STATS ROUTES
@app.route("/stats/global")
def stats_global():
    global_players = get_stats_global()
    return render_template("global_stats.html", global_players=global_players)

@app.route("/stats/nodebuff")
def stats_nodebuff():
    nodebuff_players = get_stats_nodebuff()
    return render_template("nodebuff_stats.html", nodebuff_players=nodebuff_players)

@app.route("/stats/debuff")
def stats_debuff():
    debuff_players = get_stats_debuff()
    return render_template("debuff_stats.html", debuff_players=debuff_players)

@app.route("/stats/boxing")
def stats_boxing():
    boxing_players = get_stats_boxing()
    return render_template("boxing_stats.html", boxing_players=boxing_players)

@app.route("/stats/sumo")
def stats_sumo():
    sumo_players = get_stats_sumo()
    return render_template("sumo_stats.html", sumo_players=sumo_players)

@app.route("/stats/builduhc")
def stats_builduhc():
    builduhc_players = get_stats_builduhc()
    return render_template("builduhc_stats.html", builduhc_players=builduhc_players)

@app.route("/stats/hcf")
def stats_hcf():
    hcf_players = get_stats_hcf()
    return render_template("hcf_stats.html", hcf_players=hcf_players)

@app.route("/stats/gapple")
def stats_gapple():
    gapple_players = get_stats_gapple()
    return render_template("gapple_stats.html", gapple_players=gapple_players)

@app.route("/stats/soup")
def stats_soup():
    soup_players = get_stats_soup()
    return render_template("soup_stats.html", soup_players=soup_players)

#FLASK MAIN PAGE ROUTE
@app.route("/")
def index():
    return render_template("index.html")

#FLASK STATS PAGE ROUTE
@app.route("/stats.html")
def stats():
    global_players = get_stats_global()
    nodebuff_players = get_stats_nodebuff()
    debuff_players = get_stats_debuff()
    boxing_players = get_stats_boxing()
    sumo_players = get_stats_sumo()
    builduhc_players = get_stats_builduhc()
    hcf_players = get_stats_hcf()
    gapple_players = get_stats_gapple()
    soup_players = get_stats_soup()
    return render_template("stats.html", nodebuff_players=nodebuff_players, debuff_players=debuff_players, global_players=global_players, boxing_players=boxing_players, sumo_players=sumo_players, builduhc_players=builduhc_players, hcf_players=hcf_players, gapple_players=gapple_players, soup_players=soup_players)

#FLASK CACHE DISABLE
@app.after_request
def add_header(response):
    response.cache_control.no_store = True
    return response

#FLASK APP RUN
if __name__ == "__main__":
    app.run(debug=True)
