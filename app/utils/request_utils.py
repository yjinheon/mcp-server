import httpx

ERROR_MESSAGES = {
    404: {
        "error": "Not Found",
        "message": "The requested resource could not be found.",
    },
    422: {"error": "Unprocessable Content", "message": "The request data is invalid."},
    500: {
        "error": "Internal Server Error",
        "message": "An unexpected error occurred on the server.",
    },
    502: {
        "error": "Bad Gateway",
        "message": "The server received an invalid response from the upstream server.",
    },
}


async def make_api_request(method: str, endpoint: str, data=None):
    async with httpx.AsyncClient(timeout=10.0) as client:
        try:
            response = await client.request(method, endpoint, json=data)
            response.raise_for_status()
            return response.json()

        except httpx.HTTPStatusError as e:
            status_code = e.response.status_code
            if status_code in ERROR_MESSAGES:
                return ERROR_MESSAGES[status_code]
            else:
                return {
                    "error": f"HTTP {status_code}",
                    "message": "An unexpected HTTP error occurred.",
                }
        except httpx.RequestError as e:
            return {"error": "Request Error", "message": str(e)}
