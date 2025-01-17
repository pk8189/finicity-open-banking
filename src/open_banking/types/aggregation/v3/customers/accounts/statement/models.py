"""File Generated by Sideko (sideko.dev)"""

import io
import typing


import pydantic

ModelFiles = typing.List[
    typing.Tuple[str, typing.Union[typing.BinaryIO, io.BufferedReader]]
]


class CustomerAccountMultipleStatement(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    as_of_date: int = pydantic.Field(alias="asOfDate")
    code_field: typing.Optional[str] = pydantic.Field(alias="code", default=None)
    description: typing.Optional[str] = pydantic.Field(
        alias="description", default=None
    )
    document_date: typing.Optional[str] = pydantic.Field(
        alias="documentDate", default=None
    )
    id: typing.Optional[str] = pydantic.Field(alias="id", default=None)
    index: str = pydantic.Field(alias="index")
    message: typing.Optional[str] = pydantic.Field(alias="message", default=None)


class CustomerAccountMultipleStatements(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    statements: typing.List[CustomerAccountMultipleStatement] = pydantic.Field(
        alias="statements"
    )
