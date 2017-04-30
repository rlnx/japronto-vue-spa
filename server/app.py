import factory
import store

from config import config
from static import file_cache
from testrunner import test_runner

from japronto import Application
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
async def suite_append(request):
    all_suites = await store.get_all_suites()
    return request.Response(text=all_suites.json(), mime_type='application/json')

@route('/suites/append')
def suite_append(request):
    return request.Response(json={ 'id': 0 })

@route('/suites/update', method='POST')
def suite_append(request):
    suite_id = request.json['_id']
    command  = request.json['cmd']
    return request.Response(json={ 'status': 'ok' })

@route('/runs/list')
async def suite_append(request):
    finished_tests    = test_runner.finished_tests()
    suite_run_patches = await factory.create_suite_run_patches(finished_tests)
    await store.update_suite_runs(suite_run_patches)
    suite_runs = await store.get_all_suite_runs()
    return request.Response(text=suite_runs.json(), mime_type='application/json')

@route('/runs/start/{id}')
async def run_suite(request):
    suite_id  = request.match_dict['id']
    suite     = await store.get_suite(suite_id)
    suite_run = await factory.create_suite_run(suite)
    await test_runner.schedule_test(suite_run._id, suite.command)
    return request.Response(text=suite_run.json(), mime_type='application/json')

app.run(debug=config.debug, host=config.host, port=config.port)
