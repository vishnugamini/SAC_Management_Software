import time
from pymongo import MongoClient
client = MongoClient("mongodb://localhost:27017")
db = client['SAC_Regestration']
collection = db['Badminton_Booking']

def wait_time(time_in_minutes,reg_number):
    print("timer started")
    time.sleep(time_in_minutes * 60)
    delete(reg_number)
def delete(reg_number):
    print(collection.delete_one({"registration_number":reg_number}))

    