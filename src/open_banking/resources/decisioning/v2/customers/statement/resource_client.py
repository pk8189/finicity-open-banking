"""File Generated by Sideko (sideko.dev)"""

from open_banking.core import (
    RequestOptions,
    encode_param,
    default_request_options,
    SyncBaseClient,
    QueryParams,
    AsyncBaseClient,
    to_encodable,
)
from open_banking.types.decisioning.v2.customers.statement import params
import typing


class StatementClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        # register sync resources (keep comment for code generation)

    # register sync api methods (keep comment for code generation)
    def create(
        self,
        *,
        data: params.StatementReportConstraints,
        customer_id: str,
        callback_url: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Any:
        """
        Generate a Statement Report for the given accounts under the given customer.

        This is a premium service. A billable event will be created upon the successful generation of the Statement Report.

        Before calling this API, a consumer must be created for the given customer ID (see Consumers APIs).

        _Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)
        """
        # start -- build request data (keep comment for code generation)
        _query: QueryParams = {}
        if callback_url is not None:
            _query["callbackUrl"] = encode_param(callback_url, False)
        _json = to_encodable(
            item=data, dump_with=params._SerializerStatementReportConstraints
        )
        # end -- build request data (keep comment for code generation)

        # start -- send sync request (keep comment for code generation)
        return self._base_client.request(
            method="POST",
            path=f"/decisioning/v2/customers/{customer_id}/statement",
            auth_names=["FinicityAppKey", "FinicityAppToken"],
            query_params=_query,
            json=_json,
            cast_to=typing.Any,
            request_options=request_options or default_request_options(),
        )
        # end -- send sync request (keep comment for code generation)


class AsyncStatementClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        # register async resources (keep comment for code generation)

    # register async api methods (keep comment for code generation)
    async def create(
        self,
        *,
        data: params.StatementReportConstraints,
        customer_id: str,
        callback_url: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Any:
        """
        Generate a Statement Report for the given accounts under the given customer.

        This is a premium service. A billable event will be created upon the successful generation of the Statement Report.

        Before calling this API, a consumer must be created for the given customer ID (see Consumers APIs).

        _Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)
        """
        # start -- build request data (keep comment for code generation)
        _query: QueryParams = {}
        if callback_url is not None:
            _query["callbackUrl"] = encode_param(callback_url, False)
        _json = to_encodable(
            item=data, dump_with=params._SerializerStatementReportConstraints
        )
        # end -- build request data (keep comment for code generation)

        # start -- send async request (keep comment for code generation)
        return await self._base_client.request(
            method="POST",
            path=f"/decisioning/v2/customers/{customer_id}/statement",
            auth_names=["FinicityAppKey", "FinicityAppToken"],
            query_params=_query,
            json=_json,
            cast_to=typing.Any,
            request_options=request_options or default_request_options(),
        )
        # end -- send async request (keep comment for code generation)
