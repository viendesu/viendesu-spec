from softy import Context
from softy.comb import seq, path

from openapify.core.models import RouteDef


def routes(ctx: Context) -> tuple[RouteDef, ...]:
    from . import (
        get,
    )

    get = seq(path("/"))(get.routes)
    
    return (
        *get(ctx),
    )

__all__ = ["routes"]

