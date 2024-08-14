"""File Generated by Sideko (sideko.dev)"""

from open_banking.core import (
    SyncBaseClient,
    AsyncBaseClient,
    RequestOptions,
    default_request_options,
)
import typing
from open_banking.types.aggregation.v1.customers.institutions.accounts.simple import (
    models,
)


class SimpleClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        # register sync resources (keep comment for code generation)

    # register sync api methods (keep comment for code generation)
    def list(
        self,
        *,
        customer_id: str,
        institution_id: int,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.CustomerAccountsSimple:
        """
        This API is a lighter version of Get Customer Accounts by Institution ID, returning only basic information of active accounts owned by the given customer at the given institution.

        _Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)
        """
        # start -- build request data (keep comment for code generation)
        # end -- build request data (keep comment for code generation)

        # start -- send sync request (keep comment for code generation)
        return self._base_client.request(
            method="GET",
            path=f"/aggregation/v1/customers/{customer_id}/institutions/{institution_id}/accounts/simple",
            auth_names=["FinicityAppKey", "FinicityAppToken"],
            cast_to=models.CustomerAccountsSimple,
            request_options=request_options or default_request_options(),
        )
        # end -- send sync request (keep comment for code generation)


class AsyncSimpleClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        # register async resources (keep comment for code generation)

    # register async api methods (keep comment for code generation)
    async def list(
        self,
        *,
        customer_id: str,
        institution_id: int,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.CustomerAccountsSimple:
        """
        This API is a lighter version of Get Customer Accounts by Institution ID, returning only basic information of active accounts owned by the given customer at the given institution.

        _Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)
        """
        # start -- build request data (keep comment for code generation)
        # end -- build request data (keep comment for code generation)

        # start -- send async request (keep comment for code generation)
        return await self._base_client.request(
            method="GET",
            path=f"/aggregation/v1/customers/{customer_id}/institutions/{institution_id}/accounts/simple",
            auth_names=["FinicityAppKey", "FinicityAppToken"],
            cast_to=models.CustomerAccountsSimple,
            request_options=request_options or default_request_options(),
        )
        # end -- send async request (keep comment for code generation)
