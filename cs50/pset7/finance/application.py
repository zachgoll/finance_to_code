from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session, url_for
from flask_session import Session
from passlib.apps import custom_app_context as pwd_context
from tempfile import mkdtemp

from helpers import *

# configure application
app = Flask(__name__)

# ensure responses aren't cached
if app.config["DEBUG"]:
    @app.after_request
    def after_request(response):
        response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
        response.headers["Expires"] = 0
        response.headers["Pragma"] = "no-cache"
        return response

# custom filter
app.jinja_env.filters["usd"] = usd

# configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")

@app.route("/")
@login_required
def index():
    user = session["user_id"]
    portfolio = db.execute("SELECT * FROM portfolio WHERE user = :user", user = user)
    
    for rows in portfolio:
        rows["current_price"] = usd(rows["current_price"])
        rows["total_value"] = usd(rows["total_value"])
    
    users = db.execute("SELECT * FROM users WHERE id = :id", id = user)
    curBal = users[0]["cash"]
    username = users[0]["username"]
    
    portfolioValue = db.execute("SELECT sum(total_value) FROM portfolio WHERE user = :user", user = user)
    pv = portfolioValue[0]["sum(total_value)"]
    
    if pv == None:
        value = 0
    else:
        value = usd(pv)
    
    return render_template("portfolio.html", portfolio = portfolio, username = username, curBal = usd(curBal), value = value)

@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    
    if request.method == "POST":
        # Check for inputs
        if not request.form.get("tickerBuy") or lookup(request.form.get("tickerBuy")) == None:
            return apology("Must enter", "a valid ticker symbol")
        if not (request.form.get("numShares")) or int(request.form.get("numShares")) < 0:
            return apology("Must enter", "positive number of shares to buy")
        
        # Define variables for database insertion
        
        stock = lookup(request.form.get("tickerBuy"))
        ticker = request.form.get("tickerBuy")
        shares = request.form.get("numShares")
        total = int(stock["price"])*int(request.form.get("numShares"))
        formattedTotal = usd(total)
        user = session["user_id"]
        
        # Get current user's cash balance
        
        currentUserBalance = db.execute("SELECT cash FROM users WHERE id = :id", id = user)
        newBalance = (currentUserBalance[0]["cash"]) - total
        formattedNewBalance = usd(newBalance)
        
        # Check to make sure user has enough money for their requested purchase
        
        if newBalance > 0:
            
            # Create object for current user's portfolio and load values
            
            portfolio = db.execute("SELECT * FROM history WHERE user = :user", user = user)
            userData = loadTickers(portfolio)
            
            # Insert a new purchase into history
            
            newPurchase = db.execute("INSERT INTO history (ticker, num_shares_purchased, current_share_price, total_purchase, user)\
            VALUES (:ticker, :shares, :price, :total, :user)", ticker = ticker, shares = shares, price = stock["price"],\
            total = total, user = user)
            
            # Update user's balance after purchase
            
            balance = db.execute("UPDATE users SET cash = :newBalance WHERE id = :id ", newBalance = newBalance , id = user)
            
            # Calculate values
            
            if not ticker in userData:
                total_val = int(shares)*int(stock["price"])
                # Insert stock into current user's portfolio
                varOne = db.execute("INSERT INTO portfolio (user, ticker, num_shares_owned, current_price, total_value)\
                VALUES (:user, :ticker, :shares, :price, :value)",\
                user = user, ticker = ticker, shares = shares, price = stock["price"], value = total_val)
            else:
                portfolio = db.execute("SELECT * FROM history WHERE user = :user", user = user)
                userData = loadTickers(portfolio)
                total_val = int(userData[ticker])*int(stock["price"])
                # Update portfolio to reflect new holdings
                varTwo = db.execute("UPDATE portfolio SET total_value = :value WHERE user = :user AND\
                ticker = :ticker", user = user, ticker = ticker, value = total_val)
                varThree = db.execute("UPDATE portfolio SET num_shares_owned = :shares WHERE user = :user AND ticker = :ticker",\
                user = user, ticker = ticker, shares = userData[ticker])
            
            # Redirect user to their portfolio page
            
            #portfolioTwo = db.execute("SELECT * FROM portfolio WHERE user = :user", user = user)
            
            #return render_template("portfolio.html", portfolio = portfolioTwo, user = user, curBal = formattedNewBalance)
            return redirect(url_for("index"))
            
        return apology("You've run out of cash!")
        
    else: 
        return render_template("buy.html")

@app.route("/history")
@login_required
def history():
    user = session["user_id"]
    portfolio = db.execute("SELECT * FROM history WHERE user = :user", user = user)
    users = db.execute("SELECT * FROM users WHERE id = :id", id = user)
    
    for rows in portfolio:
        rows["current_share_price"] = usd(rows["current_share_price"])
        rows["total_purchase"] = usd(rows["total_purchase"])
        
    return render_template("history.html", portfolio = portfolio, user = user, username = users[0]["username"])

