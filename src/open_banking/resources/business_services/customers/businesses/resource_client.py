"""File Generated by Sideko (sideko.dev)"""

from open_banking.core import (
    AsyncBaseClient,
    to_encodable,
    RequestOptions,
    default_request_options,
    SyncBaseClient,
)
import typing
from open_banking.types.business_services.customers.businesses import params


class BusinessesClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        # register sync resources (keep comment for code generation)

    # register sync api methods (keep comment for code generation)
    def create(
        self,
        *,
        data: params.NewBusiness,
        customer_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Any:
        """
        Create a new business record for the associated customer.
        A customer can have one business record associated.

        _Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)
        """
        # start -- build request data (keep comment for code generation)
        _json = to_encodable(item=data, dump_with=params._SerializerNewBusiness)
        # end -- build request data (keep comment for code generation)

        # start -- send sync request (keep comment for code generation)
        return self._base_client.request(
            method="POST",
            path=f"/business-services/customers/{customer_id}/businesses",
            auth_names=["FinicityAppKey", "FinicityAppToken"],
            json=_json,
            cast_to=typing.Any,
            request_options=request_options or default_request_options(),
        )
        # end -- send sync request (keep comment for code generation)

    def list(
        self,
        *,
        customer_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[typing.Any]:
        """
        Retrieve business details associated with a specific customer. By providing the unique customer identifier, details about the associated business can be accessed.

        _Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)
        """
        # start -- build request data (keep comment for code generation)
        # end -- build request data (keep comment for code generation)

        # start -- send sync request (keep comment for code generation)
        return self._base_client.request(
            method="GET",
            path=f"/business-services/customers/{customer_id}/businesses",
            auth_names=["FinicityAppKey", "FinicityAppToken"],
            cast_to=typing.List[typing.Any],
            request_options=request_options or default_request_options(),
        )
        # end -- send sync request (keep comment for code generation)


class AsyncBusinessesClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        # register async resources (keep comment for code generation)

    # register async api methods (keep comment for code generation)
    async def create(
        self,
        *,
        data: params.NewBusiness,
        customer_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Any:
        """
        Create a new business record for the associated customer.
        A customer can have one business record associated.

        _Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)
        """
        # start -- build request data (keep comment for code generation)
        _json = to_encodable(item=data, dump_with=params._SerializerNewBusiness)
        # end -- build request data (keep comment for code generation)

        # start -- send async request (keep comment for code generation)
        return await self._base_client.request(
            method="POST",
            path=f"/business-services/customers/{customer_id}/businesses",
            auth_names=["FinicityAppKey", "FinicityAppToken"],
            json=_json,
            cast_to=typing.Any,
            request_options=request_options or default_request_options(),
        )
        # end -- send async request (keep comment for code generation)

    async def list(
        self,
        *,
        customer_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[typing.Any]:
        """
        Retrieve business details associated with a specific customer. By providing the unique customer identifier, details about the associated business can be accessed.

        _Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)
        """
        # start -- build request data (keep comment for code generation)
        # end -- build request data (keep comment for code generation)

        # start -- send async request (keep comment for code generation)
        return await self._base_client.request(
            method="GET",
            path=f"/business-services/customers/{customer_id}/businesses",
            auth_names=["FinicityAppKey", "FinicityAppToken"],
            cast_to=typing.List[typing.Any],
            request_options=request_options or default_request_options(),
        )
        # end -- send async request (keep comment for code generation)
