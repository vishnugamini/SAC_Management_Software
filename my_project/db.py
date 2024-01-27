from pymongo import MongoClient
client = MongoClient("mongodb://localhost:27017")
db = client['SAC_Regestration']
collection = db['Badminton_Booking']
# Insert a single document into the collection
# document = {"registration_number": "21BCE8834", "slot": "3:00pm - 3:40pm"}
# print(collection.insert_one(document))

x = collection.find({"registration_number":"21BCE8834"})
for y in x:
    print(y)
client.close()
