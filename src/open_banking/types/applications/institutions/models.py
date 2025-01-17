"""File Generated by Sideko (sideko.dev)"""

import io
import typing


import pydantic

ModelFiles = typing.List[
    typing.Tuple[str, typing.Union[typing.BinaryIO, io.BufferedReader]]
]


class FinancialInstitution(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    created_date: typing.Optional[str] = pydantic.Field(
        alias="createdDate", default=None
    )
    institution_id: typing.Optional[int] = pydantic.Field(
        alias="institutionId", default=None
    )
    modified_date: typing.Optional[str] = pydantic.Field(
        alias="modifiedDate", default=None
    )
    status: typing.Optional[bool] = pydantic.Field(alias="status", default=None)


class InstitutionResponse(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    displaying: typing.Optional[int] = pydantic.Field(alias="displaying", default=None)
    found: typing.Optional[int] = pydantic.Field(alias="found", default=None)
    institutions: typing.Optional[typing.List[FinancialInstitution]] = pydantic.Field(
        alias="institutions", default=None
    )
    more_available: typing.Optional[bool] = pydantic.Field(
        alias="moreAvailable", default=None
    )
