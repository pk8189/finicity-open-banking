"""File Generated by Sideko (sideko.dev)"""

import io
import typing


import pydantic

ModelFiles = typing.List[
    typing.Tuple[str, typing.Union[typing.BinaryIO, io.BufferedReader]]
]


class ReportSummary(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    consumer_id: typing.Optional[str] = pydantic.Field(alias="consumerId", default=None)
    consumer_ssn: typing.Optional[str] = pydantic.Field(
        alias="consumerSsn", default=None
    )
    created_date: int = pydantic.Field(alias="createdDate")
    id: str = pydantic.Field(alias="id")
    request_id: str = pydantic.Field(alias="requestId")
    requester_name: str = pydantic.Field(alias="requesterName")
    status: str = pydantic.Field(alias="status")
    type: str = pydantic.Field(alias="type")


class ReportSummaries(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    reports: typing.List[ReportSummary] = pydantic.Field(alias="reports")
