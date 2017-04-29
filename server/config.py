
class Config(object):
    def __init__(self):
        self._config = {
            'static_dir': 'static',
            'host': 'localhost',
            'port': 5432,
            'debug': True,
            'test_dir': 'data/test_runner'
        }

    def __getitem__(self, attr_name):
        return self._config[attr_name]

    def __getattr__(self, attr_name):
        return self._config[attr_name]

config = Config()
