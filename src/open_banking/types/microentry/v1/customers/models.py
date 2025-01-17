"""File Generated by Sideko (sideko.dev)"""

import io
import typing


import pydantic

ModelFiles = typing.List[
    typing.Tuple[str, typing.Union[typing.BinaryIO, io.BufferedReader]]
]


class InitiatedMicroDeposit(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    account_id: typing.Optional[str] = pydantic.Field(alias="accountId", default=None)
    deposit_count: typing.Optional[int] = pydantic.Field(
        alias="depositCount", default=None
    )
    status: typing.Optional[str] = pydantic.Field(alias="status", default=None)
    status_description: typing.Optional[str] = pydantic.Field(
        alias="statusDescription", default=None
    )
