"""File Generated by Sideko (sideko.dev)"""

from open_banking.core import (
    SyncBaseClient,
    AsyncBaseClient,
    default_request_options,
    RequestOptions,
    to_encodable,
)
import typing
from open_banking.types.aggregation.v1.partners.access_key import models, params


class AccessKeyClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        # register sync resources (keep comment for code generation)

    # register sync api methods (keep comment for code generation)
    def put(
        self,
        *,
        data: params.ThirdPartyAccessKeyData,
        consent_receipt_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.ThirdPartyAccessKeyReceiptData:
        """
        Update access for third party partners
        """
        # start -- build request data (keep comment for code generation)
        _json = to_encodable(
            item=data, dump_with=params._SerializerThirdPartyAccessKeyData
        )
        # end -- build request data (keep comment for code generation)

        # start -- send sync request (keep comment for code generation)
        return self._base_client.request(
            method="PUT",
            path=f"/aggregation/v1/partners/accessKey/{consent_receipt_id}",
            auth_names=["FinicityAppKey", "FinicityAppToken"],
            json=_json,
            cast_to=models.ThirdPartyAccessKeyReceiptData,
            request_options=request_options or default_request_options(),
        )
        # end -- send sync request (keep comment for code generation)

    def create(
        self,
        *,
        data: params.ThirdPartyAccessKeyData,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.ThirdPartyAccessKeyReceiptData:
        """
        Generate access key for third party partners.
        A partner can provide access to third party partners with this access key.
        """
        # start -- build request data (keep comment for code generation)
        _json = to_encodable(
            item=data, dump_with=params._SerializerThirdPartyAccessKeyData
        )
        # end -- build request data (keep comment for code generation)

        # start -- send sync request (keep comment for code generation)
        return self._base_client.request(
            method="POST",
            path="/aggregation/v1/partners/accessKey",
            auth_names=["FinicityAppKey", "FinicityAppToken"],
            json=_json,
            cast_to=models.ThirdPartyAccessKeyReceiptData,
            request_options=request_options or default_request_options(),
        )
        # end -- send sync request (keep comment for code generation)

    def delete(
        self,
        *,
        consent_receipt_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Revoke access of third party partners
        """
        # start -- build request data (keep comment for code generation)
        # end -- build request data (keep comment for code generation)

        # start -- send sync request (keep comment for code generation)
        return self._base_client.request(
            method="DELETE",
            path=f"/aggregation/v1/partners/accessKey/{consent_receipt_id}",
            auth_names=["FinicityAppKey", "FinicityAppToken"],
            cast_to=type(None),
            request_options=request_options or default_request_options(),
        )
        # end -- send sync request (keep comment for code generation)


class AsyncAccessKeyClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        # register async resources (keep comment for code generation)

    # register async api methods (keep comment for code generation)
    async def put(
        self,
        *,
        data: params.ThirdPartyAccessKeyData,
        consent_receipt_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.ThirdPartyAccessKeyReceiptData:
        """
        Update access for third party partners
        """
        # start -- build request data (keep comment for code generation)
        _json = to_encodable(
            item=data, dump_with=params._SerializerThirdPartyAccessKeyData
        )
        # end -- build request data (keep comment for code generation)

        # start -- send async request (keep comment for code generation)
        return await self._base_client.request(
            method="PUT",
            path=f"/aggregation/v1/partners/accessKey/{consent_receipt_id}",
            auth_names=["FinicityAppKey", "FinicityAppToken"],
            json=_json,
            cast_to=models.ThirdPartyAccessKeyReceiptData,
            request_options=request_options or default_request_options(),
        )
        # end -- send async request (keep comment for code generation)

    async def create(
        self,
        *,
        data: params.ThirdPartyAccessKeyData,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.ThirdPartyAccessKeyReceiptData:
        """
        Generate access key for third party partners.
        A partner can provide access to third party partners with this access key.
        """
        # start -- build request data (keep comment for code generation)
        _json = to_encodable(
            item=data, dump_with=params._SerializerThirdPartyAccessKeyData
        )
        # end -- build request data (keep comment for code generation)

        # start -- send async request (keep comment for code generation)
        return await self._base_client.request(
            method="POST",
            path="/aggregation/v1/partners/accessKey",
            auth_names=["FinicityAppKey", "FinicityAppToken"],
            json=_json,
            cast_to=models.ThirdPartyAccessKeyReceiptData,
            request_options=request_options or default_request_options(),
        )
        # end -- send async request (keep comment for code generation)

    async def delete(
        self,
        *,
        consent_receipt_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Revoke access of third party partners
        """
        # start -- build request data (keep comment for code generation)
        # end -- build request data (keep comment for code generation)

        # start -- send async request (keep comment for code generation)
        return await self._base_client.request(
            method="DELETE",
            path=f"/aggregation/v1/partners/accessKey/{consent_receipt_id}",
            auth_names=["FinicityAppKey", "FinicityAppToken"],
            cast_to=type(None),
            request_options=request_options or default_request_options(),
        )
        # end -- send async request (keep comment for code generation)
