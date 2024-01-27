from flask import Flask,render_template,request
from resources import wait_timer
import threading
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

@app.route('/start_timer')
def start_timer():
    reg_no = request.args.get('reg_no')
    timer_thread = threading.Thread(target= wait_timer.wait_time(0.5,reg_no))
    timer_thread.start()
    return 'Timer started'
    # if reg_no:
    #     print(f"Received registration number: {reg_no}")
    #     wait_timer.wait_time(0.5,reg_no)
    #     return 'Timer started'
    # else:
    #     return 'Registration number not provided in the URL'
    
if __name__ == '__main__':
    app.run(debug=True)
