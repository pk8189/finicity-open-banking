"""File Generated by Sideko (sideko.dev)"""

from open_banking.core import (
    SyncBaseClient,
    RequestOptions,
    AsyncBaseClient,
    default_request_options,
    to_encodable,
)
import typing
from open_banking.types.decisioning.v1.customers.consumer import params, models


class ConsumerClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        # register sync resources (keep comment for code generation)

    # register sync api methods (keep comment for code generation)
    def create(
        self,
        *,
        data: params.NewConsumer,
        customer_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.CreatedConsumer:
        """
        Create a consumer record associated with the given customer. A consumer persists as the owner of any reports that are generated, even after the original customer is deleted from the system.

        A consumer must be created for the given customer before calling any of the Generate Report services.

        _Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)
        """
        # start -- build request data (keep comment for code generation)
        _json = to_encodable(item=data, dump_with=params._SerializerNewConsumer)
        # end -- build request data (keep comment for code generation)

        # start -- send sync request (keep comment for code generation)
        return self._base_client.request(
            method="POST",
            path=f"/decisioning/v1/customers/{customer_id}/consumer",
            auth_names=["FinicityAppKey", "FinicityAppToken"],
            json=_json,
            cast_to=models.CreatedConsumer,
            request_options=request_options or default_request_options(),
        )
        # end -- send sync request (keep comment for code generation)

    def list(
        self,
        *,
        customer_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Consumer:
        """
        Get the details of a consumer record by customer ID.

        _Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)
        """
        # start -- build request data (keep comment for code generation)
        # end -- build request data (keep comment for code generation)

        # start -- send sync request (keep comment for code generation)
        return self._base_client.request(
            method="GET",
            path=f"/decisioning/v1/customers/{customer_id}/consumer",
            auth_names=["FinicityAppKey", "FinicityAppToken"],
            cast_to=models.Consumer,
            request_options=request_options or default_request_options(),
        )
        # end -- send sync request (keep comment for code generation)


class AsyncConsumerClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        # register async resources (keep comment for code generation)

    # register async api methods (keep comment for code generation)
    async def create(
        self,
        *,
        data: params.NewConsumer,
        customer_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.CreatedConsumer:
        """
        Create a consumer record associated with the given customer. A consumer persists as the owner of any reports that are generated, even after the original customer is deleted from the system.

        A consumer must be created for the given customer before calling any of the Generate Report services.

        _Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)
        """
        # start -- build request data (keep comment for code generation)
        _json = to_encodable(item=data, dump_with=params._SerializerNewConsumer)
        # end -- build request data (keep comment for code generation)

        # start -- send async request (keep comment for code generation)
        return await self._base_client.request(
            method="POST",
            path=f"/decisioning/v1/customers/{customer_id}/consumer",
            auth_names=["FinicityAppKey", "FinicityAppToken"],
            json=_json,
            cast_to=models.CreatedConsumer,
            request_options=request_options or default_request_options(),
        )
        # end -- send async request (keep comment for code generation)

    async def list(
        self,
        *,
        customer_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Consumer:
        """
        Get the details of a consumer record by customer ID.

        _Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)
        """
        # start -- build request data (keep comment for code generation)
        # end -- build request data (keep comment for code generation)

        # start -- send async request (keep comment for code generation)
        return await self._base_client.request(
            method="GET",
            path=f"/decisioning/v1/customers/{customer_id}/consumer",
            auth_names=["FinicityAppKey", "FinicityAppToken"],
            cast_to=models.Consumer,
            request_options=request_options or default_request_options(),
        )
        # end -- send async request (keep comment for code generation)
