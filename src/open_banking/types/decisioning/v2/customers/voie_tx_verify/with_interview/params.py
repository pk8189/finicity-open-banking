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


class TxVerifyInterview(typing_extensions.TypedDict):
    """
    No description specified
    """

    accounts: typing_extensions.NotRequired[typing.List[str]]
    asset_id: typing_extensions.Required[str]


class _SerializerTxVerifyInterview(pydantic.BaseModel):
    """
    Serializer for TxVerifyInterview handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    accounts: typing.Optional[typing.List[str]] = pydantic.Field(
        alias="accounts", default=None
    )
    asset_id: str = pydantic.Field(alias="assetId")


class VoieWithInterviewData(typing_extensions.TypedDict):
    """
    No description specified
    """

    extract_deductions: typing_extensions.NotRequired[bool]
    extract_direct_deposit: typing_extensions.NotRequired[bool]
    extract_earnings: typing_extensions.NotRequired[bool]
    tx_verify_interview: typing_extensions.Required[typing.List[TxVerifyInterview]]


class _SerializerVoieWithInterviewData(pydantic.BaseModel):
    """
    Serializer for VoieWithInterviewData handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    extract_deductions: typing.Optional[bool] = pydantic.Field(
        alias="extractDeductions", default=None
    )
    extract_direct_deposit: typing.Optional[bool] = pydantic.Field(
        alias="extractDirectDeposit", default=None
    )
    extract_earnings: typing.Optional[bool] = pydantic.Field(
        alias="extractEarnings", default=None
    )
    tx_verify_interview: typing.List[_SerializerTxVerifyInterview] = pydantic.Field(
        alias="txVerifyInterview"
    )


class VoieWithTxVerifyReportConstraints(typing_extensions.TypedDict):
    """
    No description specified
    """

    account_ids: typing_extensions.NotRequired[str]
    from_date: typing_extensions.NotRequired[int]
    income_stream_confidence_minimum: typing_extensions.NotRequired[int]
    report_custom_fields: typing_extensions.NotRequired[typing.List[ReportCustomField]]
    voie_with_interview_data: typing_extensions.Required[VoieWithInterviewData]


class _SerializerVoieWithTxVerifyReportConstraints(pydantic.BaseModel):
    """
    Serializer for VoieWithTxVerifyReportConstraints handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    account_ids: typing.Optional[str] = pydantic.Field(alias="accountIds", default=None)
    from_date: typing.Optional[int] = pydantic.Field(alias="fromDate", default=None)
    income_stream_confidence_minimum: typing.Optional[int] = pydantic.Field(
        alias="incomeStreamConfidenceMinimum", default=None
    )
    report_custom_fields: typing.Optional[typing.List[_SerializerReportCustomField]] = (
        pydantic.Field(alias="reportCustomFields", default=None)
    )
    voie_with_interview_data: _SerializerVoieWithInterviewData = pydantic.Field(
        alias="voieWithInterviewData"
    )
