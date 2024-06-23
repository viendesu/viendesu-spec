import typing as t
import dataclasses as dtc

from .handler import Handler

from functools import wraps, reduce

from mashumaro.jsonschema import build_json_schema
from openapify.core.models import RouteDef
from openapify.core.openapi.models import Parameter, ParameterLocation

class Combinator(t.Protocol):
    def __call__(self, handler: Handler, /) -> Handler:
        ...

def each_route(f: t.Callable[[RouteDef], RouteDef]) -> Combinator:
    def each_inner(handler: Handler) -> Handler:
        return wraps(handler)(
            lambda ctx: tuple(
                f(route)
                for route in handler(ctx)
            )
        )
    return each_inner

def path(components: str, append: bool = False) -> Combinator:
    components = components.strip('/')

    def join(route: str) -> str:
        route = route.strip('/')
        if append:
            return '/' + route + '/' + components
        else:
            return '/' + components + '/' + route

    return each_route(lambda route: dtc.replace(route, path=join(route.path)))

def tags(*items: str) -> Combinator:
    return each_route(lambda route: dtc.replace(route, tags=[*(route.tags or []), *items]))

def seq(*combs: Combinator) -> Combinator:
    def inner(handler: Handler) -> Handler:
        return reduce(lambda h, comb: comb(h), combs, handler)
    return inner

def parameter(name: str, schema: t.Any, description: str | None = None) -> Combinator:
    return each_route(lambda route: dtc.replace(route, parameters=[
        *(route.parameters or []),
        Parameter(
            name=name,
            description=description,
            schema=build_json_schema(schema).to_dict(),
            location=ParameterLocation.PATH,
        ),
    ]))

__all__ = [
    "Combinator",
    "each_route",
    "path",
    "tags",
    "parameter",
    "seq",
]

