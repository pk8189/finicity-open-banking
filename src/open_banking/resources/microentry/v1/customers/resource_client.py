"""File Generated by Sideko (sideko.dev)"""

from open_banking.core import (
    RequestOptions,
    SyncBaseClient,
    AsyncBaseClient,
    to_encodable,
    default_request_options,
)
from open_banking.resources.microentry.v1.customers.accounts import (
    AsyncAccountsClient,
    AccountsClient,
)
from open_banking.types.microentry.v1.customers import models, params
import typing


class CustomersClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        # register sync resources (keep comment for code generation)
        self.accounts = AccountsClient(base_client=self._base_client)

    # register sync api methods (keep comment for code generation)
    def create(
        self,
        *,
        data: params.MicroDepositInitiation,
        customer_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.InitiatedMicroDeposit:
        """
        Initiate the micro entries to customer's account.

        Two random micro amounts less than a dollar each will be deposited to provided customer's account.

          _Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)
        """
        # start -- build request data (keep comment for code generation)
        _json = to_encodable(
            item=data, dump_with=params._SerializerMicroDepositInitiation
        )
        # end -- build request data (keep comment for code generation)

        # start -- send sync request (keep comment for code generation)
        return self._base_client.request(
            method="POST",
            path=f"/microentry/v1/customers/{customer_id}",
            auth_names=["FinicityAppKey", "FinicityAppToken"],
            json=_json,
            cast_to=models.InitiatedMicroDeposit,
            request_options=request_options or default_request_options(),
        )
        # end -- send sync request (keep comment for code generation)


class AsyncCustomersClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        # register async resources (keep comment for code generation)
        self.accounts = AsyncAccountsClient(base_client=self._base_client)

    # register async api methods (keep comment for code generation)
    async def create(
        self,
        *,
        data: params.MicroDepositInitiation,
        customer_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.InitiatedMicroDeposit:
        """
        Initiate the micro entries to customer's account.

        Two random micro amounts less than a dollar each will be deposited to provided customer's account.

          _Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)
        """
        # start -- build request data (keep comment for code generation)
        _json = to_encodable(
            item=data, dump_with=params._SerializerMicroDepositInitiation
        )
        # end -- build request data (keep comment for code generation)

        # start -- send async request (keep comment for code generation)
        return await self._base_client.request(
            method="POST",
            path=f"/microentry/v1/customers/{customer_id}",
            auth_names=["FinicityAppKey", "FinicityAppToken"],
            json=_json,
            cast_to=models.InitiatedMicroDeposit,
            request_options=request_options or default_request_options(),
        )
        # end -- send async request (keep comment for code generation)
