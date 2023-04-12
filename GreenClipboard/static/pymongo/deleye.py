import pymongo
if __name__=='__main__':
    client =pymongo.MongoClient('mongodb://localhost:27017')
    print(client)
    db = client['madhav']
    collection = db['Thisistryal']
    prev = {'Name':'ram'}
    a = collection.delete_one(prev)
    print(a)