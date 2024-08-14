"""File Generated by Sideko (sideko.dev)"""

from open_banking.core import SyncBaseClient, AsyncBaseClient
from open_banking.resources.institution.v2.certified_institutions import (
    AsyncCertifiedInstitutionsClient,
    CertifiedInstitutionsClient,
)
from open_banking.resources.institution.v2.institutions import (
    AsyncInstitutionsClient,
    InstitutionsClient,
)


class V2Client:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        # register sync resources (keep comment for code generation)
        self.certified_institutions = CertifiedInstitutionsClient(
            base_client=self._base_client
        )
        self.institutions = InstitutionsClient(base_client=self._base_client)

    # register sync api methods (keep comment for code generation)


class AsyncV2Client:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        # register async resources (keep comment for code generation)
        self.certified_institutions = AsyncCertifiedInstitutionsClient(
            base_client=self._base_client
        )
        self.institutions = AsyncInstitutionsClient(base_client=self._base_client)

    # register async api methods (keep comment for code generation)