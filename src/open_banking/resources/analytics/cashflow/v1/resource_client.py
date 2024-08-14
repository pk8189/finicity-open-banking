"""File Generated by Sideko (sideko.dev)"""

from open_banking.core import AsyncBaseClient, SyncBaseClient
from open_banking.resources.analytics.cashflow.v1.customer import (
    CustomerClient,
    AsyncCustomerClient,
)


class V1Client:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        # register sync resources (keep comment for code generation)
        self.customer = CustomerClient(base_client=self._base_client)

    # register sync api methods (keep comment for code generation)


class AsyncV1Client:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        # register async resources (keep comment for code generation)
        self.customer = AsyncCustomerClient(base_client=self._base_client)

    # register async api methods (keep comment for code generation)
