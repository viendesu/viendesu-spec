import dataclasses as dtc
import typing as t
from enum import StrEnum, auto

from viendesu.schemas import (
    Email,
    UInt,
    Image,
    Slug,
    DisplayableText,
    DisplayableLine,
)
from softy.types import Date

from mashumaro.jsonschema.annotations import Maximum, MaxLength

Id: t.TypeAlias = t.Annotated[UInt, Maximum(2**32 - 1)]
Username: t.TypeAlias = t.Annotated[Slug, MaxLength(64)]
Bio: t.TypeAlias = t.Annotated[DisplayableText, MaxLength(1024)]
Name: t.TypeAlias = t.Annotated[DisplayableLine, MaxLength(256)]


class Role(StrEnum):
    OWNER = auto()
    ADMIN = auto()
    MODERATOR = auto()
    USER = auto()


@dtc.dataclass
class Additional:
    role: Role
    created_at: Date
    verified_at: Date | None = None
    banned_at: Date | None = None


@dtc.dataclass
class User:
    id: Id
    username: Username

    email: Email | None = None
    name: Name | None = None
    avatar: Image | None = None
    cover: Image | None = None
    bio: Bio | None = None
    additional: Additional | None = None

