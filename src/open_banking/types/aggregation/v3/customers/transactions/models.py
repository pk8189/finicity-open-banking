"""File Generated by Sideko (sideko.dev)"""

import io
import typing


import pydantic

ModelFiles = typing.List[
    typing.Tuple[str, typing.Union[typing.BinaryIO, io.BufferedReader]]
]


class Categorization(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    best_representation: typing.Optional[str] = pydantic.Field(
        alias="bestRepresentation", default=None
    )
    category: str = pydantic.Field(alias="category")
    city: typing.Optional[str] = pydantic.Field(alias="city", default=None)
    country: str = pydantic.Field(alias="country")
    normalized_payee_name: str = pydantic.Field(alias="normalizedPayeeName")
    postal_code: typing.Optional[str] = pydantic.Field(alias="postalCode", default=None)
    state: typing.Optional[str] = pydantic.Field(alias="state", default=None)


class Transaction(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    account_id: int = pydantic.Field(alias="accountId")
    amount: float = pydantic.Field(alias="amount")
    categorization: typing.Optional[Categorization] = pydantic.Field(
        alias="categorization", default=None
    )
    check_num: typing.Optional[str] = pydantic.Field(alias="checkNum", default=None)
    commission_amount: typing.Optional[int] = pydantic.Field(
        alias="commissionAmount", default=None
    )
    created_date: int = pydantic.Field(alias="createdDate")
    currency_symbol: typing.Optional[str] = pydantic.Field(
        alias="currencySymbol", default=None
    )
    customer_id: int = pydantic.Field(alias="customerId")
    description: str = pydantic.Field(alias="description")
    effective_date: typing.Optional[int] = pydantic.Field(
        alias="effectiveDate", default=None
    )
    escrow_amount: typing.Optional[float] = pydantic.Field(
        alias="escrowAmount", default=None
    )
    fee_amount: typing.Optional[float] = pydantic.Field(alias="feeAmount", default=None)
    first_effective_date: typing.Optional[int] = pydantic.Field(
        alias="firstEffectiveDate", default=None
    )
    id: int = pydantic.Field(alias="id")
    income_type: typing.Optional[str] = pydantic.Field(alias="incomeType", default=None)
    interest_amount: typing.Optional[float] = pydantic.Field(
        alias="interestAmount", default=None
    )
    investment_transaction_type: typing.Optional[str] = pydantic.Field(
        alias="investmentTransactionType", default=None
    )
    memo: typing.Optional[str] = pydantic.Field(alias="memo", default=None)
    option_expire_date: typing.Optional[int] = pydantic.Field(
        alias="optionExpireDate", default=None
    )
    option_strike_price: typing.Optional[float] = pydantic.Field(
        alias="optionStrikePrice", default=None
    )
    posted_date: typing.Optional[int] = pydantic.Field(alias="postedDate", default=None)
    principal_amount: typing.Optional[float] = pydantic.Field(
        alias="principalAmount", default=None
    )
    running_balance_amount: typing.Optional[float] = pydantic.Field(
        alias="runningBalanceAmount", default=None
    )
    security_id: typing.Optional[str] = pydantic.Field(alias="securityId", default=None)
    security_id_type: typing.Optional[str] = pydantic.Field(
        alias="securityIdType", default=None
    )
    shares_per_contract: typing.Optional[float] = pydantic.Field(
        alias="sharesPerContract", default=None
    )
    split_denominator: typing.Optional[float] = pydantic.Field(
        alias="splitDenominator", default=None
    )
    split_numerator: typing.Optional[float] = pydantic.Field(
        alias="splitNumerator", default=None
    )
    status: str = pydantic.Field(alias="status")
    sub_account_fund: typing.Optional[str] = pydantic.Field(
        alias="subAccountFund", default=None
    )
    subaccount_security_type: typing.Optional[str] = pydantic.Field(
        alias="subaccountSecurityType", default=None
    )
    suspense_amount: typing.Optional[float] = pydantic.Field(
        alias="suspenseAmount", default=None
    )
    taxes_amount: typing.Optional[int] = pydantic.Field(
        alias="taxesAmount", default=None
    )
    ticker: typing.Optional[str] = pydantic.Field(alias="ticker", default=None)
    transaction_date: typing.Optional[int] = pydantic.Field(
        alias="transactionDate", default=None
    )
    type: typing.Optional[str] = pydantic.Field(alias="type", default=None)
    unit_price: typing.Optional[float] = pydantic.Field(alias="unitPrice", default=None)
    unit_quantity: typing.Optional[int] = pydantic.Field(
        alias="unitQuantity", default=None
    )


class Transactions(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    displaying: int = pydantic.Field(alias="displaying")
    found: int = pydantic.Field(alias="found")
    from_date: int = pydantic.Field(alias="fromDate")
    more_available: bool = pydantic.Field(alias="moreAvailable")
    sort: str = pydantic.Field(alias="sort")
    to_date: int = pydantic.Field(alias="toDate")
    transactions: typing.List[Transaction] = pydantic.Field(alias="transactions")
