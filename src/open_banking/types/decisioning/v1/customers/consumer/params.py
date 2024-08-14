"""File Generated by Sideko (sideko.dev)"""

from __future__ import annotations
import io
import typing
import pydantic
import typing_extensions

HttpxFile = typing.Tuple[str, typing.Union[typing.BinaryIO, io.BufferedReader]]


class Birthday(typing_extensions.TypedDict):
    """
    A birth date
    """

    day_of_month: typing_extensions.NotRequired[int]
    month: typing_extensions.NotRequired[int]
    year: typing_extensions.NotRequired[int]


class _SerializerBirthday(pydantic.BaseModel):
    """
    Serializer for Birthday handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    day_of_month: typing.Optional[int] = pydantic.Field(
        alias="dayOfMonth", default=None
    )
    month: typing.Optional[int] = pydantic.Field(alias="month", default=None)
    year: typing.Optional[int] = pydantic.Field(alias="year", default=None)


class ConsumerEndUser(typing_extensions.TypedDict):
    """
    Reseller end user information
    """

    address: typing_extensions.Required[str]
    city: typing_extensions.Required[str]
    email_field: typing_extensions.NotRequired[str]
    name: typing_extensions.Required[str]
    phone: typing_extensions.Required[str]
    state: typing_extensions.Required[str]
    url: typing_extensions.Required[str]
    zip: typing_extensions.Required[str]


class _SerializerConsumerEndUser(pydantic.BaseModel):
    """
    Serializer for ConsumerEndUser handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    address: str = pydantic.Field(alias="address")
    city: str = pydantic.Field(alias="city")
    email_field: typing.Optional[str] = pydantic.Field(alias="email", default=None)
    name: str = pydantic.Field(alias="name")
    phone: str = pydantic.Field(alias="phone")
    state: str = pydantic.Field(alias="state")
    url: str = pydantic.Field(alias="url")
    zip: str = pydantic.Field(alias="zip")


class NewConsumer(typing_extensions.TypedDict):
    """
    A new consumer to be created
    """

    address: typing_extensions.Required[str]
    birthday: typing_extensions.Required[Birthday]
    city: typing_extensions.Required[str]
    email_field: typing_extensions.NotRequired[str]
    end_user: typing_extensions.NotRequired[ConsumerEndUser]
    first_name: typing_extensions.Required[str]
    last_name: typing_extensions.Required[str]
    phone: typing_extensions.Required[str]
    ssn: typing_extensions.Required[str]
    state: typing_extensions.Required[str]
    suffix: typing_extensions.NotRequired[str]
    zip: typing_extensions.Required[str]


class _SerializerNewConsumer(pydantic.BaseModel):
    """
    Serializer for NewConsumer handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    address: str = pydantic.Field(alias="address")
    birthday: _SerializerBirthday = pydantic.Field(alias="birthday")
    city: str = pydantic.Field(alias="city")
    email_field: typing.Optional[str] = pydantic.Field(alias="email", default=None)
    end_user: typing.Optional[_SerializerConsumerEndUser] = pydantic.Field(
        alias="endUser", default=None
    )
    first_name: str = pydantic.Field(alias="firstName")
    last_name: str = pydantic.Field(alias="lastName")
    phone: str = pydantic.Field(alias="phone")
    ssn: str = pydantic.Field(alias="ssn")
    state: str = pydantic.Field(alias="state")
    suffix: typing.Optional[str] = pydantic.Field(alias="suffix", default=None)
    zip: str = pydantic.Field(alias="zip")