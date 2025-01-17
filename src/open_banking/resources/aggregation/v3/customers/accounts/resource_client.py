"""File Generated by Sideko (sideko.dev)"""

from open_banking.core import SyncBaseClient, AsyncBaseClient
from open_banking.resources.aggregation.v3.customers.accounts.details import (
    DetailsClient,
    AsyncDetailsClient,
)
from open_banking.resources.aggregation.v3.customers.accounts.owner import (
    AsyncOwnerClient,
    OwnerClient,
)
from open_banking.resources.aggregation.v3.customers.accounts.statement import (
    StatementClient,
    AsyncStatementClient,
)


class AccountsClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        # register sync resources (keep comment for code generation)
        self.details = DetailsClient(base_client=self._base_client)
        self.owner = OwnerClient(base_client=self._base_client)
        self.statement = StatementClient(base_client=self._base_client)

    # register sync api methods (keep comment for code generation)


class AsyncAccountsClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        # register async resources (keep comment for code generation)
        self.details = AsyncDetailsClient(base_client=self._base_client)
        self.owner = AsyncOwnerClient(base_client=self._base_client)
        self.statement = AsyncStatementClient(base_client=self._base_client)

    # register async api methods (keep comment for code generation)
