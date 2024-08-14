"""File Generated by Sideko (sideko.dev)"""

from __future__ import annotations
import io
import typing
import pydantic
import typing_extensions

HttpxFile = typing.Tuple[str, typing.Union[typing.BinaryIO, io.BufferedReader]]


class ConsumerInfo(typing_extensions.TypedDict):
    """
    The SSN and date of birth of a consumer
    """

    dob: typing_extensions.NotRequired[int]
    ssn: typing_extensions.Required[str]


class _SerializerConsumerInfo(pydantic.BaseModel):
    """
    Serializer for ConsumerInfo handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    dob: typing.Optional[int] = pydantic.Field(alias="dob", default=None)
    ssn: str = pydantic.Field(alias="ssn")


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


class ConnectParameters(typing_extensions.TypedDict):
    """
    No description specified
    """

    consumer_id: typing_extensions.NotRequired[str]
    customer_id: typing_extensions.Required[str]
    experience: typing_extensions.NotRequired[str]
    from_date: typing_extensions.NotRequired[int]
    institution_settings: typing_extensions.NotRequired[typing.Dict[str, typing.Any]]
    is_web_view: typing_extensions.NotRequired[bool]
    language: typing_extensions.NotRequired[str]
    optional_consumer_info: typing_extensions.NotRequired[ConsumerInfo]
    partner_id: typing_extensions.Required[str]
    redirect_uri: typing_extensions.NotRequired[str]
    report_custom_fields: typing_extensions.NotRequired[typing.List[ReportCustomField]]
    single_use_url: typing_extensions.NotRequired[bool]
    webhook: typing_extensions.NotRequired[str]
    webhook_content_type: typing_extensions.NotRequired[str]
    webhook_data: typing_extensions.NotRequired[typing.Dict[str, typing.Any]]
    webhook_headers: typing_extensions.NotRequired[typing.Dict[str, typing.Any]]


class _SerializerConnectParameters(pydantic.BaseModel):
    """
    Serializer for ConnectParameters handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    consumer_id: typing.Optional[str] = pydantic.Field(alias="consumerId", default=None)
    customer_id: str = pydantic.Field(alias="customerId")
    experience: typing.Optional[str] = pydantic.Field(alias="experience", default=None)
    from_date: typing.Optional[int] = pydantic.Field(alias="fromDate", default=None)
    institution_settings: typing.Optional[typing.Dict[str, typing.Any]] = (
        pydantic.Field(alias="institutionSettings", default=None)
    )
    is_web_view: typing.Optional[bool] = pydantic.Field(alias="isWebView", default=None)
    language: typing.Optional[str] = pydantic.Field(alias="language", default=None)
    optional_consumer_info: typing.Optional[_SerializerConsumerInfo] = pydantic.Field(
        alias="optionalConsumerInfo", default=None
    )
    partner_id: str = pydantic.Field(alias="partnerId")
    redirect_uri: typing.Optional[str] = pydantic.Field(
        alias="redirectUri", default=None
    )
    report_custom_fields: typing.Optional[typing.List[_SerializerReportCustomField]] = (
        pydantic.Field(alias="reportCustomFields", default=None)
    )
    single_use_url: typing.Optional[bool] = pydantic.Field(
        alias="singleUseUrl", default=None
    )
    webhook: typing.Optional[str] = pydantic.Field(alias="webhook", default=None)
    webhook_content_type: typing.Optional[str] = pydantic.Field(
        alias="webhookContentType", default=None
    )
    webhook_data: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(
        alias="webhookData", default=None
    )
    webhook_headers: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(
        alias="webhookHeaders", default=None
    )