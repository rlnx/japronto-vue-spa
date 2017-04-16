import os
from config import cfg

class FileResourceCache(object):
    def __init__(self):
        self._cache = dict()

    def html(self, request, url):
        return self._format_response(request, url, 'text/html')

    def js(self, request, url):
        return self._format_response(request, url, 'text/javascript')

    def load_file(self, resource_name):
        cache = self._cache
        if not cfg.debug:
            if resource_name in cache:
                return cache[resource_name]
        with open(resource_name, 'r') as file:
            file_source = file.read()
        cache[resource_name] = file_source
        return file_source

    def _format_response(self, request, url, mime_type):
        try:
            source = self._load_resource(url)
            return request.Response(text=source, mime_type=mime_type)
        except:
            return request.Response(code=404)

    def _load_resource(self, url):
        path_to_resource = os.path.join(cfg.static_dir, url)
        return self.load_file(path_to_resource)

file_cache = FileResourceCache()
