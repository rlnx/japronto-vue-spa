from japronto import Application
from config import cfg
from static import file_cache

app = Application()

def route(url):
    def add_handler(handler):
        app.router.add_route(url, handler)
        return handler
    return add_handler

@route('/')
def index(request):
    return file_cache.html(request, 'build/app.html')

@route('/app.bin')
def assets_js(request):
    return file_cache.js(request, 'build/app.js')

app.run(debug=cfg.debug, host=cfg.host, port=cfg.port)
