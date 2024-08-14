"""File Generated by Sideko (sideko.dev)"""

import io
import typing


import pydantic

ModelFiles = typing.List[
    typing.Tuple[str, typing.Union[typing.BinaryIO, io.BufferedReader]]
]


class Birthday(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    day_of_month: typing.Optional[int] = pydantic.Field(
        alias="dayOfMonth", default=None
    )
    month: typing.Optional[int] = pydantic.Field(alias="month", default=None)
    year: typing.Optional[int] = pydantic.Field(alias="year", default=None)


class ConsumerEndUser(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
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


class CreatedConsumer(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    created_date: typing.Optional[int] = pydantic.Field(
        alias="createdDate", default=None
    )
    customer_id: typing.Optional[int] = pydantic.Field(alias="customerId", default=None)
    id: typing.Optional[str] = pydantic.Field(alias="id", default=None)


class Consumer(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    address: str = pydantic.Field(alias="address")
    birthday: Birthday = pydantic.Field(alias="birthday")
    city: str = pydantic.Field(alias="city")
    created_date: int = pydantic.Field(alias="createdDate")
    customer_id: int = pydantic.Field(alias="customerId")
    email_field: str = pydantic.Field(alias="email")
    end_user: typing.Optional[ConsumerEndUser] = pydantic.Field(
        alias="endUser", default=None
    )
    first_name: str = pydantic.Field(alias="firstName")
    id: str = pydantic.Field(alias="id")
    last_name: str = pydantic.Field(alias="lastName")
    phone: str = pydantic.Field(alias="phone")
    ssn: str = pydantic.Field(alias="ssn")
    state: str = pydantic.Field(alias="state")
    suffix: typing.Optional[str] = pydantic.Field(alias="suffix", default=None)
    zip: str = pydantic.Field(alias="zip")
