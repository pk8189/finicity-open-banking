"""File Generated by Sideko (sideko.dev)"""

from open_banking.core import (
    default_request_options,
    AsyncBaseClient,
    SyncBaseClient,
    encode_param,
    RequestOptions,
    QueryParams,
)
import typing
from open_banking.types.decisioning.v1.consumers.reports import models


class ReportsClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        # register sync resources (keep comment for code generation)

    # register sync api methods (keep comment for code generation)
    def list(
        self,
        *,
        consumer_id: str,
        purpose: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.ReportSummaries:
        """
        Get all reports that have been generated by previous calls to Generate Report services for the given consumer.

        The `status` fields in the returned list contain "inProgress", "failure", or "success". If the status shows "inProgress", the client app should wait 20 seconds and then call this API again.

        _Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)
        """
        # start -- build request data (keep comment for code generation)
        _query: QueryParams = {}
        if purpose is not None:
            _query["purpose"] = encode_param(purpose, False)
        # end -- build request data (keep comment for code generation)

        # start -- send sync request (keep comment for code generation)
        return self._base_client.request(
            method="GET",
            path=f"/decisioning/v1/consumers/{consumer_id}/reports",
            auth_names=["FinicityAppKey", "FinicityAppToken"],
            query_params=_query,
            cast_to=models.ReportSummaries,
            request_options=request_options or default_request_options(),
        )
        # end -- send sync request (keep comment for code generation)


class AsyncReportsClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        # register async resources (keep comment for code generation)

    # register async api methods (keep comment for code generation)
    async def list(
        self,
        *,
        consumer_id: str,
        purpose: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.ReportSummaries:
        """
        Get all reports that have been generated by previous calls to Generate Report services for the given consumer.

        The `status` fields in the returned list contain "inProgress", "failure", or "success". If the status shows "inProgress", the client app should wait 20 seconds and then call this API again.

        _Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)
        """
        # start -- build request data (keep comment for code generation)
        _query: QueryParams = {}
        if purpose is not None:
            _query["purpose"] = encode_param(purpose, False)
        # end -- build request data (keep comment for code generation)

        # start -- send async request (keep comment for code generation)
        return await self._base_client.request(
            method="GET",
            path=f"/decisioning/v1/consumers/{consumer_id}/reports",
            auth_names=["FinicityAppKey", "FinicityAppToken"],
            query_params=_query,
            cast_to=models.ReportSummaries,
            request_options=request_options or default_request_options(),
        )
        # end -- send async request (keep comment for code generation)
