import os

class Config(object):
    def __init__(self):
        is_production = os.environ['SERVER_ENV'] == 'production'
        self._config = dict(
            debug                   = not is_production,
            static_dir              = 'static',
            test_dir                = 'data/test_runner',
            run_tests_scipt         = 'run_tests.py',
            rest_server_host        = 'localhost',
            rest_server_port        = 5432,
            mongo_connection_string = 'mongodb://localhost:27017/'
        )

    def __getitem__(self, attr_name):
        return self._config[attr_name]

    def __getattr__(self, attr_name):
        return self._config[attr_name]

config = Config()
