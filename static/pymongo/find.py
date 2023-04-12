import pymongo
if __name__=='__main__':
    client =pymongo.MongoClient('mongodb://localhost:27017')
    print(client)
    db = client['madhav']
    collection = db['Thisistryal']
    # a = collection.find_one({'Name':'ram'})
    a = collection.find({'Name':'siddhesh','Marks':{'$lte':200}},{'Name':1,'_id':0})
    for i in a:
        print(i)