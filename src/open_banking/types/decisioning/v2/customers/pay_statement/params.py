"""File Generated by Sideko (sideko.dev)"""

from __future__ import annotations
import io
import typing
import pydantic
import typing_extensions

HttpxFile = typing.Tuple[str, typing.Union[typing.BinaryIO, io.BufferedReader]]


class PayStatementData(typing_extensions.TypedDict):
    """
    Data to be included within the pay statement report
    """

    asset_ids: typing_extensions.Required[typing.List[str]]
    extract_deductions: typing_extensions.NotRequired[bool]
    extract_direct_deposit: typing_extensions.NotRequired[bool]
    extract_earnings: typing_extensions.NotRequired[bool]


class _SerializerPayStatementData(pydantic.BaseModel):
    """
    Serializer for PayStatementData handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    asset_ids: typing.List[str] = pydantic.Field(alias="assetIds")
    extract_deductions: typing.Optional[bool] = pydantic.Field(
        alias="extractDeductions", default=None
    )
    extract_direct_deposit: typing.Optional[bool] = pydantic.Field(
        alias="extractDirectDeposit", default=None
    )
    extract_earnings: typing.Optional[bool] = pydantic.Field(
        alias="extractEarnings", default=None
    )


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


class PayStatementReportConstraints(typing_extensions.TypedDict):
    """
    No description specified
    """

    paystatement_report: typing_extensions.Required[PayStatementData]
    report_custom_fields: typing_extensions.NotRequired[typing.List[ReportCustomField]]


class _SerializerPayStatementReportConstraints(pydantic.BaseModel):
    """
    Serializer for PayStatementReportConstraints handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    paystatement_report: _SerializerPayStatementData = pydantic.Field(
        alias="paystatementReport"
    )
    report_custom_fields: typing.Optional[typing.List[_SerializerReportCustomField]] = (
        pydantic.Field(alias="reportCustomFields", default=None)
    )
