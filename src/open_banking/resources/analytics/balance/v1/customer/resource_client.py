"""File Generated by Sideko (sideko.dev)"""

from open_banking.core import (
    RequestOptions,
    QueryParams,
    AsyncBaseClient,
    SyncBaseClient,
    encode_param,
    to_encodable,
    default_request_options,
)
from open_banking.resources.analytics.balance.v1.customer.fcra import (
    AsyncFcraClient,
    FcraClient,
)
from open_banking.types.analytics.balance.v1.customer import params, models
import typing


class CustomerClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        # register sync resources (keep comment for code generation)
        self.fcra = FcraClient(base_client=self._base_client)

    # register sync api methods (keep comment for code generation)
    def create(
        self,
        *,
        data: params.BalanceAndCashFlowAnalyticsReportConstraints,
        customer_id: str,
        reference_number: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.ObbAnalyticsReportAck:
        """
        Balance Analytics for Business analyzes bank balances over time to report metrics and identify behavior that may indicate risk.

        Calculated metrics include:
        * Current/available account balances
        * Minimum/maximum/average account balances over the requested time
          period and broken down by month

        * Daily ending balance of accounts for each day in the requested time
          period

        * Propensity of the customer's account balances to increase week over
          week

        * Number of days in the requested time period ending with a negative
          balance


        This version of the API is intended for piloting and integration testing your application with the Balance Analytics product. It does not adhere to FCRA requirements, and should not be used for production/lending purposes. See _Generate Balance Analytics - FCRA_ for the FCRA compliant version of this API.

        A successful call to this API will generate analytics and store a report within Finicity. The report can be retrieved via _Get Balance Analytics Report_ (operation: _GetObbAnalyticsReport_).

        _Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)
        """
        # start -- build request data (keep comment for code generation)
        _query: QueryParams = {}
        if reference_number is not None:
            _query["reference-number"] = encode_param(reference_number, False)
        _json = to_encodable(
            item=data,
            dump_with=params._SerializerBalanceAndCashFlowAnalyticsReportConstraints,
        )
        # end -- build request data (keep comment for code generation)

        # start -- send sync request (keep comment for code generation)
        return self._base_client.request(
            method="POST",
            path=f"/analytics/balance/v1/customer/{customer_id}",
            auth_names=["FinicityAppKey", "FinicityAppToken"],
            query_params=_query,
            json=_json,
            cast_to=models.ObbAnalyticsReportAck,
            request_options=request_options or default_request_options(),
        )
        # end -- send sync request (keep comment for code generation)


class AsyncCustomerClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        # register async resources (keep comment for code generation)
        self.fcra = AsyncFcraClient(base_client=self._base_client)

    # register async api methods (keep comment for code generation)
    async def create(
        self,
        *,
        data: params.BalanceAndCashFlowAnalyticsReportConstraints,
        customer_id: str,
        reference_number: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.ObbAnalyticsReportAck:
        """
        Balance Analytics for Business analyzes bank balances over time to report metrics and identify behavior that may indicate risk.

        Calculated metrics include:
        * Current/available account balances
        * Minimum/maximum/average account balances over the requested time
          period and broken down by month

        * Daily ending balance of accounts for each day in the requested time
          period

        * Propensity of the customer's account balances to increase week over
          week

        * Number of days in the requested time period ending with a negative
          balance


        This version of the API is intended for piloting and integration testing your application with the Balance Analytics product. It does not adhere to FCRA requirements, and should not be used for production/lending purposes. See _Generate Balance Analytics - FCRA_ for the FCRA compliant version of this API.

        A successful call to this API will generate analytics and store a report within Finicity. The report can be retrieved via _Get Balance Analytics Report_ (operation: _GetObbAnalyticsReport_).

        _Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)
        """
        # start -- build request data (keep comment for code generation)
        _query: QueryParams = {}
        if reference_number is not None:
            _query["reference-number"] = encode_param(reference_number, False)
        _json = to_encodable(
            item=data,
            dump_with=params._SerializerBalanceAndCashFlowAnalyticsReportConstraints,
        )
        # end -- build request data (keep comment for code generation)

        # start -- send async request (keep comment for code generation)
        return await self._base_client.request(
            method="POST",
            path=f"/analytics/balance/v1/customer/{customer_id}",
            auth_names=["FinicityAppKey", "FinicityAppToken"],
            query_params=_query,
            json=_json,
            cast_to=models.ObbAnalyticsReportAck,
            request_options=request_options or default_request_options(),
        )
        # end -- send async request (keep comment for code generation)
