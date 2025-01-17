"""File Generated by Sideko (sideko.dev)"""

from __future__ import annotations
import io
import typing
import pydantic
import typing_extensions

HttpxFile = typing.Tuple[str, typing.Union[typing.BinaryIO, io.BufferedReader]]


class ReportCustomField(typing_extensions.TypedDict):
    """
    No description specified
    """

    label: typing_extensions.NotRequired[str]
    shown: typing_extensions.NotRequired[bool]
    value: typing_extensions.NotRequired[str]


class _SerializerReportCustomField(pydantic.BaseModel):
    """
    Serializer for ReportCustomField handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    label: typing.Optional[str] = pydantic.Field(alias="label", default=None)
    shown: typing.Optional[bool] = pydantic.Field(alias="shown", default=None)
    value: typing.Optional[str] = pydantic.Field(alias="value", default=None)


class StatementData(typing_extensions.TypedDict):
    """
    No description specified
    """

    account_id: typing_extensions.Required[int]
    statement_index: typing_extensions.NotRequired[int]


class _SerializerStatementData(pydantic.BaseModel):
    """
    Serializer for StatementData handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    account_id: int = pydantic.Field(alias="accountId")
    statement_index: typing.Optional[int] = pydantic.Field(
        alias="statementIndex", default=None
    )


class StatementReportConstraints(typing_extensions.TypedDict):
    """
    No description specified
    """

    report_custom_fields: typing_extensions.NotRequired[typing.List[ReportCustomField]]
    statement_report_data: typing_extensions.Required[StatementData]


class _SerializerStatementReportConstraints(pydantic.BaseModel):
    """
    Serializer for StatementReportConstraints handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    report_custom_fields: typing.Optional[typing.List[_SerializerReportCustomField]] = (
        pydantic.Field(alias="reportCustomFields", default=None)
    )
    statement_report_data: _SerializerStatementData = pydantic.Field(
        alias="statementReportData"
    )
