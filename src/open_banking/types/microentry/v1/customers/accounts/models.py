"""File Generated by Sideko (sideko.dev)"""

import io
import typing


import pydantic

ModelFiles = typing.List[
    typing.Tuple[str, typing.Union[typing.BinaryIO, io.BufferedReader]]
]


class MicroDepositDetails(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    account_number_last4: typing.Optional[str] = pydantic.Field(
        alias="accountNumberLast4", default=None
    )
    creation_date: typing.Optional[str] = pydantic.Field(
        alias="creationDate", default=None
    )
    routing_number: typing.Optional[str] = pydantic.Field(
        alias="routingNumber", default=None
    )
    status: typing.Optional[str] = pydantic.Field(alias="status", default=None)
    status_description: typing.Optional[str] = pydantic.Field(
        alias="statusDescription", default=None
    )