"""Public exception hierarchy for the TikTok Shop GMV Analyzer SDK."""

class TikTokShopGmvAnalyzerError(Exception):
    """Base SDK error."""

class AuthenticationError(TikTokShopGmvAnalyzerError):
    """The Apify token is missing or rejected."""

class ActorRunError(TikTokShopGmvAnalyzerError):
    """The Actor run or Dataset request failed."""

class ActorTimeoutError(TikTokShopGmvAnalyzerError):
    """The client stopped waiting before the Actor completed."""
