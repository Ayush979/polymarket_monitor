class PolymarketException(Exception):
    """Base Polymarket exception."""


class PolymarketAPIError(PolymarketException):
    """Raised when the API returns an error."""


class PolymarketTimeout(PolymarketException):
    """Raised when a request times out."""