from __future__ import annotations

from mcp.server.fastmcp import FastMCP

from app.config.logger_config import get_rich_logger
from app.config.settings import settings
from app.mcp.loader import load_tools

log = get_rich_logger()


def create_mcp_app():
    mcp = FastMCP(settings.app_name)
    load_tools(mcp)
    app = mcp.streamable_http_app()  # FastMCP ASGI
    log.info("[mcp] server initialized")
    return app


app = create_mcp_app()
