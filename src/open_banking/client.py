"""File Generated by Sideko (sideko.dev)"""

import httpx
import typing
from open_banking.environment import Environment
from open_banking.core import SyncBaseClient, AuthKeyHeader, AsyncBaseClient
from open_banking.resources.aggregation import AsyncAggregationClient, AggregationClient
from open_banking.resources.analytics import AsyncAnalyticsClient, AnalyticsClient
from open_banking.resources.applications import (
    ApplicationsClient,
    AsyncApplicationsClient,
)
from open_banking.resources.business_services import (
    AsyncBusinessServicesClient,
    BusinessServicesClient,
)
from open_banking.resources.connect import AsyncConnectClient, ConnectClient
from open_banking.resources.customers import CustomersClient, AsyncCustomersClient
from open_banking.resources.decisioning import AsyncDecisioningClient, DecisioningClient
from open_banking.resources.institution import AsyncInstitutionClient, InstitutionClient
from open_banking.resources.microentry import MicroentryClient, AsyncMicroentryClient


class Client:
    def __init__(
        self,
        *,
        base_url: typing.Optional[str] = None,
        environment: Environment = Environment.DEFAULT,
        timeout: typing.Optional[float] = 60,
        httpx_client: typing.Optional[httpx.Client] = None,
        finicity_app_key: typing.Optional[str] = None,
        finicity_app_token: typing.Optional[str] = None,
    ):
        self._base_client = SyncBaseClient(
            base_url=_get_base_url(base_url=base_url, environment=environment),
            httpx_client=(
                httpx.Client(timeout=timeout) if httpx_client is None else httpx_client
            ),
        )

        # register auth methods (keep comment for code generation)
        self._base_client.register_auth(
            "FinicityAppKey",
            AuthKeyHeader(header_name="Finicity-App-Key", val=finicity_app_key),
        )
        self._base_client.register_auth(
            "FinicityAppToken",
            AuthKeyHeader(header_name="Finicity-App-Token", val=finicity_app_token),
        )

        # register sync resources (keep comment for code generation)
        self.aggregation = AggregationClient(base_client=self._base_client)
        self.analytics = AnalyticsClient(base_client=self._base_client)
        self.applications = ApplicationsClient(base_client=self._base_client)
        self.business_services = BusinessServicesClient(base_client=self._base_client)
        self.connect = ConnectClient(base_client=self._base_client)
        self.customers = CustomersClient(base_client=self._base_client)
        self.decisioning = DecisioningClient(base_client=self._base_client)
        self.institution = InstitutionClient(base_client=self._base_client)
        self.microentry = MicroentryClient(base_client=self._base_client)

    # register sync api methods (keep comment for code generation)


class AsyncClient:
    def __init__(
        self,
        *,
        base_url: typing.Optional[str] = None,
        environment: Environment = Environment.DEFAULT,
        timeout: typing.Optional[float] = 60,
        httpx_client: typing.Optional[httpx.AsyncClient] = None,
        finicity_app_key: typing.Optional[str] = None,
        finicity_app_token: typing.Optional[str] = None,
    ):
        self._base_client = AsyncBaseClient(
            base_url=_get_base_url(base_url=base_url, environment=environment),
            httpx_client=(
                httpx.AsyncClient(timeout=timeout)
                if httpx_client is None
                else httpx_client
            ),
        )

        # register auth methods (keep comment for code generation)
        self._base_client.register_auth(
            "FinicityAppKey",
            AuthKeyHeader(header_name="Finicity-App-Key", val=finicity_app_key),
        )
        self._base_client.register_auth(
            "FinicityAppToken",
            AuthKeyHeader(header_name="Finicity-App-Token", val=finicity_app_token),
        )

        # register async resources (keep comment for code generation)
        self.aggregation = AsyncAggregationClient(base_client=self._base_client)
        self.analytics = AsyncAnalyticsClient(base_client=self._base_client)
        self.applications = AsyncApplicationsClient(base_client=self._base_client)
        self.business_services = AsyncBusinessServicesClient(
            base_client=self._base_client
        )
        self.connect = AsyncConnectClient(base_client=self._base_client)
        self.customers = AsyncCustomersClient(base_client=self._base_client)
        self.decisioning = AsyncDecisioningClient(base_client=self._base_client)
        self.institution = AsyncInstitutionClient(base_client=self._base_client)
        self.microentry = AsyncMicroentryClient(base_client=self._base_client)

    # register async api methods (keep comment for code generation)


def _get_base_url(
    *, base_url: typing.Optional[str] = None, environment: Environment
) -> str:
    if base_url is not None:
        return base_url
    elif environment is not None:
        return environment.value
    else:
        raise Exception("Must include a base_url or environment arguments")
