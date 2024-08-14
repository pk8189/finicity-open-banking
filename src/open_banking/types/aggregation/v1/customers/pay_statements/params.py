"""File Generated by Sideko (sideko.dev)"""

from __future__ import annotations
import io
import typing
import pydantic
import typing_extensions

HttpxFile = typing.Tuple[str, typing.Union[typing.BinaryIO, io.BufferedReader]]


class PayStatement(typing_extensions.TypedDict):
    """
    A pay statement document and pay statement label
    """

    label: typing_extensions.Required[str]
    statement: typing_extensions.Required[str]


class _SerializerPayStatement(pydantic.BaseModel):
    """
    Serializer for PayStatement handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    label: str = pydantic.Field(alias="label")
    statement: str = pydantic.Field(alias="statement")