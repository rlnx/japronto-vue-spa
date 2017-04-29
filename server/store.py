from tinydb import TinyDB, Query

_db = TinyDB('test_db.json')
_suites     = _db.table('suites')
_suite_runs = _db.table('suite_runs')

class Suite(object):
    def __init__(self, **kwargs):
        self.id      = kwargs.get('id')
        self.name    = kwargs.get('name')
        self.command = kwargs.get('command')

    def to_json(self):
        return dict(
            id      = self.id,
            name    = self.name,
            command = self.command
        )

class SuiteRun(object):
    def __init__(self, **kwargs):
        self.id         = kwargs.get('id')
        self.suite_id   = kwargs.get('suiteId')
        self.suite_name = kwargs.get('suiteName')
        self.pass_rate  = kwargs.get('passRate')
        self.status     = kwargs.get('status')

    def to_json(self):
        return dict(
            id        = self.id,
            suiteId   = self.suite_id,
            suiteName = self.suite_name,
            passRate  = self.pass_rate,
            status    = self.status
        )

def insert_object(table, obj):
    obj_json = obj.to_json()
    obj_json.pop('id', None)
    obj.id = table.insert(obj_json)
    return obj

def read_object(table, id, Type):
    obj_json = table.get(eid=id)
    if obj_json == None:
        raise Exception('Object with id {} does not exist'.format(id))
    obj_json['id'] = id
    return Type(**obj_json)

def make_explicit_ids(objs_json):
    for obj_json in objs_json:
        obj_json['id'] = obj_json.eid
    return objs_json


async def get_suite(id):
    return read_object(_suites, id, Suite)

async def get_all_suites():
    return make_explicit_ids(_suites.all())

async def get_all_suite_runs_json():
    return make_explicit_ids(_suite_runs.all())

async def insert_suite_run(suite_run):
    return insert_object(_suite_runs, suite_run)

async def update_suite_runs(patches):
    for patch in patches:
        patch_id   = patch['id']
        patch_copy = patch.copy()
        patch_copy.pop('id', None)
        _suite_runs.update(patch_copy, eids=[ patch_id ])
