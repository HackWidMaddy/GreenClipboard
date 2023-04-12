import pymongo
if __name__=='__main__':
    client =pymongo.MongoClient('mongodb://localhost:27017')
    print(client)
    db = client['madhav']
    collection = db['Thisistryal']
    prev = {'Name':'ram'}
    nextt = {'$set':{'Marks':100}}
    a = collection.update_many(prev,nextt)
    print(a.modified_count)
