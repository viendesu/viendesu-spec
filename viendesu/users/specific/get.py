from softy import Context

from openapify import request_schema, response_schema
from openapify.core.models import RouteDef

from ..schemas.user import User

@request_schema()
@response_schema(User)
def get(): ...


def routes(ctx: Context) -> tuple[RouteDef, ...]:
    return (
        RouteDef(
            "/", "GET", get,
            description="Get user by id or username",
        ),
    )

__all__ = ["routes"]

