import json
from pymongo import MongoClient
from bson.objectid import ObjectId

_mongo = MongoClient('mongodb://localhost:27017/')
_suites     = _mongo.test_runner.suites
_suite_runs = _mongo.test_runner.suite_runs

class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        if isinstance(o, StoreObject):
            return o.source()
        return json.JSONEncoder.default(self, o)

class StoreObject(object):
    def __init__(self, **mongodict):
        self.__dict__ = mongodict

    def json(self):
        return JSONEncoder().encode(self.__dict__)

    def source(self):
        return self.__dict__

    def delete_key(self, key):
        self.__dict__.pop(key, None)
        return self

    def copy(self):
        return StoreObject(**( self.__dict__.copy() ))

    def __str__(self):
        return str(self.__dict__)

class StoreList(object):
    def __init__(self, objlist):
        self._list = self._wrap_objects(objlist)

    def json(self):
        return JSONEncoder().encode(self._list)

    def source(self):
        return self._list

    def __getitem__(self, index):
        return self._list[index]

    def __setitem__(self, idnex, value):
        self._list[index] = value

    def __iter__(self):
        return iter(self._list)

    def __str__(self):
        return str(self._list)

    def _wrap_objects(self, json_list):
        return [StoreObject(**o) for o in json_list]

async def get_suite(id):
    return StoreObject( **_suites.find_one({'_id': ObjectId(id) }) )

async def get_all_suites():
    return StoreList(_suites.find())

async def save_suite(suite):
    assert isinstance(suite, StoreObject)
    suite._id = _suites.insert_one(suite.source()).inserted_id
    return suite

async def get_all_suite_runs():
    return StoreList(_suite_runs.find())

async def save_suite_run(suite_run):
    assert isinstance(suite_run, StoreObject)
    suite_run._id = _suite_runs.insert_one(suite_run.source()).inserted_id
    return suite_run

async def update_suite_runs(patches):
    for patch in patches:
        patch_id   = ObjectId(patch._id)
        patch_copy = patch.copy().delete_key('_id')
        _suite_runs.update(
            { '_id': patch_id },
            { '$set': patch_copy.source() }
        )