@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in."""

    # forget any user_id
    session.clear()

    # if user reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username")

        # ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password")

        # query database for username
        rows = db.execute("SELECT * FROM users WHERE username = :username", username=request.form.get("username"))

        # ensure username exists and password is correct
        if len(rows) != 1 or not pwd_context.verify(request.form.get("password"), rows[0]["hash"]):
            return apology("invalid username and/or password")

        # remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # redirect user to home page
        return redirect(url_for("index"))

    # else if user reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")

@app.route("/logout")
def logout():
    """Log user out."""

    # forget any user_id
    session.clear()

    # redirect user to login form
    return redirect(url_for("login"))

@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    if request.method == "POST":
        
        # Make sure input is entered
        if not request.form.get("ticker"):
            return apology("Please enter a", "Ticker Symbol!")
            
        # Make sure input is valid
        ticker = lookup(request.form.get("ticker"))
        price = usd(ticker["price"])
        if ticker == None:
            return apology("Sorry this isn't a stock...", "Or you entered it wrong!")
        
        return render_template("quoted.html", ticker = ticker, price = price)
    else:
        return render_template("quote.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
    
        # ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username")

        # ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password")
            
        # check to make sure both password fields match
        
        elif not request.form.get("password") == request.form.get("passwordConfirm"):
            return apology("passwords don't match")
            
        # make sure user doesn't already exist
        
        rows = db.execute("SELECT * FROM users WHERE username = :username", username=request.form.get("username"))
        
        if len(rows): 
            return apology("You already have an account!", "Can't you remember?")
            
        # insert new user into database
        hash = pwd_context.hash(request.form.get("password"))
        result = db.execute("INSERT INTO users (username, hash) VALUES (:username, :hash)",\
        username = request.form.get("username"), hash = hash)
        
        if not result:
            return apology("Sorry", "Couldn't add you to the database")
        else:
            # query database for newly created username
            rows = db.execute("SELECT * FROM users WHERE username = :username", username=request.form.get("username"))
            # remember which user has logged in
            session["user_id"] = rows[0]["id"]
            return redirect(url_for("index"))
            
    else:
        return render_template("register.html")

@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    
    if request.method == "POST":
        
        user = session["user_id"]
        # load the current portfolio 
        
        portfolio = db.execute("SELECT * FROM history WHERE user = :user", user = user)
        userData = loadTickers(portfolio)
        
        # Define variables for database insertion
        
        stock = lookup(request.form.get("ticker"))
        ticker = request.form.get("ticker")
        shares = request.form.get("numShares")
        sellVal = int(shares)*int(stock["price"])
        
        # load portfolio and variables
        
        portfolio = db.execute("SELECT * FROM portfolio WHERE user = :user AND ticker = :ticker", user = user, ticker = ticker)
        
        num_shares = portfolio[0]["num_shares_owned"]
        current_price = portfolio[0]["current_price"]
        previous_val = portfolio[0]["total_value"]
        
        # Check for inputs
        
        if not ticker or stock == None or not ticker in userData:
            return apology("Must enter", "valid ticker that you own")
        if not shares or int(shares) < 0:
            return apology("Must enter", "positive number of shares to sell")
            
        total_val = int(previous_val) - int(sellVal)
        total_shares = int(num_shares) - int(shares)
            
        # look up users 
        users = db.execute("SELECT cash FROM users WHERE id = :id", id = user)
        currentCash = users[0]["cash"]
        newCash = int(currentCash) + int(sellVal)
        
        # if selling all shares
        if int(num_shares) == int(shares):
            one = db.execute("DELETE FROM portfolio WHERE user = :user AND ticker = :ticker", ticker = ticker, user = user)
        # if selling some but not all shares 
        elif int(num_shares) < int(shares):
            return apology("You can't sell more shares than you have")
        else:
            two = db.execute("UPDATE portfolio SET total_value = :value WHERE user = :user AND ticker = :ticker",\
            user = user, ticker = ticker, value = total_val)
            three = db.execute("UPDATE portfolio SET num_shares_owned = :shares WHERE user = :user AND ticker = :ticker",\
            user = user, ticker = ticker, shares = total_shares)
        
        # Update user's cash balance
        four = db.execute("INSERT INTO history (ticker, num_shares_purchased, current_share_price, total_purchase, user, buy_or_sell)\
        VALUES (:ticker, :shares, :price, :total, :user, :sell)", ticker = ticker, shares = shares, price = stock["price"],\
        total = sellVal, user = user, sell = "sell")
        
        five = db.execute("UPDATE users SET cash = :cash WHERE id = :id", cash = newCash, id = user)
        
        return redirect(url_for("index"))
    else:
        return render_template("sell.html")
        
@app.route("/deposit", methods=["GET", "POST"])
@login_required
def deposit():
    
    if request.method == "POST":
        user = session["user_id"]
        addMoney = request.form.get("deposit")
        
        users = db.execute("SELECT cash FROM users WHERE id = :id", id = user)
        
        currentCash = users[0]["cash"]
        
        total = int(addMoney) + int(currentCash)
        
        add = db.execute("UPDATE users SET cash = :cash WHERE id = :id", cash = total, id = user)
        
        return redirect(url_for("index"))
    else: 
        return render_template("deposit.html")
