from contextlib import asynccontextmanager

# 주기적 캐시,  warm-up


@asynccontextmanager
async def noop_lifespan(app):
    # startup
    yield
    # shutdown
