"""File Generated by Sideko (sideko.dev)"""

from open_banking.core import (
    SyncBaseClient,
    to_encodable,
    AsyncBaseClient,
    default_request_options,
    RequestOptions,
)
from open_banking.types.connect.v2.generate.microentry.verify import params, models
import typing


class VerifyClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        # register sync resources (keep comment for code generation)

    # register sync api methods (keep comment for code generation)
    def create(
        self,
        *,
        data: params.MicroEntryVerifyRequestParameter,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.ConnectUrl:
        """
        The UI re-engages the consumer to enter two microdeposit amounts found in their account and validates them.

        _Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)
        """
        # start -- build request data (keep comment for code generation)
        _json = to_encodable(
            item=data, dump_with=params._SerializerMicroEntryVerifyRequestParameter
        )
        # end -- build request data (keep comment for code generation)

        # start -- send sync request (keep comment for code generation)
        return self._base_client.request(
            method="POST",
            path="/connect/v2/generate/microentry/verify",
            auth_names=["FinicityAppKey", "FinicityAppToken"],
            json=_json,
            cast_to=models.ConnectUrl,
            request_options=request_options or default_request_options(),
        )
        # end -- send sync request (keep comment for code generation)


class AsyncVerifyClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        # register async resources (keep comment for code generation)

    # register async api methods (keep comment for code generation)
    async def create(
        self,
        *,
        data: params.MicroEntryVerifyRequestParameter,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.ConnectUrl:
        """
        The UI re-engages the consumer to enter two microdeposit amounts found in their account and validates them.

        _Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)
        """
        # start -- build request data (keep comment for code generation)
        _json = to_encodable(
            item=data, dump_with=params._SerializerMicroEntryVerifyRequestParameter
        )
        # end -- build request data (keep comment for code generation)

        # start -- send async request (keep comment for code generation)
        return await self._base_client.request(
            method="POST",
            path="/connect/v2/generate/microentry/verify",
            auth_names=["FinicityAppKey", "FinicityAppToken"],
            json=_json,
            cast_to=models.ConnectUrl,
            request_options=request_options or default_request_options(),
        )
        # end -- send async request (keep comment for code generation)
