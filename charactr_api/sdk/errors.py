import json


class ConnectionClosedError(Exception):
    def __init__(self):
        super().__init__("Connection is already closed.")


class ClientError(Exception):
    """Exception raised for 4xx http errors"""

    def __init__(self, code: int, message: str):
        super().__init__("[{0}] {1}".format(code, message))


class ServerError(Exception):
    """Exception raised for 5xx http errors"""

    def __init__(self, code: int, message: str = "?"):
        super().__init__("[{0}] {1}".format(code, message))


class UnknownError(Exception):
    """Exception raised for unknown errors"""

    def __init__(self, message: str):
        super().__init__(message)


def get_api_error(response):
    if response.status_code < 400 or response.status_code > 599:
        return UnknownError("unexpected error")

    try:
        err = json.loads(response.content)
    except Exception as e:
        return Exception(e)

    if response.status_code < 500:
        return ClientError(response.status_code, err.get("message", "unexpected error"))

    return ServerError(response.status_code, err.get("message", "unexpected error"))
