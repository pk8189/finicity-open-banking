"""File Generated by Sideko (sideko.dev)"""

from __future__ import annotations
import io
import typing
import pydantic
import typing_extensions

HttpxFile = typing.Tuple[str, typing.Union[typing.BinaryIO, io.BufferedReader]]


class TestTxPushTransaction(typing_extensions.TypedDict):
    """
    A fake transaction for TxPush testing
    """

    amount: typing_extensions.Required[float]
    description: typing_extensions.Required[str]
    posted_date: typing_extensions.NotRequired[int]
    status: typing_extensions.NotRequired[str]
    transaction_date: typing_extensions.Required[int]


class _SerializerTestTxPushTransaction(pydantic.BaseModel):
    """
    Serializer for TestTxPushTransaction handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    amount: float = pydantic.Field(alias="amount")
    description: str = pydantic.Field(alias="description")
    posted_date: typing.Optional[int] = pydantic.Field(alias="postedDate", default=None)
    status: typing.Optional[str] = pydantic.Field(alias="status", default=None)
    transaction_date: int = pydantic.Field(alias="transactionDate")
