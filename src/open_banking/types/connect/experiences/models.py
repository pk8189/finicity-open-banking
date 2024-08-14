"""File Generated by Sideko (sideko.dev)"""

import io
import typing


import pydantic

ModelFiles = typing.List[
    typing.Tuple[str, typing.Union[typing.BinaryIO, io.BufferedReader]]
]


class Experiences(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    app_name: typing.Optional[str] = pydantic.Field(alias="appName", default=None)
    id: typing.Optional[str] = pydantic.Field(alias="id", default=None)
    product_code: typing.Optional[typing.List[str]] = pydantic.Field(
        alias="productCode", default=None
    )
