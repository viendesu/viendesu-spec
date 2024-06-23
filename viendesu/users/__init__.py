from softy import Context
from softy.comb import (
    path,
    seq,
    parameter,
)

from openapify.core.models import RouteDef

from .schemas import user

def routes(ctx: Context) -> tuple[RouteDef, ...]:
    from . import (
        specific,
    )

    specific = seq(path("/{id}"), parameter("id", user.Id | user.Username, "ID or slug of the user"))(specific.routes)
    return (
        *specific(ctx),
    )


__all__ = ["routes"]

