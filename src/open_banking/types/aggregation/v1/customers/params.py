"""File Generated by Sideko (sideko.dev)"""

from __future__ import annotations
import io
import typing
import pydantic
import typing_extensions

HttpxFile = typing.Tuple[str, typing.Union[typing.BinaryIO, io.BufferedReader]]


class CustomerUpdate(typing_extensions.TypedDict):
    """
    Represent an update to customer fields
    """

    first_name: typing_extensions.NotRequired[str]
    last_name: typing_extensions.NotRequired[str]


class _SerializerCustomerUpdate(pydantic.BaseModel):
    """
    Serializer for CustomerUpdate handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    first_name: typing.Optional[str] = pydantic.Field(alias="firstName", default=None)
    last_name: typing.Optional[str] = pydantic.Field(alias="lastName", default=None)