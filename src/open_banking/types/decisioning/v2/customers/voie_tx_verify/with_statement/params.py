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


class VoieWithStatementData(typing_extensions.TypedDict):
    """
    No description specified
    """

    asset_ids: typing_extensions.Required[typing.List[str]]
    extract_deductions: typing_extensions.NotRequired[bool]
    extract_direct_deposit: typing_extensions.NotRequired[bool]
    extract_earnings: typing_extensions.NotRequired[bool]


class _SerializerVoieWithStatementData(pydantic.BaseModel):
    """
    Serializer for VoieWithStatementData handling case conversions
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


class VoieReportConstraints(typing_extensions.TypedDict):
    """
    The request details from the report generation that were used to generate the report
    """

    report_custom_fields: typing_extensions.NotRequired[typing.List[ReportCustomField]]
    voie_with_statement_data: typing_extensions.Required[VoieWithStatementData]


class _SerializerVoieReportConstraints(pydantic.BaseModel):
    """
    Serializer for VoieReportConstraints handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    report_custom_fields: typing.Optional[typing.List[_SerializerReportCustomField]] = (
        pydantic.Field(alias="reportCustomFields", default=None)
    )
    voie_with_statement_data: _SerializerVoieWithStatementData = pydantic.Field(
        alias="voieWithStatementData"
    )
