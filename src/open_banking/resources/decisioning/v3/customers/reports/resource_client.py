"""File Generated by Sideko (sideko.dev)"""

from open_banking.core import (
    AsyncBaseClient,
    encode_param,
    default_request_options,
    SyncBaseClient,
    RequestOptions,
    QueryParams,
)
import typing


class ReportsClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        # register sync resources (keep comment for code generation)

    # register sync api methods (keep comment for code generation)
    def get(
        self,
        *,
        customer_id: str,
        report_id: str,
        on_behalf_of: typing.Optional[str] = None,
        purpose: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Get a report that has been generated by a previous call to one of the Generate Report services.

        The report's `status` field contains "inProgress", "failure", or "success". If the status shows "inProgress", the client app should wait 20 seconds and then call this API again.

        Report data can either be retrieved as a JSON document or a PDF file.  To specify the format required, set the _Accept request header_ to either **application/json** or **application/pdf**. If neither is set, the report format will be returned as a JSON document.

        _Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)
        """
        # start -- build request data (keep comment for code generation)
        _query: QueryParams = {}
        if on_behalf_of is not None:
            _query["onBehalfOf"] = encode_param(on_behalf_of, False)
        if purpose is not None:
            _query["purpose"] = encode_param(purpose, False)
        # end -- build request data (keep comment for code generation)

        # start -- send sync request (keep comment for code generation)
        return self._base_client.request(
            method="GET",
            path=f"/decisioning/v3/customers/{customer_id}/reports/{report_id}",
            auth_names=["FinicityAppKey", "FinicityAppToken"],
            query_params=_query,
            cast_to=typing.Dict[str, typing.Any],
            request_options=request_options or default_request_options(),
        )
        # end -- send sync request (keep comment for code generation)


class AsyncReportsClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        # register async resources (keep comment for code generation)

    # register async api methods (keep comment for code generation)
    async def get(
        self,
        *,
        customer_id: str,
        report_id: str,
        on_behalf_of: typing.Optional[str] = None,
        purpose: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Get a report that has been generated by a previous call to one of the Generate Report services.

        The report's `status` field contains "inProgress", "failure", or "success". If the status shows "inProgress", the client app should wait 20 seconds and then call this API again.

        Report data can either be retrieved as a JSON document or a PDF file.  To specify the format required, set the _Accept request header_ to either **application/json** or **application/pdf**. If neither is set, the report format will be returned as a JSON document.

        _Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)
        """
        # start -- build request data (keep comment for code generation)
        _query: QueryParams = {}
        if on_behalf_of is not None:
            _query["onBehalfOf"] = encode_param(on_behalf_of, False)
        if purpose is not None:
            _query["purpose"] = encode_param(purpose, False)
        # end -- build request data (keep comment for code generation)

        # start -- send async request (keep comment for code generation)
        return await self._base_client.request(
            method="GET",
            path=f"/decisioning/v3/customers/{customer_id}/reports/{report_id}",
            auth_names=["FinicityAppKey", "FinicityAppToken"],
            query_params=_query,
            cast_to=typing.Dict[str, typing.Any],
            request_options=request_options or default_request_options(),
        )
        # end -- send async request (keep comment for code generation)
