from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Welcome to the Home Page'

@app.route('/scanning')
def scanning():
    return 'This is the Scanning Page'

@app.route('/court_booking')
def court_booking():
    return 'You are on the Court Booking Page'

@app.route('/equipment_borrowing')
def equipment_borrowing():
    return 'Explore the Equipment Borrowing Page'

if __name__ == '__main__':
    app.run(debug=True)
