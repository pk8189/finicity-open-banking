"""File Generated by Sideko (sideko.dev)"""

from open_banking.core import (
    default_request_options,
    SyncBaseClient,
    AsyncBaseClient,
    RequestOptions,
)
import typing
from open_banking.types.aggregation.v2.customers.institution_logins.migration import (
    models,
)


class MigrationClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        # register sync resources (keep comment for code generation)

    # register sync api methods (keep comment for code generation)
    def put(
        self,
        *,
        customer_id: str,
        institution_login_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.CustomerAccounts:
        """
        The `institutionLoginId` parameter uses Finicity's internal FI mapping to move accounts from the current FI legacy connection to the new OAuth FI connection.

        This API returns a list of accounts for the given institution login ID.

        _Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)
        """
        # start -- build request data (keep comment for code generation)
        # end -- build request data (keep comment for code generation)

        # start -- send sync request (keep comment for code generation)
        return self._base_client.request(
            method="PUT",
            path=f"/aggregation/v2/customers/{customer_id}/institutionLogins/{institution_login_id}/migration",
            auth_names=["FinicityAppKey", "FinicityAppToken"],
            cast_to=models.CustomerAccounts,
            request_options=request_options or default_request_options(),
        )
        # end -- send sync request (keep comment for code generation)


class AsyncMigrationClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        # register async resources (keep comment for code generation)

    # register async api methods (keep comment for code generation)
    async def put(
        self,
        *,
        customer_id: str,
        institution_login_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.CustomerAccounts:
        """
        The `institutionLoginId` parameter uses Finicity's internal FI mapping to move accounts from the current FI legacy connection to the new OAuth FI connection.

        This API returns a list of accounts for the given institution login ID.

        _Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)
        """
        # start -- build request data (keep comment for code generation)
        # end -- build request data (keep comment for code generation)

        # start -- send async request (keep comment for code generation)
        return await self._base_client.request(
            method="PUT",
            path=f"/aggregation/v2/customers/{customer_id}/institutionLogins/{institution_login_id}/migration",
            auth_names=["FinicityAppKey", "FinicityAppToken"],
            cast_to=models.CustomerAccounts,
            request_options=request_options or default_request_options(),
        )
        # end -- send async request (keep comment for code generation)
