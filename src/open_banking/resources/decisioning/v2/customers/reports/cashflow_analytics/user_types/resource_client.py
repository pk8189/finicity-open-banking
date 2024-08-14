"""File Generated by Sideko (sideko.dev)"""

from open_banking.core import (
    QueryParams,
    default_request_options,
    encode_param,
    to_encodable,
    RequestOptions,
    SyncBaseClient,
    AsyncBaseClient,
)
from open_banking.types.decisioning.v2.customers.reports.cashflow_analytics.user_types import (
    params,
)
import typing


class UserTypesClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        # register sync resources (keep comment for code generation)

    # register sync api methods (keep comment for code generation)
    def create(
        self,
        *,
        data: params.AnalyticsReportConstraints,
        customer_id: str,
        user_type: str,
        callback_url: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Any:
        """
        Generate a Cashflow Analytics Report for a given customer. This service retrieves up to two years of transaction history from connected accounts.

        Cashflow Analytics analyzes transaction over time to report metrics and identify behavior that may indicate risk.

        Before calling this API, a consumer or business may need to be created for the given customer ID based on the user type (see Consumer/Business APIs).

        If no account type of checking or savings is found, the service will return HTTP 400 Bad Request.

        This is a premium service, billable per every successful API call for non-testing customers. A successful call to this API will generate analytics report which can be retrieved via Get Report by Customer or Get Report by Consumer.

        _Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)
        """
        # start -- build request data (keep comment for code generation)
        _query: QueryParams = {}
        if callback_url is not None:
            _query["callbackUrl"] = encode_param(callback_url, False)
        _json = to_encodable(
            item=data, dump_with=params._SerializerAnalyticsReportConstraints
        )
        # end -- build request data (keep comment for code generation)

        # start -- send sync request (keep comment for code generation)
        return self._base_client.request(
            method="POST",
            path=f"/decisioning/v2/customers/{customer_id}/reports/cashflow-analytics/userTypes/{user_type}",
            auth_names=["FinicityAppKey", "FinicityAppToken"],
            query_params=_query,
            json=_json,
            cast_to=typing.Any,
            request_options=request_options or default_request_options(),
        )
        # end -- send sync request (keep comment for code generation)


class AsyncUserTypesClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        # register async resources (keep comment for code generation)

    # register async api methods (keep comment for code generation)
    async def create(
        self,
        *,
        data: params.AnalyticsReportConstraints,
        customer_id: str,
        user_type: str,
        callback_url: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Any:
        """
        Generate a Cashflow Analytics Report for a given customer. This service retrieves up to two years of transaction history from connected accounts.

        Cashflow Analytics analyzes transaction over time to report metrics and identify behavior that may indicate risk.

        Before calling this API, a consumer or business may need to be created for the given customer ID based on the user type (see Consumer/Business APIs).

        If no account type of checking or savings is found, the service will return HTTP 400 Bad Request.

        This is a premium service, billable per every successful API call for non-testing customers. A successful call to this API will generate analytics report which can be retrieved via Get Report by Customer or Get Report by Consumer.

        _Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)
        """
        # start -- build request data (keep comment for code generation)
        _query: QueryParams = {}
        if callback_url is not None:
            _query["callbackUrl"] = encode_param(callback_url, False)
        _json = to_encodable(
            item=data, dump_with=params._SerializerAnalyticsReportConstraints
        )
        # end -- build request data (keep comment for code generation)

        # start -- send async request (keep comment for code generation)
        return await self._base_client.request(
            method="POST",
            path=f"/decisioning/v2/customers/{customer_id}/reports/cashflow-analytics/userTypes/{user_type}",
            auth_names=["FinicityAppKey", "FinicityAppToken"],
            query_params=_query,
            json=_json,
            cast_to=typing.Any,
            request_options=request_options or default_request_options(),
        )
        # end -- send async request (keep comment for code generation)
