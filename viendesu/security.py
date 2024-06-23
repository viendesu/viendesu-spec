from openapify.core.openapi.models import (
    APIKeySecurityScheme,
    SecurityScheme,
    SecuritySchemeAPIKeyLocation,
)

SECURITY_SCHEMES: dict[str, SecurityScheme] = {
    "token": APIKeySecurityScheme(name="access_token", location=SecuritySchemeAPIKeyLocation.COOKIE),
    "captcha": APIKeySecurityScheme(name="X-Captcha-Token", location=SecuritySchemeAPIKeyLocation.HEADER),
}

__all__ = ["SECURITY_SCHEMES"]

