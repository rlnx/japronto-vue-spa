from japronto import Application
from config import cfg
from static import file_cache

app = Application()

def route(url, method='GET'):
    def add_handler(handler):
        app.router.add_route(url, handler, method=method)
        return handler
    return add_handler

@route('/')
def index(request):
    return file_cache.html(request, 'build/app.html')

@route('/app.bin')
def assets_js(request):
    return file_cache.js(request, 'build/app.js')

@route('/suites/list')
def suite_append(request):
    return request.Response(json=[
        { 'id': 0, 'name': 'Predefined test suite',
          'command': 'python3 run-my-ugly-script.py' }
    ])

@route('/suites/append')
def suite_append(request):
    return request.Response(json={ 'id': 0 })

@route('/suites/update', method='POST')
def suite_append(request):
    suite_id = request.json['id']
    command  = request.json['cmd']
    return request.Response(json={ 'status': 'ok' })

@route('/runs/list')
def suite_append(request):
    return request.Response(json=[
        { 'id': 0, 'suiteId': 0,
          'suiteName': 'Predefined test suite',
          'passRate': '10/10', 'status': 'finished' },
        { 'id': 1, 'suiteId': 0,
          'suiteName': 'Predefined test suite',
          'passRate': '8/10', 'status': 'failed' }
    ])

@route('/runs/start/{id}')
def suite_append(request):
    suite_id = request.match_dict['id']
    return request.Response(json={ 'id': 0 })


app.run(debug=cfg.debug, host=cfg.host, port=cfg.port)
