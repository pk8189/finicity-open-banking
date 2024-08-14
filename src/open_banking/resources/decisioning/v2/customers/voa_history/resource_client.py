"""File Generated by Sideko (sideko.dev)"""

from open_banking.core import (
    AsyncBaseClient,
    SyncBaseClient,
    to_encodable,
    RequestOptions,
    encode_param,
    default_request_options,
    QueryParams,
)
from open_banking.types.decisioning.v2.customers.voa_history import params
import typing


class VoaHistoryClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        # register sync resources (keep comment for code generation)

    # register sync api methods (keep comment for code generation)
    def create(
        self,
        *,
        data: params.VoaWithIncomeReportConstraints,
        customer_id: str,
        callback_url: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Any:
        """
        Generate a Verification of Assets with Income (VOAI) report for all checking, savings, money market, and investment accounts for the given customer. This service retrieves up to 24 months of transaction history for each account and uses this information to generate the VOAI report. The report includes 1 - 6 months of all debit and credit transactions for asset verification. By default, the history is set to 61 days, however, you can change the transaction history in this section by setting the `fromDate` parameter. The report also includes up to 24 months of income credit transactions (ordered by account and confidence level) regardless of `fromDate` for income verification.

        This is a premium service. The billable event is the successful generation of a VOAI report.

        Before calling this API, a consumer must be created for the given customer ID (see Consumers APIs).

        If no account of type checking, savings, money market, or investment is found, the service will return HTTP 400 Bad Request.

        _Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)
        """
        # start -- build request data (keep comment for code generation)
        _query: QueryParams = {}
        if callback_url is not None:
            _query["callbackUrl"] = encode_param(callback_url, False)
        _json = to_encodable(
            item=data, dump_with=params._SerializerVoaWithIncomeReportConstraints
        )
        # end -- build request data (keep comment for code generation)

        # start -- send sync request (keep comment for code generation)
        return self._base_client.request(
            method="POST",
            path=f"/decisioning/v2/customers/{customer_id}/voaHistory",
            auth_names=["FinicityAppKey", "FinicityAppToken"],
            query_params=_query,
            json=_json,
            cast_to=typing.Any,
            request_options=request_options or default_request_options(),
        )
        # end -- send sync request (keep comment for code generation)


class AsyncVoaHistoryClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        # register async resources (keep comment for code generation)

    # register async api methods (keep comment for code generation)
    async def create(
        self,
        *,
        data: params.VoaWithIncomeReportConstraints,
        customer_id: str,
        callback_url: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Any:
        """
        Generate a Verification of Assets with Income (VOAI) report for all checking, savings, money market, and investment accounts for the given customer. This service retrieves up to 24 months of transaction history for each account and uses this information to generate the VOAI report. The report includes 1 - 6 months of all debit and credit transactions for asset verification. By default, the history is set to 61 days, however, you can change the transaction history in this section by setting the `fromDate` parameter. The report also includes up to 24 months of income credit transactions (ordered by account and confidence level) regardless of `fromDate` for income verification.

        This is a premium service. The billable event is the successful generation of a VOAI report.

        Before calling this API, a consumer must be created for the given customer ID (see Consumers APIs).

        If no account of type checking, savings, money market, or investment is found, the service will return HTTP 400 Bad Request.

        _Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)
        """
        # start -- build request data (keep comment for code generation)
        _query: QueryParams = {}
        if callback_url is not None:
            _query["callbackUrl"] = encode_param(callback_url, False)
        _json = to_encodable(
            item=data, dump_with=params._SerializerVoaWithIncomeReportConstraints
        )
        # end -- build request data (keep comment for code generation)

        # start -- send async request (keep comment for code generation)
        return await self._base_client.request(
            method="POST",
            path=f"/decisioning/v2/customers/{customer_id}/voaHistory",
            auth_names=["FinicityAppKey", "FinicityAppToken"],
            query_params=_query,
            json=_json,
            cast_to=typing.Any,
            request_options=request_options or default_request_options(),
        )
        # end -- send async request (keep comment for code generation)
