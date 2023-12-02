from typing import Optional


class EnkaNetworkException(Exception):
    """Base class for EnkaNetwork errors."""


class NetworkError(EnkaNetworkException):
    """Base class for exceptions due to networking errors."""


class TimedOut(NetworkError):
    """Raised when a request took too long to finish."""


class ValidateUIDError(EnkaNetworkException):
    """Raised when the UID is not valid."""


class BadRequest(EnkaNetworkException):
    """Raised when an API request cannot be processed correctly."""

    status_code: int
    message: str

    def __init__(self, message: Optional[str] = None, status_code: Optional[int] = None, **kwargs) -> None:
        if self.message is not None:
            self.message = message
        if self.status_code is not None:
            self.status_code = status_code
        if kwargs:
            self.message = self.message.format(**kwargs)


class EnkaServerError(BadRequest):
    """Exception that's raised for when status code 500 occurs."""

    status_code = 500
    message = "Enka.network server has down or Genshin server broken."


class EnkaServerMaintenance(BadRequest):
    """Exception that's raised when status code 424 occurs."""

    status_code = 424
    message = "Enka.Network doing maintenance server. Please wait took 5-8 hours or 1 day"


class EnkaServerRateLimit(BadRequest):
    """Exception that's raised when status code 429 occurs."""

    status_code = 429
    message = "Enka.network has been rate limit this path"


class EnkaServerUnknown(BadRequest):
    """Exception that's raised when status code 503 occurs."""

    status_code = 429
    message = "I screwed up massively"


class EnkaValidateUIDError(BadRequest, ValidateUIDError):
    """Raised when the UID is not valid."""

    status_code = 400
    message = "Validate UID {uid} failed."


class EnkaPlayerNotFound(BadRequest):
    """Raised when the UID is not found."""

    status_code = 404
    message = "Player ID {uid} not found. Please check your UID / Username"


ERROR_MAP = {
    400: EnkaValidateUIDError,
    404: EnkaPlayerNotFound,
    429: EnkaServerRateLimit,
    424: EnkaServerMaintenance,
    500: EnkaServerError,
    503: EnkaServerUnknown,
}
