from typing import Any

import httpx

from app.config.settings import CALLBACK_URL


# simple callback test
def register(mcp):
    @mcp.tool()
    async def send_callback(
        task_id: str, data: dict[str, Any] | None = None
    ) -> dict[str, Any]:
        payload = {"task_id": task_id, "data": data or {}}
        try:
            async with httpx.AsyncClient(timeout=10.0) as client:
                resp = await client.post(CALLBACK_URL, json=payload)
            return {
                "ok": resp.is_success,
                "status_code": resp.status_code,
                "response_preview": resp.text[:500],
                "callback_url": CALLBACK_URL,
            }
        except Exception as e:
            return {"ok": False, "error": str(e), "callback_url": CALLBACK_URL}
