from logging import getLogger

from app.config.settings import APP_NAME

log = getLogger(APP_NAME)  # 처음에 초기화한 logger


def register(mcp):
    @mcp.tool()
    def hello(name: str = "world") -> str:
        log.info(f"[tool] hello name : {name}")
        return f"Hello, {name}!"
