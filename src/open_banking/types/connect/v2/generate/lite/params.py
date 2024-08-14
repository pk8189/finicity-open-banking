"""File Generated by Sideko (sideko.dev)"""

from __future__ import annotations
import io
import typing
import pydantic
import typing_extensions

HttpxFile = typing.Tuple[str, typing.Union[typing.BinaryIO, io.BufferedReader]]


class LiteConnectParameters(typing_extensions.TypedDict):
    """
    No description specified
    """

    customer_id: typing_extensions.Required[str]
    experience: typing_extensions.NotRequired[str]
    institution_id: typing_extensions.Required[int]
    is_web_view: typing_extensions.NotRequired[bool]
    language: typing_extensions.NotRequired[str]
    partner_id: typing_extensions.Required[str]
    redirect_uri: typing_extensions.NotRequired[str]
    single_use_url: typing_extensions.NotRequired[bool]
    webhook: typing_extensions.NotRequired[str]
    webhook_content_type: typing_extensions.NotRequired[str]
    webhook_data: typing_extensions.NotRequired[typing.Dict[str, typing.Any]]
    webhook_headers: typing_extensions.NotRequired[typing.Dict[str, typing.Any]]


class _SerializerLiteConnectParameters(pydantic.BaseModel):
    """
    Serializer for LiteConnectParameters handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    customer_id: str = pydantic.Field(alias="customerId")
    experience: typing.Optional[str] = pydantic.Field(alias="experience", default=None)
    institution_id: int = pydantic.Field(alias="institutionId")
    is_web_view: typing.Optional[bool] = pydantic.Field(alias="isWebView", default=None)
    language: typing.Optional[str] = pydantic.Field(alias="language", default=None)
    partner_id: str = pydantic.Field(alias="partnerId")
    redirect_uri: typing.Optional[str] = pydantic.Field(
        alias="redirectUri", default=None
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
