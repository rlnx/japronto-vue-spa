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
    return request.Response(text=file_cache.app_container, mime_type='text/html')

app.run(debug=cfg.debug, host=cfg.host, port=cfg.port)
