from config import cfg

class FileResourceCache(object):
    def __init__(self):
        self._cache = dict()

    def load_file(self, resource_name):
        cache = self._cache
        if resource_name in cache:
            return cache[resource_name]
        with open(cfg[resource_name], 'r') as file:
            file_source = file.read()
        cache[resource_name] = file_source
        return file_source

    def __getattr__(self, resource_name):
        return self.load_file(resource_name)

file_cache = FileResourceCache()
