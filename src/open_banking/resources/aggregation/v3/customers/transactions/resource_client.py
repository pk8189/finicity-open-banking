"""File Generated by Sideko (sideko.dev)"""

from open_banking.core import (
    AsyncBaseClient,
    SyncBaseClient,
    QueryParams,
    default_request_options,
    RequestOptions,
    encode_param,
)
import typing
from open_banking.types.aggregation.v3.customers.transactions import models


class TransactionsClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        # register sync resources (keep comment for code generation)

    # register sync api methods (keep comment for code generation)
    def list(
        self,
        *,
        customer_id: str,
        from_date: int,
        to_date: int,
        include_pending: typing.Optional[bool] = None,
        limit: typing.Optional[int] = None,
        sort: typing.Optional[str] = None,
        start: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Transactions:
        """
        Get all transactions available for this customer within the given date range, across all accounts. This service supports paging and sorting by `transactionDate` (or `postedDate` if no transaction date is provided), with a maximum of 1000 transactions per request.

        Standard consumer aggregation provides up to 180 days of transactions prior to the date each account was added to the Finicity system. To access older transactions, you must first call the service Load Historic Transactions for Account.

        There is no limit for the size of the window between `fromDate` and `toDate`, however, the maximum number of transactions returned on one page is 1000.

        _Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)
        """
        # start -- build request data (keep comment for code generation)
        _query: QueryParams = {}
        _query["fromDate"] = encode_param(from_date, False)
        _query["toDate"] = encode_param(to_date, False)
        if include_pending is not None:
            _query["includePending"] = encode_param(include_pending, False)
        if limit is not None:
            _query["limit"] = encode_param(limit, False)
        if sort is not None:
            _query["sort"] = encode_param(sort, False)
        if start is not None:
            _query["start"] = encode_param(start, False)
        # end -- build request data (keep comment for code generation)

        # start -- send sync request (keep comment for code generation)
        return self._base_client.request(
            method="GET",
            path=f"/aggregation/v3/customers/{customer_id}/transactions",
            auth_names=["FinicityAppKey", "FinicityAppToken"],
            query_params=_query,
            cast_to=models.Transactions,
            request_options=request_options or default_request_options(),
        )
        # end -- send sync request (keep comment for code generation)


class AsyncTransactionsClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        # register async resources (keep comment for code generation)

    # register async api methods (keep comment for code generation)
    async def list(
        self,
        *,
        customer_id: str,
        from_date: int,
        to_date: int,
        include_pending: typing.Optional[bool] = None,
        limit: typing.Optional[int] = None,
        sort: typing.Optional[str] = None,
        start: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Transactions:
        """
        Get all transactions available for this customer within the given date range, across all accounts. This service supports paging and sorting by `transactionDate` (or `postedDate` if no transaction date is provided), with a maximum of 1000 transactions per request.

        Standard consumer aggregation provides up to 180 days of transactions prior to the date each account was added to the Finicity system. To access older transactions, you must first call the service Load Historic Transactions for Account.

        There is no limit for the size of the window between `fromDate` and `toDate`, however, the maximum number of transactions returned on one page is 1000.

        _Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)
        """
        # start -- build request data (keep comment for code generation)
        _query: QueryParams = {}
        _query["fromDate"] = encode_param(from_date, False)
        _query["toDate"] = encode_param(to_date, False)
        if include_pending is not None:
            _query["includePending"] = encode_param(include_pending, False)
        if limit is not None:
            _query["limit"] = encode_param(limit, False)
        if sort is not None:
            _query["sort"] = encode_param(sort, False)
        if start is not None:
            _query["start"] = encode_param(start, False)
        # end -- build request data (keep comment for code generation)

        # start -- send async request (keep comment for code generation)
        return await self._base_client.request(
            method="GET",
            path=f"/aggregation/v3/customers/{customer_id}/transactions",
            auth_names=["FinicityAppKey", "FinicityAppToken"],
            query_params=_query,
            cast_to=models.Transactions,
            request_options=request_options or default_request_options(),
        )
        # end -- send async request (keep comment for code generation)
