"""File Generated by Sideko (sideko.dev)"""

import io
import typing


import pydantic

ModelFiles = typing.List[
    typing.Tuple[str, typing.Union[typing.BinaryIO, io.BufferedReader]]
]


class CustomerAuthorizationDetails(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    authorization_end_date: str = pydantic.Field(alias="authorizationEndDate")
    authorization_start_date: str = pydantic.Field(alias="authorizationStartDate")
    institution_login_id: int = pydantic.Field(alias="institutionLoginId")
