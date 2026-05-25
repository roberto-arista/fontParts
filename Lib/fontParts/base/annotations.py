# pylint: disable=C0103, C0114
from __future__ import annotations
from typing import Protocol, TypeVar, Union
import datetime

from fontTools.pens.basePen import AbstractPen
from fontTools.pens.pointPen import AbstractPointPen

T = TypeVar("T")

# Generic numeric scalar.
IntFloatType = int | float

# Generic list-or-tuple — for collections of objects where a domain-specific
# name doesn't apply (e.g. setter inputs that accept either a list or a tuple
# of base objects or indices). Domain-named sequences are defined below.
CollectionType = Union[list[T], tuple[T, ...]]

# 2D point / offset / scale result — (x, y).
Coordinate = tuple[IntFloatType, IntFloatType]
CoordinateLike = list[IntFloatType] | Coordinate

# Bounding box — (xMin, yMin, xMax, yMax).
BoundingBox = tuple[IntFloatType, IntFloatType, IntFloatType, IntFloatType]
BoundingBoxLike = list[IntFloatType] | BoundingBox

# RGBA color tuple — floats in [0, 1] after normalization. (The `Color` class
# in `fontParts.base.color` wraps an `RGBA` to add `.r/.g/.b/.a` accessors.)
RGBA = tuple[float, float, float, float]
ColorLike = (
    list[IntFloatType] | tuple[IntFloatType, IntFloatType, IntFloatType, IntFloatType]
)

# Affine transformation matrix — (xx, xy, yx, yy, dx, dy).
AffineTransformation = tuple[float, float, float, float, float, float]
AffineTransformationLike = (
    list[IntFloatType]
    | tuple[
        IntFloatType,
        IntFloatType,
        IntFloatType,
        IntFloatType,
        IntFloatType,
        IntFloatType,
    ]
)

# Kerning pair — (left, right) glyph or group names.
KerningPair = tuple[str, str]
KerningPairLike = list[str] | KerningPair

# Scale factor input — scalar (uniform) or (sx, sy) (non-uniform).
ScaleFactorLike = IntFloatType | list[IntFloatType] | Coordinate

# Variable-length sequences of names or unicodes.
NameSequence = list[str] | tuple[str, ...]
UnicodeSequence = list[int] | tuple[int, ...]

# Pens.
PenType = AbstractPen
PointPenType = AbstractPointPen

# Mappings.
CharacterMappingType = dict[int, tuple[str, ...]]
ReverseComponentMappingType = dict[str, tuple[str, ...]]

# Flat kerning — (left, right) → value.
KerningDictType = dict[KerningPair, IntFloatType]

# Lib values — primitives plus nested collections.
LibValueType = (
    str
    | IntFloatType
    | bool
    | bytes
    | bytearray
    | datetime.datetime
    | list["LibValueType"]
    | tuple["LibValueType", ...]
    | dict[str, "LibValueType"]
)


class LibValue:
    # Documentation class for LibValueType
    """A :class:`~fontParts.base.BaseLib` value may be one of the following
    *non-collection* types:

    - :class:`str`
    - :class:`int`
    - :class:`float`
    - :class:`bool`
    - :class:`bytes`,
    - :class:`bytearray`
    - :class:`datetime.datetime`

    In addition, a value may also be a :class:`list` or :class:`tuple` containing any of
    the types above, or a :class:`dict` mapping :class:`str` keys to values of those
    same types (including nested lists, tuples, or dicts).

    """


# Interpolation.
InterpolatableType = TypeVar("InterpolatableType", bound="Interpolatable")


class Interpolatable(Protocol):
    """Represent a protocol for interpolatable types."""

    def __add__(
        self: InterpolatableType, other: InterpolatableType
    ) -> InterpolatableType: ...

    def __sub__(
        self: InterpolatableType, other: InterpolatableType
    ) -> InterpolatableType: ...

    def __mul__(
        self: InterpolatableType, other: ScaleFactorLike
    ) -> InterpolatableType: ...
