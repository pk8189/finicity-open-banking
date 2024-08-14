"""File Generated by Sideko (sideko.dev)"""

from __future__ import annotations
import io
import typing
import pydantic
import typing_extensions

HttpxFile = typing.Tuple[str, typing.Union[typing.BinaryIO, io.BufferedReader]]


class BalanceAndCashFlowAnalyticsReportConstraints(typing_extensions.TypedDict):
    """
    Request parameters from the partner to control the customer accounts included in the report, and the length of time to report on.
    """

    account_ids: typing_extensions.NotRequired[typing.List[int]]
    length_of_report: typing_extensions.NotRequired[int]


class _SerializerBalanceAndCashFlowAnalyticsReportConstraints(pydantic.BaseModel):
    """
    Serializer for BalanceAndCashFlowAnalyticsReportConstraints handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    account_ids: typing.Optional[typing.List[int]] = pydantic.Field(
        alias="accountIds", default=None
    )
    length_of_report: typing.Optional[int] = pydantic.Field(
        alias="lengthOfReport", default=None
    )
