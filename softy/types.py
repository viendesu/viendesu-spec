import typing as t

from mashumaro.jsonschema.models import JSONSchemaStringFormat

Email: t.TypeAlias = t.Annotated[str, JSONSchemaStringFormat.EMAIL]
URI: t.TypeAlias = t.Annotated[str,JSONSchemaStringFormat.URI]
Date: t.TypeAlias = t.Annotated[str,JSONSchemaStringFormat.DATETIME]

__all__ = ["Email", "URI", "Date"]
