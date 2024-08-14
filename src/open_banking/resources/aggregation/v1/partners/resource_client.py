"""File Generated by Sideko (sideko.dev)"""

from open_banking.core import SyncBaseClient, AsyncBaseClient
from open_banking.resources.aggregation.v1.partners.access_key import (
    AccessKeyClient,
    AsyncAccessKeyClient,
)
from open_banking.resources.aggregation.v1.partners.applications import (
    AsyncApplicationsClient,
    ApplicationsClient,
)


class PartnersClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        # register sync resources (keep comment for code generation)
        self.access_key = AccessKeyClient(base_client=self._base_client)
        self.applications = ApplicationsClient(base_client=self._base_client)

    # register sync api methods (keep comment for code generation)


class AsyncPartnersClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        # register async resources (keep comment for code generation)
        self.access_key = AsyncAccessKeyClient(base_client=self._base_client)
        self.applications = AsyncApplicationsClient(base_client=self._base_client)

    # register async api methods (keep comment for code generation)