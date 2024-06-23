import typing as t
import re
import string

from mashumaro.jsonschema.annotations import Pattern, Minimum
from softy.types import URI, Email as _Email

RUSSIAN_LETTERS = "йцукенгшщзхъфывапролджэячсмитьбю"
RUSSIAN_LETTERS += RUSSIAN_LETTERS.upper()
DISPLAYABLE_WITHOUT_NEWLINE = RUSSIAN_LETTERS + string.ascii_letters + string.digits + " "
DISPLAYABLE = DISPLAYABLE_WITHOUT_NEWLINE = "\n"

def any_of_regex(*values: str) -> str:
    return '(' + '|'.join(map(re.escape, values)) + ')'

Slug: t.TypeAlias = t.Annotated[str, Pattern(r"[a-zA-Z][a-zA-Z_\-\d]*")]
UInt: t.TypeAlias = t.Annotated[int, Minimum(0)]
DisplayableText: t.TypeAlias = t.Annotated[str, any_of_regex(*DISPLAYABLE)]
DisplayableLine: t.TypeAlias = t.Annotated[str, any_of_regex(*DISPLAYABLE_WITHOUT_NEWLINE)]
Image: t.TypeAlias = URI
Email: t.TypeAlias = _Email

__all__ = [
    "Slug",
    "UInt",
    "DisplayableText",
    "Image",
    "any_of_regex",
]

