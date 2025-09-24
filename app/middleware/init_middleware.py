import logging
from functools import wraps

from app.config.settings import settings

log = logging.getLogger(settings.app_name)


def tool_logger(func):
    @wraps(func)
    async def aw(*args, **kwargs):
        log.info("→ %s args=%s kwargs=%s", func.__name__, args, kwargs)
        res = (
            await func(*args, **kwargs)
            if callable(getattr(func, "__call__", None))
            and func.__code__.co_flags & 0x80
            else func(*args, **kwargs)
        )
        log.info("← %s result=%s", func.__name__, str(res)[:200])
        return res

    return aw
