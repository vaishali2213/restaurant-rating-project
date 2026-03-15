from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/submit', methods=['POST'])
def submit():

    restaurant = request.form['restaurant']
    food = request.form['food']
    cost = request.form['cost']
    rating = request.form['rating']
    review = request.form['review']

    conn = sqlite3.connect("reviews.db")
    cur = conn.cursor()

    cur.execute("INSERT INTO reviews VALUES (?,?,?,?,?)",
                (restaurant, food, cost, rating, review))

    conn.commit()
    conn.close()

    return "Review Submitted Successfully!"

@app.route('/reviews')
def reviews():

    conn = sqlite3.connect("reviews.db")
    cur = conn.cursor()

    cur.execute("SELECT * FROM reviews")
    data = cur.fetchall()

    conn.close()

    return render_template("reviews.html", reviews=data)

if __name__ == '_main_':
    app.run(debug=True)