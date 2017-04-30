import store

async def create_suite(name, command):
    suite = store.StoreObject(
        name    = name,
        command = command
    )
    return await store.save_suite(suite)

def create_suite_patch(id, command):
    suite_patch = store.StoreObject(
        _id     = id,
        command = command
    )
    return suite_patch

async def create_suite_run(suite):
    suite_run = store.StoreObject(
        suiteId   = suite._id,
        suiteName = suite.name,
        status    = 'pending',
        passRate  = 'N/A'
    )
    return await store.save_suite_run(suite_run)

async def create_suite_run_patches_from_tests(tests):
    patches = []
    for test in tests:
        suite_run_patch = store.StoreObject(
            _id      = test.id,
            status   = await test.status(),
            passRate = await test.pass_rate()
        )
        patches.append(suite_run_patch)
    return patches
