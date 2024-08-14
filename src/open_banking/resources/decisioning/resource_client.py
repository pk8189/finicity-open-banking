"""File Generated by Sideko (sideko.dev)"""

from open_banking.core import AsyncBaseClient, SyncBaseClient
from open_banking.resources.decisioning.v1 import V1Client, AsyncV1Client
from open_banking.resources.decisioning.v3 import AsyncV3Client, V3Client
from open_banking.resources.decisioning.v2 import V2Client, AsyncV2Client


class DecisioningClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        # register sync resources (keep comment for code generation)
        self.v1 = V1Client(base_client=self._base_client)
        self.v3 = V3Client(base_client=self._base_client)
        self.v2 = V2Client(base_client=self._base_client)

    # register sync api methods (keep comment for code generation)


class AsyncDecisioningClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        # register async resources (keep comment for code generation)
        self.v1 = AsyncV1Client(base_client=self._base_client)
        self.v3 = AsyncV3Client(base_client=self._base_client)
        self.v2 = AsyncV2Client(base_client=self._base_client)

    # register async api methods (keep comment for code generation)