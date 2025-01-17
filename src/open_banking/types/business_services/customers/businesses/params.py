"""File Generated by Sideko (sideko.dev)"""

from __future__ import annotations
import io
import typing
import pydantic
import typing_extensions

HttpxFile = typing.Tuple[str, typing.Union[typing.BinaryIO, io.BufferedReader]]


class NewAddress(typing_extensions.TypedDict):
    """
    No description specified
    """

    address_line1: typing_extensions.NotRequired[str]
    address_line2: typing_extensions.NotRequired[str]
    city: typing_extensions.NotRequired[str]
    country: typing_extensions.NotRequired[str]
    postal_code: typing_extensions.NotRequired[str]
    state: typing_extensions.NotRequired[str]


class _SerializerNewAddress(pydantic.BaseModel):
    """
    Serializer for NewAddress handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    address_line1: typing.Optional[str] = pydantic.Field(
        alias="addressLine1", default=None
    )
    address_line2: typing.Optional[str] = pydantic.Field(
        alias="addressLine2", default=None
    )
    city: typing.Optional[str] = pydantic.Field(alias="city", default=None)
    country: typing.Optional[str] = pydantic.Field(alias="country", default=None)
    postal_code: typing.Optional[str] = pydantic.Field(alias="postalCode", default=None)
    state: typing.Optional[str] = pydantic.Field(alias="state", default=None)


class PhoneNumberFormat(typing_extensions.TypedDict):
    """
    No description specified
    """

    country_code: typing_extensions.NotRequired[str]
    phone_no: typing_extensions.NotRequired[str]


class _SerializerPhoneNumberFormat(pydantic.BaseModel):
    """
    Serializer for PhoneNumberFormat handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    country_code: typing.Optional[str] = pydantic.Field(
        alias="countryCode", default=None
    )
    phone_no: typing.Optional[str] = pydantic.Field(alias="phoneNo", default=None)


class NewBusiness(typing_extensions.TypedDict):
    """
    No description specified
    """

    address: typing_extensions.Required[NewAddress]
    email_field: typing_extensions.NotRequired[str]
    name: typing_extensions.Required[str]
    personally_liable: typing_extensions.Required[bool]
    phone_number: typing_extensions.Required[PhoneNumberFormat]
    tax_id: typing_extensions.NotRequired[str]
    type: typing_extensions.NotRequired[str]
    url: typing_extensions.NotRequired[str]


class _SerializerNewBusiness(pydantic.BaseModel):
    """
    Serializer for NewBusiness handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    address: _SerializerNewAddress = pydantic.Field(alias="address")
    email_field: typing.Optional[str] = pydantic.Field(alias="email", default=None)
    name: str = pydantic.Field(alias="name")
    personally_liable: bool = pydantic.Field(alias="personallyLiable")
    phone_number: _SerializerPhoneNumberFormat = pydantic.Field(alias="phoneNumber")
    tax_id: typing.Optional[str] = pydantic.Field(alias="taxId", default=None)
    type: typing.Optional[str] = pydantic.Field(alias="type", default=None)
    url: typing.Optional[str] = pydantic.Field(alias="url", default=None)
