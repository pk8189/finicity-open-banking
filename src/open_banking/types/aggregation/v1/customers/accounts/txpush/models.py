"""File Generated by Sideko (sideko.dev)"""

import io
import typing


import pydantic

ModelFiles = typing.List[
    typing.Tuple[str, typing.Union[typing.BinaryIO, io.BufferedReader]]
]


class SubscriptionRecord(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    account_id: int = pydantic.Field(alias="accountId")
    callback_url: str = pydantic.Field(alias="callbackUrl")
    id: int = pydantic.Field(alias="id")
    signing_key: str = pydantic.Field(alias="signingKey")
    type: str = pydantic.Field(alias="type")


class TxPushSubscriptions(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    subscriptions: typing.List[SubscriptionRecord] = pydantic.Field(
        alias="subscriptions"
    )
