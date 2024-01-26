from flask import Flask,render_template

app = Flask(__name__,template_folder='pages')

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/scanning')
def scanning():
    return render_template("scanning.html")

@app.route('/court_booking')
def court_booking():
    return render_template("court_booking.html")

@app.route('/equipment_borrowing')
def equipment_borrowing():
    return render_template("equipment_borrowing.html")

if __name__ == '__main__':
    app.run(debug=True)
