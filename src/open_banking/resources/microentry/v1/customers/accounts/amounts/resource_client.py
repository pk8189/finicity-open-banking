"""File Generated by Sideko (sideko.dev)"""

from open_banking.core import (
    default_request_options,
    SyncBaseClient,
    AsyncBaseClient,
    RequestOptions,
    to_encodable,
)
from open_banking.types.microentry.v1.customers.accounts.amounts import models, params
import typing


class AmountsClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        # register sync resources (keep comment for code generation)

    # register sync api methods (keep comment for code generation)
    def create(
        self,
        *,
        data: params.MicroDepositVerification,
        customer_id: str,
        account_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.VerifiedMicroDeposit:
        """
        Verify the micro entries as received by customer in customer's account.
        Customer needs to verify the micro amounts received in customer's account. `customerId` and `accountId` are the identifiers of the customer and account  receiving the micro entries.

          _Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)
        """
        # start -- build request data (keep comment for code generation)
        _json = to_encodable(
            item=data, dump_with=params._SerializerMicroDepositVerification
        )
        # end -- build request data (keep comment for code generation)

        # start -- send sync request (keep comment for code generation)
        return self._base_client.request(
            method="POST",
            path=f"/microentry/v1/customers/{customer_id}/accounts/{account_id}/amounts",
            auth_names=["FinicityAppKey", "FinicityAppToken"],
            json=_json,
            cast_to=models.VerifiedMicroDeposit,
            request_options=request_options or default_request_options(),
        )
        # end -- send sync request (keep comment for code generation)


class AsyncAmountsClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        # register async resources (keep comment for code generation)

    # register async api methods (keep comment for code generation)
    async def create(
        self,
        *,
        data: params.MicroDepositVerification,
        customer_id: str,
        account_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.VerifiedMicroDeposit:
        """
        Verify the micro entries as received by customer in customer's account.
        Customer needs to verify the micro amounts received in customer's account. `customerId` and `accountId` are the identifiers of the customer and account  receiving the micro entries.

          _Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)
        """
        # start -- build request data (keep comment for code generation)
        _json = to_encodable(
            item=data, dump_with=params._SerializerMicroDepositVerification
        )
        # end -- build request data (keep comment for code generation)

        # start -- send async request (keep comment for code generation)
        return await self._base_client.request(
            method="POST",
            path=f"/microentry/v1/customers/{customer_id}/accounts/{account_id}/amounts",
            auth_names=["FinicityAppKey", "FinicityAppToken"],
            json=_json,
            cast_to=models.VerifiedMicroDeposit,
            request_options=request_options or default_request_options(),
        )
        # end -- send async request (keep comment for code generation)