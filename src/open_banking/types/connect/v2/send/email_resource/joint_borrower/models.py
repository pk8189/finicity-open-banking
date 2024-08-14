"""File Generated by Sideko (sideko.dev)"""

import io
import typing


import pydantic

ModelFiles = typing.List[
    typing.Tuple[str, typing.Union[typing.BinaryIO, io.BufferedReader]]
]


class EmailOptions(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    first_name: typing.Optional[str] = pydantic.Field(alias="firstName", default=None)
    from_field: typing.Optional[str] = pydantic.Field(alias="from", default=None)
    institution_address: typing.Optional[str] = pydantic.Field(
        alias="institutionAddress", default=None
    )
    institution_name: typing.Optional[str] = pydantic.Field(
        alias="institutionName", default=None
    )
    signature: typing.Optional[typing.List[str]] = pydantic.Field(
        alias="signature", default=None
    )
    subject: typing.Optional[str] = pydantic.Field(alias="subject", default=None)
    support_phone: typing.Optional[str] = pydantic.Field(
        alias="supportPhone", default=None
    )
    to: str = pydantic.Field(alias="to")


class ConnectEmailUrl(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    email_config: EmailOptions = pydantic.Field(alias="emailConfig")
    link: str = pydantic.Field(alias="link")