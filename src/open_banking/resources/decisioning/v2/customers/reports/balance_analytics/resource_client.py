"""File Generated by Sideko (sideko.dev)"""

from open_banking.core import AsyncBaseClient, SyncBaseClient
from open_banking.resources.decisioning.v2.customers.reports.balance_analytics.user_types import (
    UserTypesClient,
    AsyncUserTypesClient,
)


class BalanceAnalyticsClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        # register sync resources (keep comment for code generation)
        self.user_types = UserTypesClient(base_client=self._base_client)

    # register sync api methods (keep comment for code generation)


class AsyncBalanceAnalyticsClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        # register async resources (keep comment for code generation)
        self.user_types = AsyncUserTypesClient(base_client=self._base_client)

    # register async api methods (keep comment for code generation)
