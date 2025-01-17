"""File Generated by Sideko (sideko.dev)"""

import io
import typing


import pydantic

ModelFiles = typing.List[
    typing.Tuple[str, typing.Union[typing.BinaryIO, io.BufferedReader]]
]


class Descriptor(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    type: str = pydantic.Field(alias="type")
    value: str = pydantic.Field(alias="value")


class PaymentInstruction(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    account_number: str = pydantic.Field(alias="accountNumber")
    descriptors: typing.Optional[typing.List[Descriptor]] = pydantic.Field(
        alias="descriptors", default=None
    )
    transfer_in_enabled: typing.Optional[bool] = pydantic.Field(
        alias="transferInEnabled", default=None
    )
    transfer_out_enabled: typing.Optional[bool] = pydantic.Field(
        alias="transferOutEnabled", default=None
    )
    type: str = pydantic.Field(alias="type")


class PaymentInstructions(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    payment_instruction: typing.Optional[typing.List[PaymentInstruction]] = (
        pydantic.Field(alias="paymentInstruction", default=None)
    )
