import pymongo
if __name__=='__main__':
    client =pymongo.MongoClient('mongodb://localhost:27017')
    print(client)
    db = client['madhav']
    collection = db['Thisistryal']
    mydict = {'one':'two','ew':'e','oene':'tewo','onee':'tweo'}
    collection.insert_one(mydict)
    # collection.insert_one({'two':'one'})
    # collection.insert_one({'siz':'five'})
    mylist = [
        {'Name':'Krish','Marks':34,'Location':'Mumbai'},
        {'Name':'ram','Marks':54,'Location':'Cheannai'},
        {'Name':'siddhesh','Marks':37,'Location':'Madras'},
    ]
    collection.insert_many(mylist)

