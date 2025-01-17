"""File Generated by Sideko (sideko.dev)"""

from open_banking.core import SyncBaseClient, AsyncBaseClient
from open_banking.resources.microentry.v1 import V1Client, AsyncV1Client


class MicroentryClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        # register sync resources (keep comment for code generation)
        self.v1 = V1Client(base_client=self._base_client)

    # register sync api methods (keep comment for code generation)


class AsyncMicroentryClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        # register async resources (keep comment for code generation)
        self.v1 = AsyncV1Client(base_client=self._base_client)

    # register async api methods (keep comment for code generation)
