from pymongo import MongoClient
client = MongoClient("mongodb://localhost:27017")
db = client['SAC_booking_system']
collection = db['Badminton_Court']
# Insert a single document into the collection
document = {"Name": "Danny", "Start_time": "3:00pm"}
x = collection.find({"Name":"Vishnu"})
for y in x:
    print(y)
client.close()
