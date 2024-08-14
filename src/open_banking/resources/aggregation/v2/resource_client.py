"""File Generated by Sideko (sideko.dev)"""

from open_banking.core import SyncBaseClient, AsyncBaseClient
from open_banking.resources.aggregation.v2.customers import (
    CustomersClient,
    AsyncCustomersClient,
)
from open_banking.resources.aggregation.v2.partners import (
    PartnersClient,
    AsyncPartnersClient,
)


class V2Client:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        # register sync resources (keep comment for code generation)
        self.customers = CustomersClient(base_client=self._base_client)
        self.partners = PartnersClient(base_client=self._base_client)

    # register sync api methods (keep comment for code generation)


class AsyncV2Client:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        # register async resources (keep comment for code generation)
        self.customers = AsyncCustomersClient(base_client=self._base_client)
        self.partners = AsyncPartnersClient(base_client=self._base_client)

    # register async api methods (keep comment for code generation)