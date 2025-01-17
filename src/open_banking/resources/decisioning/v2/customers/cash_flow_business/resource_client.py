"""File Generated by Sideko (sideko.dev)"""

from open_banking.core import (
    default_request_options,
    QueryParams,
    AsyncBaseClient,
    encode_param,
    to_encodable,
    SyncBaseClient,
    RequestOptions,
)
from open_banking.types.decisioning.v2.customers.cash_flow_business import params
import typing


class CashFlowBusinessClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        # register sync resources (keep comment for code generation)

    # register sync api methods (keep comment for code generation)
    def create(
        self,
        *,
        data: params.CashFlowReportConstraints,
        customer_id: str,
        callback_url: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Any:
        """
        Generate a Cash Flow Report (Business) report for all checking and savings under the given customer. This service retrieves up to two years of transaction history for the given account. It then uses this information to generate the CFR report. A consumer is not required to generate this report.

        This report is not provided under FCRA rules, and this report is not available in the Finicity Consumer Portal for the borrower to view.

        If no account type of checking or savings is found, the service will return HTTP 400 Bad Request.

        _Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)
        """
        # start -- build request data (keep comment for code generation)
        _query: QueryParams = {}
        if callback_url is not None:
            _query["callbackUrl"] = encode_param(callback_url, False)
        _json = to_encodable(
            item=data, dump_with=params._SerializerCashFlowReportConstraints
        )
        # end -- build request data (keep comment for code generation)

        # start -- send sync request (keep comment for code generation)
        return self._base_client.request(
            method="POST",
            path=f"/decisioning/v2/customers/{customer_id}/cashFlowBusiness",
            auth_names=["FinicityAppKey", "FinicityAppToken"],
            query_params=_query,
            json=_json,
            cast_to=typing.Any,
            request_options=request_options or default_request_options(),
        )
        # end -- send sync request (keep comment for code generation)


class AsyncCashFlowBusinessClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        # register async resources (keep comment for code generation)

    # register async api methods (keep comment for code generation)
    async def create(
        self,
        *,
        data: params.CashFlowReportConstraints,
        customer_id: str,
        callback_url: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Any:
        """
        Generate a Cash Flow Report (Business) report for all checking and savings under the given customer. This service retrieves up to two years of transaction history for the given account. It then uses this information to generate the CFR report. A consumer is not required to generate this report.

        This report is not provided under FCRA rules, and this report is not available in the Finicity Consumer Portal for the borrower to view.

        If no account type of checking or savings is found, the service will return HTTP 400 Bad Request.

        _Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)
        """
        # start -- build request data (keep comment for code generation)
        _query: QueryParams = {}
        if callback_url is not None:
            _query["callbackUrl"] = encode_param(callback_url, False)
        _json = to_encodable(
            item=data, dump_with=params._SerializerCashFlowReportConstraints
        )
        # end -- build request data (keep comment for code generation)

        # start -- send async request (keep comment for code generation)
        return await self._base_client.request(
            method="POST",
            path=f"/decisioning/v2/customers/{customer_id}/cashFlowBusiness",
            auth_names=["FinicityAppKey", "FinicityAppToken"],
            query_params=_query,
            json=_json,
            cast_to=typing.Any,
            request_options=request_options or default_request_options(),
        )
        # end -- send async request (keep comment for code generation)
