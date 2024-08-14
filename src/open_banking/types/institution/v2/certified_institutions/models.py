"""File Generated by Sideko (sideko.dev)"""

import io
import typing


import pydantic

ModelFiles = typing.List[
    typing.Tuple[str, typing.Union[typing.BinaryIO, io.BufferedReader]]
]


class ChildInstitution(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    institution_id: int = pydantic.Field(alias="institutionId")
    name: str = pydantic.Field(alias="name")
    parent_rssd: int = pydantic.Field(alias="parentRSSD")
    rssd: int = pydantic.Field(alias="rssd")


class CertifiedInstitution(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    account_owner: bool = pydantic.Field(alias="accountOwner")
    ach: bool = pydantic.Field(alias="ach")
    aha: bool = pydantic.Field(alias="aha")
    avail_balance: bool = pydantic.Field(alias="availBalance")
    child_institutions: typing.Optional[typing.List[ChildInstitution]] = pydantic.Field(
        alias="childInstitutions", default=None
    )
    id: int = pydantic.Field(alias="id")
    loan_payment_details: bool = pydantic.Field(alias="loanPaymentDetails")
    name: str = pydantic.Field(alias="name")
    rssd: typing.Optional[int] = pydantic.Field(alias="rssd", default=None)
    state_agg: bool = pydantic.Field(alias="stateAgg")
    student_loan_data: bool = pydantic.Field(alias="studentLoanData")
    trans_agg: bool = pydantic.Field(alias="transAgg")
    voa: bool = pydantic.Field(alias="voa")
    voi: bool = pydantic.Field(alias="voi")


class CertifiedInstitutions(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    displaying: int = pydantic.Field(alias="displaying")
    found: int = pydantic.Field(alias="found")
    institutions: typing.List[CertifiedInstitution] = pydantic.Field(
        alias="institutions"
    )
    more_available: bool = pydantic.Field(alias="moreAvailable")
    requested_date: int = pydantic.Field(alias="requestedDate")