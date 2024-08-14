"""File Generated by Sideko (sideko.dev)"""

from open_banking.core import SyncBaseClient, AsyncBaseClient
from open_banking.resources.connect.experiences import (
    AsyncExperiencesClient,
    ExperiencesClient,
)
from open_banking.resources.connect.v2 import V2Client, AsyncV2Client


class ConnectClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        # register sync resources (keep comment for code generation)
        self.experiences = ExperiencesClient(base_client=self._base_client)
        self.v2 = V2Client(base_client=self._base_client)

    # register sync api methods (keep comment for code generation)


class AsyncConnectClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        # register async resources (keep comment for code generation)
        self.experiences = AsyncExperiencesClient(base_client=self._base_client)
        self.v2 = AsyncV2Client(base_client=self._base_client)

    # register async api methods (keep comment for code generation)