"""File Generated by Sideko (sideko.dev)"""

import io
import typing


import pydantic

ModelFiles = typing.List[
    typing.Tuple[str, typing.Union[typing.BinaryIO, io.BufferedReader]]
]


class ObbAnalyticsReportAck(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    account_ids: typing.List[int] = pydantic.Field(alias="accountIds")
    business_id: typing.Optional[int] = pydantic.Field(alias="businessId", default=None)
    created_date: str = pydantic.Field(alias="createdDate")
    customer_id: int = pydantic.Field(alias="customerId")
    report_id: str = pydantic.Field(alias="reportId")
    report_pin: str = pydantic.Field(alias="reportPin")
    requester_name: typing.Optional[str] = pydantic.Field(
        alias="requesterName", default=None
    )
    title: str = pydantic.Field(alias="title")