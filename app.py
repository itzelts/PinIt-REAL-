import os
import re
import geocoder
from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Custom filter
#app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///pinit.db")

# Make sure API key is set
# if not os.environ.get("API_KEY"):
#     raise RuntimeError("API_KEY not set")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

@app.route("/")
@login_required
def index():
    """Show Locations (MAP)"""
    pins = db.execute("SELECT lat, long FROM locations")

    return render_template("index.html", pins = pins)
 
@app.route("/leaderboard", methods=["GET", "POST"])
@login_required
def leaderboard():
    """Show locations in table"""
    locations = db.execute("SELECT * FROM locations ORDER BY rank DESC")

    return render_template("leaderboard.html", locations=locations)

@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            flash("must provide username")
            return redirect("/upload")


        # Ensure password was submitted
        elif not request.form.get("password"):
            flash("must provide password")
            return redirect("/upload")


        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?",
                          request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")

@app.route("/logout")
@login_required
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")

@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            flash("Must provide username")
            return redirect("/register")

        #if not request.form.get("email"):
            #return apology("Must provide email", 400)

        # Ensure username is not taken
        elif len(db.execute("SELECT * FROM users WHERE username=:username", username=request.form.get("username"))) != 0:
            flash("Username unavailable")
            return redirect("/register")

        #elif not re.fullmatch(r"[^@]+@[^@]+\.[^@]+", request.form.get("email")):
            #return apology("Must enter a valid email", 400)

        # Ensure password was submitted
        elif not request.form.get("password"):
            flash("Must provide password")
            return redirect("/register")

        # Ensure password meets requirements
        elif len(request.form.get("password")) < 8:
            flash("Password must be at least 8 characters long")
            return redirect("/register")


        elif not any(char.isdigit() for char in request.form.get("password")):
            flash("Password must contain one number")
            return redirect("/register")

        elif not any(char.isupper() for char in request.form.get("password")):
            flash("Password must contain one uppercase character")
            return redirect("/register")

        elif not any(char.isalnum for char in request.form.get("password")):
            flash("Password must contain one special character")
            return redirect("/register")

        # Ensure password was submitted
        elif not request.form.get("confirmation"):
            flash("Must confirm password")
            return redirect("/register")

        # Ensure passwords match
        elif request.form.get("confirmation") != request.form.get("password"):
            flash("Passwords must match", 400)
            return redirect("/register")

        # Hash password
        hash = generate_password_hash(request.form.get("password"))

        # Add user to database
        user = db.execute("INSERT INTO users (username, hash) VALUES (:username,:hash)",
                          username=request.form.get("username"), hash=hash)

        # Remember user
        session["user_id"] = user

        # Rederict user to homepage
        return redirect("/")

    # User reached route via GET
    else:
        return render_template("register.html")


@app.route("/upload", methods=["GET", "POST"])
@login_required
def upload():
    """Sell shares of stock"""

    if request.method == "POST":

        # Ensure stock is selected
        if not request.form.get("name"):
            flash("Must input name")
            return redirect("/upload")

        # Ensure user owns stock
        
        # Ensure shares is submitted
        elif not request.form.get("description"):
            flash("Must provide description")
            return redirect("/upload")


        g = geocoder.ip('me')
        lat = g.lat
        long = g.lng

        if len(db.execute("SELECT * FROM locations WHERE name=:name", name=request.form.get("name"))) != 0:
            db.execute("UPDATE locations SET rank = rank + 1 WHERE name=:name", name=request.form.get("name"))
        else:
            db.execute("INSERT INTO locations (name, description, lat, long) VALUES (:name, :description, :lat, :long)", name=request.form.get("name"), description=request.form.get("description"), long=long, lat=lat)

        # Redirect user to home page
        return redirect("/")

    else:
        return render_template("upload.html")
