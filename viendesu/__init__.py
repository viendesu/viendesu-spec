from softy import Context
from softy.comb import path, tags, seq

from openapify.core.models import RouteDef


def routes(ctx: Context) -> tuple[RouteDef, ...]:
    from . import (
        users,
    )

    users = seq(path('/users'), tags("users"))(users.routes)

    return (
        *users(ctx),
    )


__all__ = ["routes"]

