"""File Generated by Sideko (sideko.dev)"""

import io
import typing


import pydantic

ModelFiles = typing.List[
    typing.Tuple[str, typing.Union[typing.BinaryIO, io.BufferedReader]]
]


class PortfolioReport(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    created_date: int = pydantic.Field(alias="createdDate")
    id: str = pydantic.Field(alias="id")
    portfolio_id: str = pydantic.Field(alias="portfolioId")
    status: str = pydantic.Field(alias="status")
    type: str = pydantic.Field(alias="type")


class PortfolioSummary(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    portfolio_id: str = pydantic.Field(alias="portfolioId")
    reports: typing.List[PortfolioReport] = pydantic.Field(alias="reports")
