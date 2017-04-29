import store

async def create_suite_run(suite):
    suite_run = store.SuiteRun(
        suiteId   = suite.id,
        suiteName = suite.name,
        status    = 'pending',
        passRate  = 'N/A'
    )
    return await store.insert_suite_run(suite_run)

async def create_suite_run_patches(tests):
    patches = []
    for test in tests:
        suite_run_patch = dict(
            id       = test.id,
            status   = await test.status(),
            passRate = await test.pass_rate()
        )
        patches.append(suite_run_patch)
    return patches
