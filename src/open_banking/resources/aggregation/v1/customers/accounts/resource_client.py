"""File Generated by Sideko (sideko.dev)"""

from open_banking.core import (
    encode_param,
    default_request_options,
    SyncBaseClient,
    AsyncBaseClient,
    RequestOptions,
    QueryParams,
)
from open_banking.resources.aggregation.v1.customers.accounts.txpush import (
    TxpushClient,
    AsyncTxpushClient,
)
from open_banking.resources.aggregation.v1.customers.accounts.simple import (
    AsyncSimpleClient,
    SimpleClient,
)
from open_banking.resources.aggregation.v1.customers.accounts.available_balance import (
    AsyncAvailableBalanceClient,
    AvailableBalanceClient,
)
from open_banking.resources.aggregation.v1.customers.accounts.details import (
    AsyncDetailsClient,
    DetailsClient,
)
from open_banking.resources.aggregation.v1.customers.accounts.owner import (
    AsyncOwnerClient,
    OwnerClient,
)
from open_banking.resources.aggregation.v1.customers.accounts.statement import (
    AsyncStatementClient,
    StatementClient,
)
from open_banking.resources.aggregation.v1.customers.accounts.transactions import (
    AsyncTransactionsClient,
    TransactionsClient,
)
import typing
from open_banking.types.aggregation.v1.customers.accounts import models


class AccountsClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        # register sync resources (keep comment for code generation)
        self.txpush = TxpushClient(base_client=self._base_client)
        self.simple = SimpleClient(base_client=self._base_client)
        self.available_balance = AvailableBalanceClient(base_client=self._base_client)
        self.details = DetailsClient(base_client=self._base_client)
        self.owner = OwnerClient(base_client=self._base_client)
        self.statement = StatementClient(base_client=self._base_client)
        self.transactions = TransactionsClient(base_client=self._base_client)

    # register sync api methods (keep comment for code generation)
    def create(
        self,
        *,
        customer_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.CustomerAccounts:
        """
        Refresh account and transaction data for all accounts associated with the  given `customerId` with a connection to the institution.

        Client apps are not permitted to automate calls to the Refresh services. Active accounts are automatically refreshed by Finicity once per day. Because many financial institutions only post transactions once per day, calling Refresh services repeatedly is usually a waste of resources and is not recommended.

        Apps may call Refresh services for a specific customer when there is a specific business case for the need of data that is up to date as of the moment. Please discuss with your account manager and systems engineer for further clarification.

        The recommended timeout setting for this request is 120 seconds in order to receive a response. However, you can terminate the connection after making the call the operation will still complete. You will have to pull the account records to check for an updated aggregation attempt date to know when the refresh is complete.

        Note: This service is not available for all Data Access Tiers.

        _Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)
        """
        # start -- build request data (keep comment for code generation)
        # end -- build request data (keep comment for code generation)

        # start -- send sync request (keep comment for code generation)
        return self._base_client.request(
            method="POST",
            path=f"/aggregation/v1/customers/{customer_id}/accounts",
            auth_names=["FinicityAppKey", "FinicityAppToken"],
            cast_to=models.CustomerAccounts,
            request_options=request_options or default_request_options(),
        )
        # end -- send sync request (keep comment for code generation)

    def list(
        self,
        *,
        customer_id: str,
        account_type: typing.Optional[str] = None,
        status: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.CustomerAccounts:
        """
        Get all accounts owned by the given customer.

        _Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)
        """
        # start -- build request data (keep comment for code generation)
        _query: QueryParams = {}
        if account_type is not None:
            _query["account_type"] = encode_param(account_type, False)
        if status is not None:
            _query["status"] = encode_param(status, False)
        # end -- build request data (keep comment for code generation)

        # start -- send sync request (keep comment for code generation)
        return self._base_client.request(
            method="GET",
            path=f"/aggregation/v1/customers/{customer_id}/accounts",
            auth_names=["FinicityAppKey", "FinicityAppToken"],
            query_params=_query,
            cast_to=models.CustomerAccounts,
            request_options=request_options or default_request_options(),
        )
        # end -- send sync request (keep comment for code generation)

    def delete(
        self,
        *,
        customer_id: str,
        account_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        This will delete access to a specific account only. If there are multiple permissioned accounts, then partners and their customers will have the flexibility to continue to access data from other connected accounts using the consented (Oauth) token for the customer.
        The customer data on that specific account will no longer be accessible. Any customer data already collected will be retained in accordance with our enterprise retention policy consistent with legal and business purposes. ​
        _Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)
        """
        # start -- build request data (keep comment for code generation)
        # end -- build request data (keep comment for code generation)

        # start -- send sync request (keep comment for code generation)
        return self._base_client.request(
            method="DELETE",
            path=f"/aggregation/v1/customers/{customer_id}/accounts/{account_id}",
            auth_names=["FinicityAppKey", "FinicityAppToken"],
            cast_to=type(None),
            request_options=request_options or default_request_options(),
        )
        # end -- send sync request (keep comment for code generation)


class AsyncAccountsClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        # register async resources (keep comment for code generation)
        self.txpush = AsyncTxpushClient(base_client=self._base_client)
        self.simple = AsyncSimpleClient(base_client=self._base_client)
        self.available_balance = AsyncAvailableBalanceClient(
            base_client=self._base_client
        )
        self.details = AsyncDetailsClient(base_client=self._base_client)
        self.owner = AsyncOwnerClient(base_client=self._base_client)
        self.statement = AsyncStatementClient(base_client=self._base_client)
        self.transactions = AsyncTransactionsClient(base_client=self._base_client)

    # register async api methods (keep comment for code generation)
    async def create(
        self,
        *,
        customer_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.CustomerAccounts:
        """
        Refresh account and transaction data for all accounts associated with the  given `customerId` with a connection to the institution.

        Client apps are not permitted to automate calls to the Refresh services. Active accounts are automatically refreshed by Finicity once per day. Because many financial institutions only post transactions once per day, calling Refresh services repeatedly is usually a waste of resources and is not recommended.

        Apps may call Refresh services for a specific customer when there is a specific business case for the need of data that is up to date as of the moment. Please discuss with your account manager and systems engineer for further clarification.

        The recommended timeout setting for this request is 120 seconds in order to receive a response. However, you can terminate the connection after making the call the operation will still complete. You will have to pull the account records to check for an updated aggregation attempt date to know when the refresh is complete.

        Note: This service is not available for all Data Access Tiers.

        _Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)
        """
        # start -- build request data (keep comment for code generation)
        # end -- build request data (keep comment for code generation)

        # start -- send async request (keep comment for code generation)
        return await self._base_client.request(
            method="POST",
            path=f"/aggregation/v1/customers/{customer_id}/accounts",
            auth_names=["FinicityAppKey", "FinicityAppToken"],
            cast_to=models.CustomerAccounts,
            request_options=request_options or default_request_options(),
        )
        # end -- send async request (keep comment for code generation)

    async def list(
        self,
        *,
        customer_id: str,
        account_type: typing.Optional[str] = None,
        status: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.CustomerAccounts:
        """
        Get all accounts owned by the given customer.

        _Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)
        """
        # start -- build request data (keep comment for code generation)
        _query: QueryParams = {}
        if account_type is not None:
            _query["account_type"] = encode_param(account_type, False)
        if status is not None:
            _query["status"] = encode_param(status, False)
        # end -- build request data (keep comment for code generation)

        # start -- send async request (keep comment for code generation)
        return await self._base_client.request(
            method="GET",
            path=f"/aggregation/v1/customers/{customer_id}/accounts",
            auth_names=["FinicityAppKey", "FinicityAppToken"],
            query_params=_query,
            cast_to=models.CustomerAccounts,
            request_options=request_options or default_request_options(),
        )
        # end -- send async request (keep comment for code generation)

    async def delete(
        self,
        *,
        customer_id: str,
        account_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        This will delete access to a specific account only. If there are multiple permissioned accounts, then partners and their customers will have the flexibility to continue to access data from other connected accounts using the consented (Oauth) token for the customer.
        The customer data on that specific account will no longer be accessible. Any customer data already collected will be retained in accordance with our enterprise retention policy consistent with legal and business purposes. ​
        _Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)
        """
        # start -- build request data (keep comment for code generation)
        # end -- build request data (keep comment for code generation)

        # start -- send async request (keep comment for code generation)
        return await self._base_client.request(
            method="DELETE",
            path=f"/aggregation/v1/customers/{customer_id}/accounts/{account_id}",
            auth_names=["FinicityAppKey", "FinicityAppToken"],
            cast_to=type(None),
            request_options=request_options or default_request_options(),
        )
        # end -- send async request (keep comment for code generation)