from pymongo import MongoClient, ASCENDING


class DataBase(object):
    HOST = 'mongodb://105.103.67.61:27017/'
    replicaSet = "rs0"
    db = MongoClient(HOST, replicaSet=replicaSet)['requirement']

def returnElementsFromCL(cl):
    ims_ml_collection = DataBase.db.machine_learning_cls
    product_owner = ims_ml_collection.find({'Cl': cl}, {'Description': True, '_id': False})
    result = []
    for prod in product_owner:
        result.append(dict(prod))
    return result

def returnElements(query):
    ims_ml_collection = DataBase.db.machine_learning_cls
    product_owner = ims_ml_collection.find({}, {'Description': True, '_id': False})
    result = []
    for prod in product_owner:
        result.append(prod['Description'])
    return result
