"""File Generated by Sideko (sideko.dev)"""

from open_banking.core import (
    RequestOptions,
    AsyncBaseClient,
    to_encodable,
    SyncBaseClient,
    default_request_options,
)
from open_banking.types.aggregation.v1.partners.applications import models, params
import typing


class ApplicationsClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        # register sync resources (keep comment for code generation)

    # register sync api methods (keep comment for code generation)
    def put(
        self,
        *,
        data: params.Application,
        pre_app_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.RegisteredApplication:
        """
        Update a registered application.

        _Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)
        """
        # start -- build request data (keep comment for code generation)
        _json = to_encodable(item=data, dump_with=params._SerializerApplication)
        # end -- build request data (keep comment for code generation)

        # start -- send sync request (keep comment for code generation)
        return self._base_client.request(
            method="PUT",
            path=f"/aggregation/v1/partners/applications/{pre_app_id}",
            auth_names=["FinicityAppKey", "FinicityAppToken"],
            json=_json,
            cast_to=models.RegisteredApplication,
            request_options=request_options or default_request_options(),
        )
        # end -- send sync request (keep comment for code generation)

    def create(
        self,
        *,
        data: params.Application,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.RegisteredApplication:
        """
        Register a new application to access financial institutions using OAuth connections.

        _Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)
        """
        # start -- build request data (keep comment for code generation)
        _json = to_encodable(item=data, dump_with=params._SerializerApplication)
        # end -- build request data (keep comment for code generation)

        # start -- send sync request (keep comment for code generation)
        return self._base_client.request(
            method="POST",
            path="/aggregation/v1/partners/applications",
            auth_names=["FinicityAppKey", "FinicityAppToken"],
            json=_json,
            cast_to=models.RegisteredApplication,
            request_options=request_options or default_request_options(),
        )
        # end -- send sync request (keep comment for code generation)


class AsyncApplicationsClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        # register async resources (keep comment for code generation)

    # register async api methods (keep comment for code generation)
    async def put(
        self,
        *,
        data: params.Application,
        pre_app_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.RegisteredApplication:
        """
        Update a registered application.

        _Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)
        """
        # start -- build request data (keep comment for code generation)
        _json = to_encodable(item=data, dump_with=params._SerializerApplication)
        # end -- build request data (keep comment for code generation)

        # start -- send async request (keep comment for code generation)
        return await self._base_client.request(
            method="PUT",
            path=f"/aggregation/v1/partners/applications/{pre_app_id}",
            auth_names=["FinicityAppKey", "FinicityAppToken"],
            json=_json,
            cast_to=models.RegisteredApplication,
            request_options=request_options or default_request_options(),
        )
        # end -- send async request (keep comment for code generation)

    async def create(
        self,
        *,
        data: params.Application,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.RegisteredApplication:
        """
        Register a new application to access financial institutions using OAuth connections.

        _Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)
        """
        # start -- build request data (keep comment for code generation)
        _json = to_encodable(item=data, dump_with=params._SerializerApplication)
        # end -- build request data (keep comment for code generation)

        # start -- send async request (keep comment for code generation)
        return await self._base_client.request(
            method="POST",
            path="/aggregation/v1/partners/applications",
            auth_names=["FinicityAppKey", "FinicityAppToken"],
            json=_json,
            cast_to=models.RegisteredApplication,
            request_options=request_options or default_request_options(),
        )
        # end -- send async request (keep comment for code generation)