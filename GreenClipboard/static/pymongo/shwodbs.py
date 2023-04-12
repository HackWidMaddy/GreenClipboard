import pymongo
if __name__=='__main__':
    client =pymongo.MongoClient('mongodb://localhost:27017')
    print(client)
    db = client['madhav']
    collection = db['Thisistryal']
    a = client.list_database_names()
    print(a)
    