import typing as t

from .context import Context

from openapify.core.models import RouteDef


class Handler(t.Protocol):
    def __call__(self, ctx: Context, /) -> tuple[RouteDef, ...]:
        ...


__all__ = ["Handler"]

