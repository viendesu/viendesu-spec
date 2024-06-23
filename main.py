from openapify import build_spec

import viendesu
from viendesu.security import SECURITY_SCHEMES

from softy.context import Context


ctx = Context()
routes = viendesu.routes(ctx)

spec = build_spec(
    title="VienDesu! API",
    version="0.1.0",
    servers=["https://api.viende.su"],
    routes=routes,
    security_schemes=SECURITY_SCHEMES,
    plugins=[],
)
print(spec.to_yaml())

