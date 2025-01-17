"""File Generated by Sideko (sideko.dev)"""

from open_banking.core import (
    QueryParams,
    encode_param,
    AsyncBaseClient,
    SyncBaseClient,
    default_request_options,
    RequestOptions,
)
import typing


class FcraClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        # register sync resources (keep comment for code generation)

    # register sync api methods (keep comment for code generation)
    def list(
        self,
        *,
        obb_report_id: str,
        purpose: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Any:
        """
        Retrieve the report saved by _Generate Balance Analytics - FCRA_, _Generate Cash Flow Analytics - FCRA_, or _Generate Payment History - FCRA_. Requires the report ID generated by the previous call.

        Report data can either be retrieved as a JSON document or a PDF file.  To specify the format required, set the _Accept request header_ to either **application/json** or **application/pdf**. If neither is set, the report format will be returned as a JSON document.

        *Note:* this is a premium service, billable per every successful API call for non-testing customers.

        _Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)
        """
        # start -- build request data (keep comment for code generation)
        _query: QueryParams = {}
        _query["purpose"] = encode_param(purpose, False)
        # end -- build request data (keep comment for code generation)

        # start -- send sync request (keep comment for code generation)
        return self._base_client.request(
            method="GET",
            path=f"/analytics/data/v1/{obb_report_id}/fcra",
            auth_names=["FinicityAppKey", "FinicityAppToken"],
            query_params=_query,
            cast_to=typing.Any,
            request_options=request_options or default_request_options(),
        )
        # end -- send sync request (keep comment for code generation)


class AsyncFcraClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        # register async resources (keep comment for code generation)

    # register async api methods (keep comment for code generation)
    async def list(
        self,
        *,
        obb_report_id: str,
        purpose: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Any:
        """
        Retrieve the report saved by _Generate Balance Analytics - FCRA_, _Generate Cash Flow Analytics - FCRA_, or _Generate Payment History - FCRA_. Requires the report ID generated by the previous call.

        Report data can either be retrieved as a JSON document or a PDF file.  To specify the format required, set the _Accept request header_ to either **application/json** or **application/pdf**. If neither is set, the report format will be returned as a JSON document.

        *Note:* this is a premium service, billable per every successful API call for non-testing customers.

        _Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)
        """
        # start -- build request data (keep comment for code generation)
        _query: QueryParams = {}
        _query["purpose"] = encode_param(purpose, False)
        # end -- build request data (keep comment for code generation)

        # start -- send async request (keep comment for code generation)
        return await self._base_client.request(
            method="GET",
            path=f"/analytics/data/v1/{obb_report_id}/fcra",
            auth_names=["FinicityAppKey", "FinicityAppToken"],
            query_params=_query,
            cast_to=typing.Any,
            request_options=request_options or default_request_options(),
        )
        # end -- send async request (keep comment for code generation)
