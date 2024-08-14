"""File Generated by Sideko (sideko.dev)"""

from open_banking.core import (
    AsyncBaseClient,
    SyncBaseClient,
    default_request_options,
    RequestOptions,
)
import typing
from open_banking.types.aggregation.v3.customers.accounts.details import models


class DetailsClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        # register sync resources (keep comment for code generation)

    # register sync api methods (keep comment for code generation)
    def list(
        self,
        *,
        customer_id: str,
        account_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.PaymentInstructions:
        """
        Return the real account number and routing number details for an ACH payment along with the supported payment instruction details. If the RTP (Real Time Payment) value for “transferInEnabled” is true, then the account can receive RTPs. If the value for “transferOutEnabled” is true, then the account can send RTPs

        Note: this is a premium service, billable per every successful API call.

        _Supported account types_: "checking", "savings", "moneyMarket"

        _Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)
        """
        # start -- build request data (keep comment for code generation)
        # end -- build request data (keep comment for code generation)

        # start -- send sync request (keep comment for code generation)
        return self._base_client.request(
            method="GET",
            path=f"/aggregation/v3/customers/{customer_id}/accounts/{account_id}/details",
            auth_names=["FinicityAppKey", "FinicityAppToken"],
            cast_to=models.PaymentInstructions,
            request_options=request_options or default_request_options(),
        )
        # end -- send sync request (keep comment for code generation)


class AsyncDetailsClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        # register async resources (keep comment for code generation)

    # register async api methods (keep comment for code generation)
    async def list(
        self,
        *,
        customer_id: str,
        account_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.PaymentInstructions:
        """
        Return the real account number and routing number details for an ACH payment along with the supported payment instruction details. If the RTP (Real Time Payment) value for “transferInEnabled” is true, then the account can receive RTPs. If the value for “transferOutEnabled” is true, then the account can send RTPs

        Note: this is a premium service, billable per every successful API call.

        _Supported account types_: "checking", "savings", "moneyMarket"

        _Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)
        """
        # start -- build request data (keep comment for code generation)
        # end -- build request data (keep comment for code generation)

        # start -- send async request (keep comment for code generation)
        return await self._base_client.request(
            method="GET",
            path=f"/aggregation/v3/customers/{customer_id}/accounts/{account_id}/details",
            auth_names=["FinicityAppKey", "FinicityAppToken"],
            cast_to=models.PaymentInstructions,
            request_options=request_options or default_request_options(),
        )
        # end -- send async request (keep comment for code generation)
