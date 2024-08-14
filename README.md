
# Open Banking Python SDK

## Overview
OpenAPI specification for Finicity APIs.

Open Banking solutions in the US are provided by Finicity, a Mastercard
company.

## Initilization
Initialize either the synchronous or asynchronous client to authenticate

### Synchronous Client
```python
from open_banking import Client
from os import getenv

Client(finicity_app_key=getenv("API_KEY"), finicity_app_token=getenv("API_KEY"))
```

### Asynchronous Client
```python
from open_banking import AsyncClient
from os import getenv

AsyncClient(finicity_app_key=getenv("API_KEY"), finicity_app_token=getenv("API_KEY"))
```


### Delete Access to Customer by ID
> Delete access to a customer and all associated accounts.
> This will delete access to the customer and all their linked accounts. The customer data will no longer be accessible. Any customer data already collected will be retained in accordance with our enterprise data retention policy consistent with legal and business purposes. 
> ⚠️ Use this service carefully! It will not pause for confirmation before performing the operation!
> _Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

```python
client.aggregation.v1.customers.delete(customer_id="1005061234")
```

---

### Delete Access to Customer Account by ID
> This will delete access to a specific account only. If there are multiple permissioned accounts, then partners and their customers will have the flexibility to continue to access data from other connected accounts using the consented (Oauth) token for the customer.
> The customer data on that specific account will no longer be accessible. Any customer data already collected will be retained in accordance with our enterprise retention policy consistent with legal and business purposes. ​
> _Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

```python
client.aggregation.v1.customers.accounts.delete(
    customer_id="1005061234", account_id="5011648377"
)
```

---

### Disable TxPush Notifications
> Delete all TxPush subscriptions with their notifications for the given account. No more notifications will be sent for account or transaction events.
> 
> For additional details on this process, see [TxPush Listener Service](https://developer.mastercard.com/open-banking-us/documentation/products/manage/tx-push/#setting-up-the-txpush-listener-service).
> 
> _Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

```python
client.aggregation.v1.customers.accounts.txpush.delete(
    customer_id="1005061234", account_id="5011648377"
)
```

---

### Delete Access to Customer Accounts by Institution Login ID
> Delete access to all customer accounts for a given FI.​
> This will delete access to the underlying account(s) under a given Institution Login ID. The customer data will no longer be accessible. Any customer data already collected will be retained in accordance with our enterprise retention policy consistent with legal and business purposes.
> _Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

```python
client.aggregation.v1.customers.institution_logins.delete(
    customer_id="1005061234", institution_login_id="1007302745"
)
```

---

### Delete TxPush Subscription
> Delete a specific subscription to TxPush notifications for the given account. This could be individual deleting the account or transactions events. No more events will be sent for that specific subscription.
> 
> For additional details on this process, see [TxPush Listener Service](https://developer.mastercard.com/open-banking-us/documentation/products/manage/tx-push/#setting-up-the-txpush-listener-service).
> 
> _Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

```python
client.aggregation.v1.customers.subscriptions.delete(
    customer_id="1005061234", subscription_id=17554874
)
```

---

### Revoke Third Party Access
> Revoke access of third party partners

```python
client.aggregation.v1.partners.access_key.delete(
    consent_receipt_id="cr_4pfI3r1X8aOHrDDwrwC01NHFxOXlT1"
)
```

---

### Get Customers
> Find all customers enrolled by the current partner, where the search text is found in the customer's username or any combination of `firstName` and `lastName` fields. If no search text is provided, all customers will be returned.
> 
> _Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

```python
client.aggregation.v1.customers.list(
    limit=1, search="Search Value", start=1, type="active", username="customerusername1"
)
```

---

### Get Customer by ID
> Retrieve a customer by ID.
> 
> _Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

```python
client.aggregation.v1.customers.get(customer_id="1005061234")
```

---

### Get Customer Accounts
> Get all accounts owned by the given customer.
> 
> _Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

```python
client.aggregation.v1.customers.accounts.list(
    customer_id="1005061234", account_type="string", status="pending"
)
```

---

### Get Customer Accounts (Simple)
> This API is a lighter version of Get Customer Accounts, returning only basic information of all active customer accounts.
> 
> _Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

```python
client.aggregation.v1.customers.accounts.simple.list_1(customer_id="1005061234")
```

---

### Get Available Balance - Cached
> Retrieve the latest cached available and cleared account balances for a customer. Since we update and store balances throughout the day, this is the most accurate balance information available when a connection to a financial institution is unavailable or when a faster response is needed. Only deposit account types are supported: Checking, Savings, Money Market, and CD.
> 
> Note: this is a premium service, billable per every successful API call. Enrollment is required.
> 
> _Supported account types_: "checking", "savings", "moneyMarket", "cd"
> 
> _Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

```python
client.aggregation.v1.customers.accounts.available_balance.list(
    customer_id="1005061234", account_id="5011648377"
)
```

---

### Get Available Balance
> Retrieve the available and cleared account balances for a single account in real-time directly from a financial institution.  
> You can define an additional query parameter `balance_cache_interval` to specify the time interval of the last cached balance. This parameter is used by the server to determine whether the cached balance is still valid or if it needs to be refreshed.  
> 
> 
> Note: this is a premium service, billable per every successful API call.
> 
> _Supported account types_: "checking", "savings", "moneyMarket", "cd"
> 
> _Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

```python
client.aggregation.v1.customers.accounts.available_balance.live.list(
    customer_id="1005061234", account_id="5011648377", balance_cache_interval=1
)
```

---

### Get Account ACH Details
> Return the real account number and routing number details for an ACH payment.
> 
> Note: this is a premium service, billable per every successful API call.
> 
> _Supported account types_: "checking", "savings", "moneyMarket"
> 
> _Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

```python
client.aggregation.v1.customers.accounts.details.list(
    customer_id="1005061234", account_id="5011648377"
)
```

---

### Get Account Owner
> Retrieve the names and addresses of the account owner from a financial institution.
> 
> Note: this is a premium service, billable per every successful API call.
> 
> This service retrieves account data from the institution. This usually returns quickly, but in some scenarios may take a few minutes to complete. In the event of a timeout condition, retry the call.
> 
> _Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

```python
client.aggregation.v1.customers.accounts.owner.list(
    customer_id="1005061234", account_id="5011648377"
)
```

---

### Get Customer Account by ID (Simple)
> This API is a lighter version of Get Customer Accounts by ID, returning only basic information of a customer account.
> 
> _Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

```python
client.aggregation.v1.customers.accounts.simple.list_1(
    customer_id="1005061234", account_id="5011648377"
)
```

---

### Get Customer Account Statement
> Retrieve the customer's bank statements in PDF format. Up to 24 months of history is available depending on the financial institution. Since this is a premium service, charges incur per each successful statement retrieved.
> 
> For certified financial institutions, statements are available for the following account types:
> * Checking
> * Savings
> * Money market
> * CDs
> * Investments
> * Mortgage
> * Credit cards
> * Loans
> * Line of credit
> * Student Loans
> 
> Note: setting the timeout to 180 seconds is recommended to allow enough time for a response.
> 
> _Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

```python
client.aggregation.v1.customers.accounts.statement.list(
    customer_id="1005061234", account_id="5011648377", index=1, type="taxStatement"
)
```

---

### Get Customer With App Data by ID
> Retrieve a customer along with additional details about the OAuth application.
> 
> _Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

```python
client.aggregation.v1.customers.application.list(customer_id="1005061234")
```

---

### Get Asset by Customer and ID
> Retrieve a binary file for the given asset ID.
> 
> _Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

```python
client.aggregation.v1.customers.assets.get(
    customer_id="1005061234", asset_id="097545c5-1c2a-4f20-a5ef-77f0820344c9-2018601178"
)
```

---

### Get Customer Accounts by Institution Login ID
> Get all accounts associated with the given institution login. All accounts returned are accessible by a single set of credentials on a single institution.
> 
> _Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

```python
client.aggregation.v1.customers.institution_logins.accounts.list(
    customer_id="1005061234", institution_login_id="1007302745"
)
```

---

### Get Customer Accounts by Institution Login ID (Simple)
> This API is a lighter version of Get Customer Accounts by Institution Login ID, returning only basic information of all active accounts owned by the given customer at the given institution login ID.
> 
> _Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

```python
client.aggregation.v1.customers.institution_logins.accounts.simple.list(
    customer_id="1005061234", institution_login_id="1007302745"
)
```

---

### Get Customer Accounts by Institution ID
> Get all active accounts owned by the given customer at the given institution.
> 
> _Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

```python
client.aggregation.v1.customers.institutions.accounts.list(
    customer_id="1005061234", institution_id=4222
)
```

---

### Get Customer Accounts by Institution ID (Simple)
> This API is a lighter version of Get Customer Accounts by Institution ID, returning only basic information of active accounts owned by the given customer at the given institution.
> 
> _Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

```python
client.aggregation.v1.customers.institutions.accounts.simple.list(
    customer_id="1005061234", institution_id=4222
)
```

---

### Get Customer Account by ID
> Get a customer account by ID.
> 
> _Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

```python
client.aggregation.v2.customers.accounts.get(
    customer_id="1005061234", account_id="5011648377"
)
```

---

### Get Loan Payment Details
> Return the loan payment details of the customer for a loan-type account.
> 
> Note: this is a premium service, billable per every successful API call.
> 
> _Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

```python
client.aggregation.v2.customers.accounts.loan_details.list(
    customer_id="1005061234", account_id="5011648377"
)
```

---

### Get Customer Transaction by ID
> Get details for the given transaction.
> 
> _Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

```python
client.aggregation.v2.customers.transactions.get(
    customer_id="1005061234", transaction_id=21284820852
)
```

---

### Get App Registration Status
> Get the status of your application registration(s).
> 
> _Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

```python
client.aggregation.v2.partners.applications.list(
    app_name="Awesome Budget App",
    application_id="123456789",
    modified_date=1607450357,
    page=1,
    page_size=20,
    pre_app_id="2581",
    status="P",
    submitted_date=1607450357,
)
```

---

### Get Account ACH Details with RTP
> Return the real account number and routing number details for an ACH payment along with the supported payment instruction details. If the RTP (Real Time Payment) value for “transferInEnabled” is true, then the account can receive RTPs. If the value for “transferOutEnabled” is true, then the account can send RTPs  
> 
> Note: this is a premium service, billable per every successful API call.
> 
> _Supported account types_: "checking", "savings", "moneyMarket"
> 
> _Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

```python
client.aggregation.v3.customers.accounts.details.list(
    customer_id="1005061234", account_id="5011648377"
)
```

---

### Get Account Owner Details
> This service retrieves the account details for an account holder from an institution. The following data objects are available.
> 
> * Account holders
> 
> * Addresses
> 
> * Emails
> 
> * Phones
> 
> * Documentations
> 
> * Identity Insights
> 
> 
> Note: The data returned varies from institution to institution as not all of them make the same data available. This is a premium service, billable per each successful API call.
> 
> _Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

```python
client.aggregation.v3.customers.accounts.owner.list(
    customer_id="1005061234", account_id="5011648377", with_insights=True
)
```

---

### Get Customer Account Multiple Statements
> This endpoint retrieves account statements for a given customer. The maximum number of statements that can be returned is 24.
> 
> _Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

```python
client.aggregation.v3.customers.accounts.statement.list(
    customer_id="1005061234", account_id="5011648377", index="1,2,3,4,5,6"
)
```

---

### Get All Customer Transactions
> Get all transactions available for this customer within the given date range, across all accounts. This service supports paging and sorting by `transactionDate` (or `postedDate` if no transaction date is provided), with a maximum of 1000 transactions per request.
> 
> Standard consumer aggregation provides up to 180 days of transactions prior to the date each account was added to the Finicity system. To access older transactions, you must first call the service Load Historic Transactions for Account.
> 
> There is no limit for the size of the window between `fromDate` and `toDate`, however, the maximum number of transactions returned on one page is 1000.
> 
> _Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

```python
client.aggregation.v3.customers.transactions.list(
    customer_id="1005061234",
    from_date=1607450357,
    to_date=1607450357,
    include_pending=True,
    limit=1,
    sort="desc",
    start=1,
)
```

---

### Get Customer Account Transactions
> Get all transactions available for this customer account within the given date range. This service supports paging and sorting by `transactionDate` (or `postedDate` if no transaction date is provided), with a maximum of 1000 transactions per request.
> 
> Standard consumer aggregation provides up to 180 days of transactions prior to the date each account was added to the Finicity system. To access older transactions, you must first call the Cash Flow Verification service Load Historic Transactions for Account.
> 
> There is no limit for the size of the window between `fromDate` and `toDate`, however, the maximum number of transactions returned on one page is 1000.
> 
> _Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

```python
client.aggregation.v4.customers.accounts.transactions.list(
    customer_id="1005061234",
    account_id="5011648377",
    from_date=1607450357,
    to_date=1607450357,
    include_pending=True,
    limit=1,
    sort="desc",
    start=1,
)
```

---

### Get OBB Analytics Report
> Retrieve the report saved by _Generate Balance Analytics_, _Generate Cash Flow Analytics_, or _Generate Payment History_. Requires the report ID generated by the previous call.
> 
> Report data can either be retrieved as a JSON document or a PDF file.  To specify the format required, set the _Accept request header_ to either **application/json** or **application/pdf**. If neither is set, the report format will be returned as a JSON document.
> 
> _Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

```python
client.analytics.data.v1.get(obb_report_id="string")
```

---

### Get OBB Analytics Report - FCRA
> Retrieve the report saved by _Generate Balance Analytics - FCRA_, _Generate Cash Flow Analytics - FCRA_, or _Generate Payment History - FCRA_. Requires the report ID generated by the previous call.
> 
> Report data can either be retrieved as a JSON document or a PDF file.  To specify the format required, set the _Accept request header_ to either **application/json** or **application/pdf**. If neither is set, the report format will be returned as a JSON document.
> 
> *Note:* this is a premium service, billable per every successful API call for non-testing customers.
> 
> _Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

```python
client.analytics.data.v1.fcra.list(obb_report_id="string", purpose="string")
```

---

### Get applications details.
> This endpoint returns the status of the submitted application and provides additional details.
> 
> _Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

```python
client.applications.list(
    application_id="string",
    limit=20,
    name="string",
    pre_app_id=123,
    start=1,
    status="string",
)
```

---

### Get the application registration status with the financial institutions.
> The registration status of the approved application against the financial institutions.
> 
> _Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

```python
client.applications.institutions.list(
    application_id="string", institution_id=123, limit=25, start=1
)
```

---

### Get Business by ID
> Retrieve business details.
> 
> _Supported regions_: ![\U0001F1FA\U0001F1F8](https://flagcdn.com/20x15/us.png)

```python
client.business_services.businesses.get(business_id="1112")
```

---

### Get Business for Customer
> Retrieve business details associated with a specific customer. By providing the unique customer identifier, details about the associated business can be accessed.
> 
> _Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

```python
client.business_services.customers.businesses.list(customer_id="1005061234")
```

---

### Get Experience IDs
> Retrieve Connect experiences by application name. Optionally, filter the experiences by product codes.

```python
client.connect.experiences.list(app_name="string", product_code=["string"])
```

---

### Returns customer authorization details for the institution login identification.
> The endpoint provides customer authorization details like authorization start date, authorization end date against the requested institution login id
> 
> _Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

```python
client.customers.institution_logins.authorization_details.list(
    institution_login_id=7008461438
)
```

---

### Get Consumer by ID
> Get the details of a consumer record by consumer ID.
> 
> _Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

```python
client.decisioning.v1.consumers.get(consumer_id="0bf46322c167b562e6cbed9d40e19a4c")
```

---

### Get Portfolio by Consumer
> Return a portfolio of most recently generated reports for each report type for a given consumer. If there are multiple reports that were generated for a report type (VOA, VOI, etc.), only the most recently generated report for the type will be returned.
> 
> _Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

```python
client.decisioning.v1.consumers.portfolios.get(
    consumer_id="0bf46322c167b562e6cbed9d40e19a4c", portfolio_id="y4zsgccj4xpw-6-port"
)
```

---

### Get Reports by Consumer ID
> Get all reports that have been generated by previous calls to Generate Report services for the given consumer.
> 
> The `status` fields in the returned list contain "inProgress", "failure", or "success". If the status shows "inProgress", the client app should wait 20 seconds and then call this API again.
> 
> _Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

```python
client.decisioning.v1.consumers.reports.list(
    consumer_id="0bf46322c167b562e6cbed9d40e19a4c", purpose="31"
)
```

---

### Get Consumer For Customer
> Get the details of a consumer record by customer ID.
> 
> _Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

```python
client.decisioning.v1.customers.consumer.list(customer_id="1005061234")
```

---

### Get Portfolio by Customer
> Return a portfolio of most recently generated reports for each report type for the given customer. If there are multiple reports that were generated for a report type (VOA, VOI, etc.), only the most recently generated report for the type will be returned.
> 
> _Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)
> 

```python
client.decisioning.v1.customers.portfolios.get(
    customer_id="1005061234", portfolio_id="y4zsgccj4xpw-6-port"
)
```

---

### Get Reports by Customer ID
> Get all reports that have been generated by previous calls to Generate Report services for the given customer.
> 
> The `status` fields in the returned list contain "inProgress", "failure", or "success". If the status shows "inProgress", the client app should wait 20 seconds and then call this API again.
> 
> _Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

```python
client.decisioning.v1.customers.reports.list(customer_id="1005061234", purpose="31")
```

---

### Get Report by Consumer and ID
> Get a report that has been generated by a previous call to one of the Generate Report services.
> 
> The report's `status` field contains "inProgress", "failure", or "success". If the status shows "inProgress", the client app should wait 20 seconds and then call this API again.
> 
> Report data can either be retrieved as a JSON document or a PDF file.  To specify the format required, set the _Accept request header_ to either **application/json** or **application/pdf**. If neither is set, the report format will be returned as a JSON document.
> 
> _Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

```python
client.decisioning.v3.consumers.reports.get(
    consumer_id="0bf46322c167b562e6cbed9d40e19a4c",
    report_id="u4hstnnak45g",
    on_behalf_of="Some entity",
    purpose="31",
)
```

---

### Get Report by Customer and ID
> Get a report that has been generated by a previous call to one of the Generate Report services.
> 
> The report's `status` field contains "inProgress", "failure", or "success". If the status shows "inProgress", the client app should wait 20 seconds and then call this API again.
> 
> Report data can either be retrieved as a JSON document or a PDF file.  To specify the format required, set the _Accept request header_ to either **application/json** or **application/pdf**. If neither is set, the report format will be returned as a JSON document.
> 
> _Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

```python
client.decisioning.v3.customers.reports.get(
    customer_id="1005061234",
    report_id="u4hstnnak45g",
    on_behalf_of="Some entity",
    purpose="31",
)
```

---

### Get Certified Institutions
> Search for financial institutions by certified product.
> 
> _Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

```python
client.institution.v2.certified_institutions.list(
    limit=1, search="finbank", start=1, supported_countries=["us"], type="voa"
)
```

---

### Get Certified Institutions With RSSD
> Search for certified financial institutions w/RSSD.
> 
> _Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

```python
client.institution.v2.certified_institutions.rssd.list(
    limit=1, search="finbank", start=1, supported_countries=["us"], type="voa"
)
```

---

### Get Institutions
> Search for financial institutions.
> 
> _Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

```python
client.institution.v2.institutions.list(
    limit=1, search="finbank", start=1, supported_countries=["us"], type="voa"
)
```

---

### Get Institution by ID
> Get financial institution details by ID.
> 
> _Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

```python
client.institution.v2.institutions.get(institution_id=4222)
```

---

### Get Institution Branding by ID
> Return the branding information for a financial institution.
> 
> _Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

```python
client.institution.v2.institutions.branding.list(institution_id=4222)
```

---

### Get Micro Entries Details
> Fetch the micro entries details.
> `customerId` and `accountId` are the identifiers of the customer and account receiving the micro entries.
> 
>   _Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

```python
client.microentry.v1.customers.accounts.get(
    customer_id="1005061234", account_id="5011648377"
)
```

---

### Refresh Customer Accounts
> Refresh account and transaction data for all accounts associated with the  given `customerId` with a connection to the institution.
> 
> Client apps are not permitted to automate calls to the Refresh services. Active accounts are automatically refreshed by Finicity once per day. Because many financial institutions only post transactions once per day, calling Refresh services repeatedly is usually a waste of resources and is not recommended.
> 
> Apps may call Refresh services for a specific customer when there is a specific business case for the need of data that is up to date as of the moment. Please discuss with your account manager and systems engineer for further clarification.
> 
> The recommended timeout setting for this request is 120 seconds in order to receive a response. However, you can terminate the connection after making the call the operation will still complete. You will have to pull the account records to check for an updated aggregation attempt date to know when the refresh is complete.
> 
> Note: This service is not available for all Data Access Tiers.
> 
> _Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

```python
client.aggregation.v1.customers.accounts.create(customer_id="1005061234")
```

---

### Create TxPush Test Transaction
> Inject a transaction into the transaction list for a testing account. This allows an app to trigger TxPush notifications for the account in order to test the app's TxPush Listener service. This causes the platform to send one transaction event and one account event (showing that the account balance has changed). This service is only supported for testing accounts.
> 
> For additional details on this process, see [TxPush Listener Service](https://developer.mastercard.com/open-banking-us/documentation/products/manage/tx-push/#setting-up-the-txpush-listener-service).
> 
> _Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

```python
client.aggregation.v1.customers.accounts.transactions.create(
    customer_id="1005061234",
    account_id="5011648377",
    data={
        "amount": -4.25,
        "description": "a testing transaction description",
        "posted_date": 1607450357,
        "status": "pending",
        "transaction_date": 1607450357,
    },
)
```

---

### Load Historic Transactions for Customer Account
> Connect to the account's financial institution and load up to 24 months of historic transactions for the account. Length of history varies by institution.
> 
> This is a premium service. The billable event is a call to this service specifying a customer ID that has not been seen before by this service. (If this service is called multiple times with the same customer ID, to load transactions from multiple accounts, only one billable event has occurred.)
> 
> The recommended timeout setting for this request is 180 seconds in order to receive a response. However, you can terminate the connection after making the call the operation will still complete. You will have to pull the account records to check for an updated aggregation attempt date to know when the refresh is complete.
> 
> The date range sent to the institution is calculated from the account's `createdDate`. This means that calling this service a second time for the same account normally will not add any new transactions for the account. For this reason, a second call to this service for a known account ID will usually return immediately.
> 
> In a few specific scenarios, it may be desirable to force a second connection to the institution for a known account ID. Some examples are:
> 
> * The institution's policy has changed, making more transactions available
> * Finicity has now added a longer transaction history support for the institution
> * The first call encountered an error, and the resulting Aggregation Ticket has now been fixed by the Finicity Support Team
> 
> In these cases, the POST request can contain the parameter `force=true` in the request body to force the second connection.
> 
> _Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

```python
client.aggregation.v1.customers.accounts.transactions.historic.create(
    customer_id="1005061234", account_id="5011648377"
)
```

---

### Subscribe to TxPush Notifications
> Register a client app's TxPush Listener to receive TxPush notifications related to the given account.
> 
> Each call to this service will return two records, one with class account and one with class transaction. Account events are sent when values change in the account's fields (such as `balance` or `interestRate`). Transaction events are sent whenever a new transaction is posted for the account. For institutions that do not provide TxPush services, notifications are sent as soon as Finicity finds a new transaction or new account data through regular aggregation processes.
> 
> The listener's URL must be secure (HTTPS) for any real-world account. In addition, the client's TxPush Listener will need to be verified. HTTP and HTTPS connections are only allowed on the standard ports 80 (HTTP) and 443 (HTTPS). The use of other ports will result with the call failing.
> 
> For additional details on this process, see [TxPush Listener Service](https://developer.mastercard.com/open-banking-us/documentation/products/manage/tx-push/#setting-up-the-txpush-listener-service).
> 
> _Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

```python
client.aggregation.v1.customers.accounts.txpush.create(
    customer_id="1005061234",
    account_id="5011648377",
    data={"callback_url": "https://www.mydomain.com/txpush/listener"},
)
```

---

### Refresh Customer Accounts by Institution Login ID
> Refresh account and transaction data for all accounts associated with a given `institutionLoginId` with a connection to the institution.
> 
> Client apps are not permitted to automate calls to the Refresh services. Active accounts are automatically refreshed by Finicity once per day. Because many financial institutions only post transactions once per day, calling Refresh repeatedly is usually a waste of resources and is not recommended.
> 
> Apps may call Refresh services for a specific customer when there is a specific business case for the need of data that is up to date as of the moment. Please discuss with your account manager and systems engineer for further clarification.
> 
> The recommended timeout setting for this request is 120 seconds in order to receive a response. However, you can terminate the connection after making the call the operation will still complete. You will have to pull the account records to check for an updated aggregation attempt date to know when the refresh is complete.
> 
> Note: This service is not available for all Data Access Tiers.
> 
> _Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

```python
client.aggregation.v1.customers.institution_logins.accounts.create(
    customer_id="1005061234", institution_login_id="1007302745"
)
```

---

### Store Customer Pay Statement
> Upload pay statements for a customer.
> 
> _Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

```python
client.aggregation.v1.customers.pay_statements.create(
    customer_id="1005061234",
    data={"label": "lastPayPeriod", "statement": "VGhpcyBtdXN0IGJlIGFuIGltYWdl"},
)
```

---

### Generate Third Party Access Key
> Generate access key for third party partners.
> A partner can provide access to third party partners with this access key.

```python
client.aggregation.v1.partners.access_key.create(
    data={
        "customer_id": "1005061234",
        "partner_id": "1234583871234",
        "products": [
            {
                "access_period": {
                    "end_time": "2022-03-10T06:06:20.042584549Z",
                    "start_time": "2022-03-10T06:06:20.042584549Z",
                    "type": "timeframe",
                },
                "account_id": "5011648377",
                "max_calls": 200,
                "payor_id": "2445581559892",
                "product": "moneyTransferDetails",
            }
        ],
        "provenance": {
            "client_fingerprint": "LU9ZYxcDNQCwEmAxH52XFzaRiGMAAAAABclSKxW5S9P8pUMDV4fbpg",
            "ip_address": "8.8.8.8",
            "token_field": "P9YbR+srNVyQI35893d+BzPrhGMAAAAAuacVUt+3m4svbaFjVSbHEA==",
        },
        "third_party_partner_id": "1234583871234",
    }
)
```

---

### Register App
> Register a new application to access financial institutions using OAuth connections.
> 
> _Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

```python
client.aggregation.v1.partners.applications.create(
    data={
        "app_description": "The app that makes your budgeting experience awesome",
        "app_name": "Awesome Budget App",
        "app_url": "https://www.finicity.com/",
        "image": "PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiIHN0YW5kYWxvbmU9Im5vIj8+CjxzdmcgICAKICAgeG1sbnM6c3ZnPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIKICAgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIgogICB2ZXJzaW9uPSIxLjEiCiAgIHZpZXdCb3g9IjAgMCAwIDAiCiAgIGhlaWdodD0iMCIKICAgd2lkdGg9IjAiPgogICAgPGcvPgo8L3N2Zz4K",
        "owner_address_line1": "434 W Ascension Way",
        "owner_address_line2": "Suite #200",
        "owner_city": "Murray",
        "owner_country": "USA",
        "owner_name": "Finicity",
        "owner_postal_code": "84123",
        "owner_state": "UT",
    }
)
```

---

### Add Customer
> Enroll an active customer, which is the actual owner of one or more real-world accounts. This is a billable customer.
> 
> Active customers must use the "FinBank Billable" profiles for testing purposes.
> 
> _Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

```python
client.aggregation.v2.customers.active.create(
    data={
        "application_id": "123456789",
        "email_field": "myname@mycompany.com",
        "first_name": "John",
        "last_name": "Smith",
        "phone": "1-801-984-4200",
        "username": "customerusername1",
    }
)
```

---

### Add Testing Customer
> Enroll a testing customer (Test Drive accounts).
> 
> For using testing customers with FinBank OAuth, you must register a test application with your systems engineer or account manager. Then, use that testing `applicationId` when creating testing customers.
> 
> Testing Customers can access FinBank profiles (except "FinBank Billable" profiles), and cannot access live financial institutions.
> 
> _Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

```python
client.aggregation.v2.customers.testing.create(
    data={
        "application_id": "123456789",
        "email_field": "myname@mycompany.com",
        "first_name": "John",
        "last_name": "Smith",
        "phone": "1-801-984-4200",
        "username": "customerusername1",
    }
)
```

---

### Refresh Customer Accounts for Data Access Tiers
> Refresh account and transaction data for all accounts associated with the  given `customerId` with a connection to the institution.
> 
> Client apps are not permitted to automate calls to the Refresh services. Active accounts are automatically refreshed by Finicity once per day.
> Apps may call Refresh services for a specific customer when there is a specific business case for the need of data that is up to date as of the moment. Please discuss with your account manager and systems engineer for further clarification.
> 
> Note: This service will be used for Data Access Tiers ASD, AFD and ATD.
> 
> _Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

```python
client.aggregation.v2.customers.accounts.create(customer_id="1005061234")
```

---

### Refresh Customer Account by Institution Login ID for Data Access Tiers
> Refresh account and transaction data for all accounts associated with a given 'institutionLoginId` with a connection to the institution. Client apps are not permitted to automate calls to the Refresh services. Active accounts are automatically refreshed by Finicity once per day.
> 
> Apps may call Refresh services for a specific customer when there is a specific business case for the need of data that is up to date as of the moment. Please discuss with your account manager and systems engineer for further clarification.
> 
> Note: This service will be used for Data Access Tiers ASD, AFD and ATD.
> 
> _Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

```python
client.aggregation.v2.customers.institution_logins.accounts.create(
    customer_id="1005061234", institution_login_id="1007302745"
)
```

---

### Create Access Token
> Send Partner ID and Partner Secret to the Partner Authentication service to obtain a token for accessing Finicity APIs.
> * The token is valid for two hours and is required on all calls to the Finicity APIs
> * As a best practice, use a single token for all calls. Assign a timestamp for each token, and then check the current timestamp before making any calls. If the token is greater than 90 minutes, generate a new one.
> * ⚠️ After five failed attempts to authenticate, your account will be locked. To reset your account, you can report a support issue using the support.finicity.com portal. Alternatively, contact your Client Success Manager or your onboarding representative.
> 
> _Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

```python
client.aggregation.v2.partners.authentication.create(
    data={"partner_id": "1234583871234", "partner_secret": "aqJ5Ic4SEVx2IgDQ6oR4"}
)
```

---

### Generate Balance Analytics
> Balance Analytics for Business analyzes bank balances over time to report metrics and identify behavior that may indicate risk.
> 
> Calculated metrics include:
> * Current/available account balances
> * Minimum/maximum/average account balances over the requested time
>   period and broken down by month
> 
> * Daily ending balance of accounts for each day in the requested time
>   period
> 
> * Propensity of the customer's account balances to increase week over
>   week
> 
> * Number of days in the requested time period ending with a negative
>   balance
> 
> 
> This version of the API is intended for piloting and integration testing your application with the Balance Analytics product. It does not adhere to FCRA requirements, and should not be used for production/lending purposes. See _Generate Balance Analytics - FCRA_ for the FCRA compliant version of this API.
> 
> A successful call to this API will generate analytics and store a report within Finicity. The report can be retrieved via _Get Balance Analytics Report_ (operation: _GetObbAnalyticsReport_).
> 
> _Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

```python
client.analytics.balance.v1.customer.create(
    customer_id="1005061234",
    reference_number="abc123",
    data={"account_ids": [5011648377], "length_of_report": 730},
)
```

---

### Generate Balance Analytics - FCRA
> Balance Analytics for Business analyzes bank balances over time to report metrics and identify behavior that may indicate risk.
> 
> Calculated metrics include:
> * Current/available account balances
> * Minimum/maximum/average account balances over the requested time
>   period and broken down by month
> 
> * Daily ending balance of accounts for each day in the requested time
>   period
> 
> * Propensity of the customer's account balances to increase week over
>   week
> 
> * Number of days in the requested time period ending with a negative
>   balance
> 
> 
> This version of the API is intended for production use. It maintains and enforces all compliance with FCRA rules and requirements.
> 
> *Note:* this is a premium service, billable per every successful API call for non-testing customers.
> 
> A successful call to this API will generate analytics and store a report within Finicity. The report can be retrieved via _Get Balance Analytics Report - FCRA_ (operation: _GetObbAnalyticsReportFCRA_).
> 
> _Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

```python
client.analytics.balance.v1.customer.fcra.create(
    customer_id="1005061234",
    reference_number="abc123",
    data={"account_ids": [5011648377], "length_of_report": 730},
)
```

---

### Generate Cash Flow Analytics
> Cash Flow Analytics for Business analyzes cash flow over time to report metrics and identify behavior that may indicate risk.
> 
> Calculated metrics include:
> * Average transaction value by month over the requested time period
> * Net cash flow over the requested time period and broken down by month
> * Count and report of weeks in the requested time period where there
>   were zero transactions posted to the customer's accounts
> 
> * Minimum/maximum/average/sum/count of deposits by month
> * Minimum/maximum/average/sum/count of withdrawals by month
> * Estimated amount of deposits that can be classified as business
>   revenue
> 
> * Number of transactions posted incurring a non-sufficient funds (NSF)
>   fee, and net amount charged in NSF fees
> 
> 
> This version of the API is intended for piloting and integration testing your application with the Cash Flow Analytics product. It does not adhere to FCRA requirements, and should not be used for production/lending purposes. See _Generate Cash Flow Analytics - FCRA_ for the FCRA compliant version of this API.
> 
> A successful call to this API will generate analytics and store a report within Finicity. The report can be retrieved via _Get Cash Flow Analytics Report_ (operation: _GetCashFlowAnalyticsReport_).
> 
> _Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

```python
client.analytics.cashflow.v1.customer.create(
    customer_id="1005061234",
    reference_number="abc123",
    data={"account_ids": [5011648377], "length_of_report": 730},
)
```

---

### Generate Cash Flow Analytics - FCRA
> Cash Flow Analytics for Business analyzes cash flow over time to report metrics and identify behavior that may indicate risk.
> 
> Calculated metrics include:
> * Average transaction value by month over the requested time period
> * Net cash flow over the requested time period and broken down by month
> * Count and report of weeks in the requested time period where there
>   were zero transactions posted to the customer's accounts
> 
> * Minimum/maximum/average/sum/count of deposits by month
> * Minimum/maximum/average/sum/count of withdrawals by month
> * Estimated amount of deposits that can be classified as business
>   revenue
> 
> * Number of transactions posted incurring a non-sufficient funds (NSF)
>   fee, and net amount charged in NSF fees
> 
> 
> This version of the API is intended for production use. It maintains and enforces all compliance with FCRA rules and requirements.
> 
> *Note:* this is a premium service, billable per every successful API call for non-testing customers.
> 
> A successful call to this API will generate analytics and store a report within Finicity. The report can be retrieved via _Get Cash Flow Analytics Report - FCRA_ (operation: _GetCashFlowAnalyticsReportFCRA_).
> 
> _Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

```python
client.analytics.cashflow.v1.customer.fcra.create(
    customer_id="1005061234",
    reference_number="abc123",
    data={"account_ids": [5011648377], "length_of_report": 730},
)
```

---

### Generate Payment History
> Payment history report analyzes up to 12-months of transactions and predicts the probability that a SMB will experience a payment risk event, such as NSF/Overdraft or missed recurring payments, in the near future when making a payment. The Risk Score provided in the report is a 2-digit ranking with four levels of risk going from low to high.
> 
> Some of the highlights of calculated risk present in the report include:
> * Risk Score representing the likelihood of a missed payment
>   based on analysis of permissioned open-banking data
> 
> * Monthly average balance for all accounts by month in the requested
>   time period
> 
> * Total deposit amount by month for all accounts in the requested time
>   period
> 
> * Total withdrawal amounts by month for all accounts in the requested
>   time period
> 
> * Number of NSF counts and aggregate amount per month in the requested
>   time period
> 
> * Recurring loan payment amounts per month in the requested time period
> * Insurance payment amount per month in the requested time period
> * Tax payment amounts per month in the requested time period
> 
> This version of the API is intended for piloting and integration testing your application with the Payment History product. It does not adhere to FCRA requirements, and should not be used for production/lending purposes. See _Generate Payment History - FCRA_ for the FCRA compliant version of this API.
> 
> *Note:* this is a premium service, billable per every successful API call for non-testing customers.
> 
> A successful call to this API will generate analytics and store a report within Finicity. The report can be retrieved via _Get OBB Analytics Report_ (operation: _GetObbAnalyticsReport_).
> *Note:* this is a premium service, billable per every successful API call for non-testing customers.
> 
> _Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

```python
client.analytics.payment_history.v1.customer.create(
    customer_id="1005061234", reference_number="abc123"
)
```

---

### Generate Payment History - FCRA
> Payment history report analyzes up to 12-months of transactions and predicts the probability that a SMB will experience a payment risk event, such as NSF/Overdraft or missed recurring payments, in the near future when making a payment. The Risk Score provided in the report is a 2-digit ranking with four levels of risk going from low to high.
> 
> Some of the highlights of calculated risk present in the report include:
> * Risk Score representing the likelihood of a missed payment
>   based on analysis of permissioned open-banking data
> 
> * Monthly average balance for all accounts by month in the requested
>   time period
> 
> * Total deposit amount by month for all accounts in the requested time
>   period
> 
> * Total withdrawal amounts by month for all accounts in the requested
>   time period
> 
> * Number of NSF counts and aggregate amount per month in the requested
>   time period
> 
> * Recurring loan payment amounts per month in the requested time period
> * Insurance payment amount per month in the requested time period
> * Tax payment amounts per month in the requested time period
> 
> This version of the API is intended for production use. It maintains and
>  enforces all compliance with FCRA rules and requirements.
> 
> 
> *Note:* this is a premium service, billable per every successful API call for non-testing customers.
> 
> A successful call to this API will generate analytics and store a report within Finicity. The report can be retrieved via _Get OBB Analytics Report - FCRA_  (operation: _GetObbAnalyticsReportFcra_).
> 
> _Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

```python
client.analytics.payment_history.v1.customer.fcra.create(
    customer_id="1005061234", reference_number="abc123"
)
```

---

### Create a New Business for a Customer
> Create a new business record for the associated customer.
> A customer can have one business record associated.
> 
> _Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

```python
client.business_services.customers.businesses.create(
    customer_id="1005061234",
    data={
        "address": {
            "address_line1": "434 W Ascension Way",
            "address_line2": "Suite #200",
            "city": "Murray",
            "country": "US",
            "postal_code": "84123",
            "state": "UT",
        },
        "email_field": "myname@mycompany.com",
        "name": "ABC Tires Inc",
        "personally_liable": True,
        "phone_number": {"country_code": "1", "phone_no": "8042221111"},
        "tax_id": "A1234561Z",
        "type": "Nonprofit",
        "url": "https://www.finicity.com/",
    },
)
```

---

### Generate Connect URL
> Generate a Connect URL link to add within your own applications.
> 
> Optional Parameters:
> * `experience`: Configure different customer experiences per Connect session by changing the brand, color, logo, icon, the type of credit decisioning report to generate after the session ends, and more.
> * `language`: By default, the Connect application is in English. You don't need to pass  this parameter unless you want to translate Connect into one of our supported languages.
> 
>   * Spanish (United States)
>   * French (Canada)
> 
> 
> MVS Developers: You can pre-populate the consumer's SSN on the Find employment records page at the beginning of the MVS payroll app. Pass the SSN value for the consumer in the body of the request call.
> 
> _Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

```python
client.connect.v2.generate.create(
    data={
        "consumer_id": "0bf46322c167b562e6cbed9d40e19a4c",
        "customer_id": "1005061234",
        "experience": "default",
        "from_date": 1607450357,
        "institution_settings": {},
        "is_web_view": True,
        "language": "es",
        "optional_consumer_info": {"dob": 1607450357, "ssn": "999999999"},
        "partner_id": "1234583871234",
        "redirect_uri": "https://www.finicity.com/connect/",
        "report_custom_fields": [{"label": "loanID", "shown": True, "value": "123456"}],
        "single_use_url": True,
        "webhook": "https://webhook.site/8d4421a7-d1d1-4f01-bb08-5370aff0321b",
        "webhook_content_type": "application/json",
        "webhook_data": {},
        "webhook_headers": {},
    }
)
```

---

### Generate Fix Connect URL
> Use the Connect Fix API when the following conditions occur:
> * The connection to the user's financial institution is lost
> * The user's credentials were updated (for any number of reasons)
> * The user's MFA challenge has expired
> 
> _Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

```python
client.connect.v2.generate.fix.create(
    data={
        "customer_id": "1005061234",
        "experience": "default",
        "institution_login_id": "1007302745",
        "is_web_view": True,
        "language": "es",
        "partner_id": "1234583871234",
        "redirect_uri": "https://www.finicity.com/connect/",
        "single_use_url": True,
        "webhook": "https://webhook.site/8d4421a7-d1d1-4f01-bb08-5370aff0321b",
        "webhook_content_type": "application/json",
        "webhook_data": {},
        "webhook_headers": {},
    }
)
```

---

### Generate Connect URL - Joint Borrower
> Same as Connect Full (`POST /connect/v2/generate`) but for joint borrowers.
> 
> MVS prompts both the primary and joint borrower to enter each of their financial, payroll, and paystub information in the same Connect session.
> 
> _Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

```python
client.connect.v2.generate.joint_borrower.create(
    data={
        "borrowers": [
            {
                "consumer_id": "0bf46322c167b562e6cbed9d40e19a4c",
                "customer_id": "1005061234",
                "optional_consumer_info": {"dob": 1607450357, "ssn": "999999999"},
                "type": "primary",
            }
        ],
        "experience": "default",
        "from_date": 1607450357,
        "institution_settings": {},
        "language": "es",
        "partner_id": "1234583871234",
        "redirect_uri": "https://www.finicity.com/connect/",
        "report_custom_fields": [{"label": "loanID", "shown": True, "value": "123456"}],
        "single_use_url": True,
        "webhook": "https://webhook.site/8d4421a7-d1d1-4f01-bb08-5370aff0321b",
        "webhook_content_type": "application/json",
        "webhook_data": {},
        "webhook_headers": {},
    }
)
```

---

### Generate Lite Connect URL
> Connect Lite is a variation of Connect Full (`POST /connect/v2/generate`), which has a limited set of features.
> * Sign in, user's credentials, and Multi-Factor Authentication (MFA)
> * No user account management
> 
> The Connect Web SDK isn't a requirement when using Connect lite. However, if you want to use the SDK events, routes, and user events, then you must integrate with the Connect Web SDK.
> 
> _Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

```python
client.connect.v2.generate.lite.create(
    data={
        "customer_id": "1005061234",
        "experience": "default",
        "institution_id": 4222,
        "is_web_view": True,
        "language": "es",
        "partner_id": "1234583871234",
        "redirect_uri": "https://www.finicity.com/connect/",
        "single_use_url": True,
        "webhook": "https://webhook.site/8d4421a7-d1d1-4f01-bb08-5370aff0321b",
        "webhook_content_type": "application/json",
        "webhook_data": {},
        "webhook_headers": {},
    }
)
```

---

### Account Validation Assistant User verification of microdeposits
> The UI re-engages the consumer to enter two microdeposit amounts found in their account and validates them.
> 
> _Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

```python
client.connect.v2.generate.microentry.verify.create(
    data={
        "account_id": "5011648377",
        "customer_id": "1005061234",
        "experience": "default",
        "partner_id": "1234583871234",
        "redirect_uri": "https://www.finicity.com/connect/",
        "webhook": "https://webhook.site/8d4421a7-d1d1-4f01-bb08-5370aff0321b",
        "webhook_content_type": "application/json",
        "webhook_data": {},
        "webhook_headers": {},
    }
)
```

---

### Send Connect Email
> Same as Connect Full (`POST /connect/v2/generate`) but send a Connect email to a consumer.
> 
> _Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

```python
client.connect.v2.send.email_resource.create(
    data={
        "consumer_id": "0bf46322c167b562e6cbed9d40e19a4c",
        "customer_id": "1005061234",
        "email_field": {
            "first_name": "Bob",
            "from_field": "test.lender@test.com",
            "institution_address": "222 Winnipeg Drive SLC UT, 84109",
            "institution_name": "Acme Lending",
            "signature": [
                "Cindy Mayfield",
                "Senior Loan Officer",
                "Direct 123-456-7890",
            ],
            "subject": "Verify your income",
            "support_phone": "800-555-5555",
            "to": "bob@example.com",
        },
        "experience": "default",
        "from_date": 1607450357,
        "institution_settings": {},
        "language": "es",
        "optional_consumer_info": {"dob": 1607450357, "ssn": "999999999"},
        "partner_id": "1234583871234",
        "redirect_uri": "https://www.finicity.com/connect/",
        "report_custom_fields": [{"label": "loanID", "shown": True, "value": "123456"}],
        "single_use_url": True,
        "webhook": "https://webhook.site/8d4421a7-d1d1-4f01-bb08-5370aff0321b",
        "webhook_content_type": "application/json",
        "webhook_data": {},
        "webhook_headers": {},
    }
)
```

---

### Send Connect Email - Joint Borrower
> Same as Connect Joint Borrower (`POST /connect/v2/generate/jointBorrower`) but send a Connect email  to at least one of the joint borrower's email addresses.
> 
> When the consumer opens the email, MVS prompts both the primary and joint borrower to enter each of their financial, payroll, and paystub information in the same Connect session.
> 
> _Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

```python
client.connect.v2.send.email_resource.joint_borrower.create(
    data={
        "borrowers": [
            {
                "consumer_id": "0bf46322c167b562e6cbed9d40e19a4c",
                "customer_id": "1005061234",
                "optional_consumer_info": {"dob": 1607450357, "ssn": "999999999"},
                "type": "primary",
            }
        ],
        "email_field": {
            "first_name": "Bob",
            "from_field": "test.lender@test.com",
            "institution_address": "222 Winnipeg Drive SLC UT, 84109",
            "institution_name": "Acme Lending",
            "signature": [
                "Cindy Mayfield",
                "Senior Loan Officer",
                "Direct 123-456-7890",
            ],
            "subject": "Verify your income",
            "support_phone": "800-555-5555",
            "to": "bob@example.com",
        },
        "experience": "default",
        "from_date": 1607450357,
        "institution_settings": {},
        "language": "es",
        "partner_id": "1234583871234",
        "redirect_uri": "https://www.finicity.com/connect/",
        "report_custom_fields": [{"label": "loanID", "shown": True, "value": "123456"}],
        "single_use_url": True,
        "webhook": "https://webhook.site/8d4421a7-d1d1-4f01-bb08-5370aff0321b",
        "webhook_content_type": "application/json",
        "webhook_data": {},
        "webhook_headers": {},
    }
)
```

---

### Create Consumer
> Create a consumer record associated with the given customer. A consumer persists as the owner of any reports that are generated, even after the original customer is deleted from the system.
> 
> A consumer must be created for the given customer before calling any of the Generate Report services.
> 
> _Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

```python
client.decisioning.v1.customers.consumer.create(
    customer_id="1005061234",
    data={
        "address": "434 W Ascension Way Suite #200 Murray UT 84123",
        "birthday": {"day_of_month": 13, "month": 8, "year": 1989},
        "city": "Murray",
        "email_field": "myname@mycompany.com",
        "end_user": {
            "address": "434 W Ascension Way",
            "city": "Murray",
            "email_field": "myname@mycompany.com",
            "name": "John",
            "phone": "1-801-984-4200",
            "state": "UT",
            "url": "testurl.com",
            "zip": "84123",
        },
        "first_name": "John",
        "last_name": "Smith",
        "phone": "1-801-984-4200",
        "ssn": "999-99-9999",
        "state": "UT",
        "suffix": "PhD",
        "zip": "84123",
    },
)
```

---

### Generate Prequalification (Non-CRA) Report
> Retrieve all checking, savings, money market, and investment accounts for a customer. The account, owner information, and the number of insufficient funds (NSFs) for checking accounts are also provided.
> 
> If no account type of checking, savings, money market, or investment is found, the service will return HTTP 400 Bad Request.
> 
> _Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

```python
client.decisioning.v2.customers.asset_summary.create(
    customer_id="1005061234",
    callback_url="https://finicity-test/webhook",
    data={
        "account_ids": "1000535275",
        "from_date": 1580558400,
        "report_custom_fields": [
            {"label": "loanID", "shown": True, "value": "12345"},
            {"label": "trackingID", "shown": True, "value": "5555"},
            {"label": "loanType", "shown": False, "value": "car"},
            {"label": "vendorID", "shown": True, "value": "1613aa23"},
            {"label": "vendorName", "shown": False, "value": "PSC Finance"},
        ],
        "show_nsf": False,
    },
)
```

---

### Generate Cash Flow Report - Business
> Generate a Cash Flow Report (Business) report for all checking and savings under the given customer. This service retrieves up to two years of transaction history for the given account. It then uses this information to generate the CFR report. A consumer is not required to generate this report.
> 
> This report is not provided under FCRA rules, and this report is not available in the Finicity Consumer Portal for the borrower to view.
> 
> If no account type of checking or savings is found, the service will return HTTP 400 Bad Request.
> 
> _Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

```python
client.decisioning.v2.customers.cash_flow_business.create(
    customer_id="1005061234",
    callback_url="https://finicity-test/webhook",
    data={
        "account_ids": "1000535275",
        "from_date": 1580558400,
        "income_stream_confidence_minimum": 50,
        "report_custom_fields": [
            {"label": "loanID", "shown": True, "value": "12345"},
            {"label": "trackingID", "shown": True, "value": "5555"},
            {"label": "loanType", "shown": False, "value": "car"},
            {"label": "vendorID", "shown": True, "value": "1613aa23"},
            {"label": "vendorName", "shown": False, "value": "PSC Finance"},
        ],
        "show_nsf": False,
    },
)
```

---

### Generate Cash Flow Report - Personal
> Generate a Cash Flow Report (Personal) report for all checking and savings under the given customer. This service retrieves up to two years of transaction history for the given account. It then uses this information to generate the CFR report.
> 
> This report is provided under FCRA rules, with Finicity acting as the CRA (Consumer Reporting Agency). If an individual account is included in the report - for example, with an individual acting as an personal guarantor on the loan - then this version of the report should be used. In case of an adverse action on the loan where the decision was based on this report, then the borrower can be referred to the [Finicity Consumer Portal](https://consumer.finicityreports.com) where they can view this report and submit a dispute if they feel any information in this report is inaccurate.
> 
> Before calling this API, a consumer must be created for the given customer ID (see Consumers APIs).
> 
> If no account type of checking or savings is found, the service will return HTTP 400 Bad Request.
> 
> _Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

```python
client.decisioning.v2.customers.cash_flow_personal.create(
    customer_id="1005061234",
    callback_url="https://finicity-test/webhook",
    data={
        "account_ids": "1000535275",
        "from_date": 1580558400,
        "income_stream_confidence_minimum": 50,
        "report_custom_fields": [
            {"label": "loanID", "shown": True, "value": "12345"},
            {"label": "trackingID", "shown": True, "value": "5555"},
            {"label": "loanType", "shown": False, "value": "car"},
            {"label": "vendorID", "shown": True, "value": "1613aa23"},
            {"label": "vendorName", "shown": False, "value": "PSC Finance"},
        ],
        "show_nsf": False,
    },
)
```

---

### Generate Pay Statement Report
> Generate Pay Statement Extraction Report for the given customer. This service accepts asset IDs of the stored pay statements to generate a Pay Statement Extraction Report.
> 
> This is a premium service. The billing rate is the variable rate for Pay Statement Extraction Report under the current subscription plan. The billable event is the successful generation of a Pay Statement Extraction Report.
> 
> _Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

```python
client.decisioning.v2.customers.pay_statement.create(
    customer_id="1005061234",
    callback_url="https://finicity-test/webhook",
    data={
        "paystatement_report": {
            "asset_ids": ["6f8fb0a0-e882-4f57-b672-cf53f1397581"],
            "extract_deductions": False,
            "extract_direct_deposit": True,
            "extract_earnings": True,
        },
        "report_custom_fields": [
            {"label": "loanID", "shown": True, "value": "12345"},
            {"label": "trackingID", "shown": True, "value": "5555"},
            {"label": "loanType", "shown": False, "value": "car"},
            {"label": "vendorID", "shown": True, "value": "1613aa23"},
            {"label": "vendorName", "shown": False, "value": "PSC Finance"},
        ],
    },
)
```

---

### Generate Prequalification (CRA) Report
> Retrieve all checking, savings, money market, and investment accounts for a consumer. The account, owner information, and the number of insufficient funds (NSFs) for checking accounts are also provided.
> 
> If no account of type checking, savings, money market, or investment is found, the service will return HTTP 400 Bad Request.
> 
> _Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

```python
client.decisioning.v2.customers.pre_qual_voa.create(
    customer_id="1005061234",
    callback_url="https://finicity-test/webhook",
    data={
        "account_ids": "1000535275",
        "from_date": 1580558400,
        "report_custom_fields": [
            {"label": "loanID", "shown": True, "value": "12345"},
            {"label": "trackingID", "shown": True, "value": "5555"},
            {"label": "loanType", "shown": False, "value": "car"},
            {"label": "vendorID", "shown": True, "value": "1613aa23"},
            {"label": "vendorName", "shown": False, "value": "PSC Finance"},
        ],
        "show_nsf": False,
    },
)
```

---

### Generate Balance Analytics Report - Personal/Business
> Generate a Balance Analytics Report for a given customer. This service retrieves up to two years of transaction history from connected accounts.
> 
> Balance  Analytics analyzes bank balances over time to report metrics and identify behavior that may indicate risk.
> 
> Before calling this API, a consumer or business may need to be created for the given customer ID based on the user type (see Consumer/Business APIs).
> 
> If no account type of checking or savings is found, the service will return HTTP 400 Bad Request.
> 
> This is a premium service, billable per every successful API call for non-testing customers. A successful call to this API will generate analytics report which can be retrieved via Get Report by Customer or Get Report by Consumer.
> 
> _Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

```python
client.decisioning.v2.customers.reports.balance_analytics.user_types.create(
    customer_id="1005061234",
    user_type="business",
    callback_url="https://finicity-test/webhook",
    data={
        "account_ids": "1000535275 1000535276",
        "analytics_report_data": {
            "applicant_is_personal_guarantor": True,
            "for_cra_purpose": True,
            "time_interval_types": ["MONTHLY_CALENDAR"],
        },
        "from_date": 1580558400,
        "report_custom_fields": [
            {"label": "loanID", "shown": True, "value": "12345"},
            {"label": "trackingID", "shown": True, "value": "5555"},
            {"label": "loanType", "shown": False, "value": "car"},
            {"label": "vendorID", "shown": True, "value": "1613aa23"},
            {"label": "vendorName", "shown": False, "value": "PSC Finance"},
        ],
    },
)
```

---

### Generate Cashflow Analytics Report - Personal/Business
> Generate a Cashflow Analytics Report for a given customer. This service retrieves up to two years of transaction history from connected accounts.
> 
> Cashflow Analytics analyzes transaction over time to report metrics and identify behavior that may indicate risk.
> 
> Before calling this API, a consumer or business may need to be created for the given customer ID based on the user type (see Consumer/Business APIs).
> 
> If no account type of checking or savings is found, the service will return HTTP 400 Bad Request.
> 
> This is a premium service, billable per every successful API call for non-testing customers. A successful call to this API will generate analytics report which can be retrieved via Get Report by Customer or Get Report by Consumer.
> 
> _Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

```python
client.decisioning.v2.customers.reports.cashflow_analytics.user_types.create(
    customer_id="1005061234",
    user_type="business",
    callback_url="https://finicity-test/webhook",
    data={
        "account_ids": "1000535275 1000535276",
        "analytics_report_data": {
            "applicant_is_personal_guarantor": True,
            "for_cra_purpose": True,
            "time_interval_types": ["MONTHLY_CALENDAR"],
        },
        "from_date": 1580558400,
        "report_custom_fields": [
            {"label": "loanID", "shown": True, "value": "12345"},
            {"label": "trackingID", "shown": True, "value": "5555"},
            {"label": "loanType", "shown": False, "value": "car"},
            {"label": "vendorID", "shown": True, "value": "1613aa23"},
            {"label": "vendorName", "shown": False, "value": "PSC Finance"},
        ],
    },
)
```

---

### Generate Statement Report
> Generate a Statement Report for the given accounts under the given customer.
> 
> This is a premium service. A billable event will be created upon the successful generation of the Statement Report.
> 
> Before calling this API, a consumer must be created for the given customer ID (see Consumers APIs).
> 
> _Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

```python
client.decisioning.v2.customers.statement.create(
    customer_id="1005061234",
    callback_url="https://finicity-test/webhook",
    data={
        "report_custom_fields": [{"label": "loanID", "shown": True, "value": "123456"}],
        "statement_report_data": {"account_id": 1000076901, "statement_index": 1},
    },
)
```

---

### Generate Transactions Report
> Generate a Transaction Report for the given accounts under the given customer. This service retrieves up to 24 months of transaction history for the given customer. It then uses this information to generate the Transaction Report.
> 
> This is a premium service. A billable event will be created upon the successful generation of the Transactions Report.
> 
> Before calling this API, a consumer must be created for the given customer ID (see Consumers APIs).
> 
> There cannot be more than 24 months between `fromDate` and `toDate`.
> 
> _Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

```python
client.decisioning.v2.customers.transactions.create(
    customer_id="1005061234",
    to_date=1607450357,
    callback_url="https://finicity-test/webhook",
    include_pending=True,
    data={
        "account_ids": "1027339038 1027339039",
        "from_date": 1580558400,
        "report_custom_fields": [
            {"label": "loanID", "shown": True, "value": "12345"},
            {"label": "trackingID", "shown": True, "value": "5555"},
            {"label": "loanType", "shown": False, "value": "car"},
            {"label": "vendorID", "shown": True, "value": "1613aa23"},
            {"label": "vendorName", "shown": False, "value": "PSC Finance"},
        ],
    },
)
```

---

### Generate VOA Report
> Generate a Verification of Assets (VOA) report for all checking, savings, money market, and investment accounts for the given customer. This service retrieves up to twelve months of transaction history for each account and uses this information to generate the VOA report.
> 
> This is a premium service. The billing rate is the variable rate for Verification of Assets under the current subscription plan. The billable event is the successful generation of a VOA report.
> 
> Before calling this API, a consumer must be created for the given customer ID (see Consumers APIs).
> 
> If no account of type checking, savings, money market, or investment is found, the service will return HTTP 400 Bad Request.
> 
> _Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

```python
client.decisioning.v2.customers.voa.create(
    customer_id="1005061234",
    callback_url="https://finicity-test/webhook",
    data={
        "account_ids": "1000535275",
        "from_date": 1580558400,
        "report_custom_fields": [
            {"label": "loanID", "shown": True, "value": "12345"},
            {"label": "trackingID", "shown": True, "value": "5555"},
            {"label": "loanType", "shown": False, "value": "car"},
            {"label": "vendorID", "shown": True, "value": "1613aa23"},
            {"label": "vendorName", "shown": False, "value": "PSC Finance"},
        ],
        "show_nsf": False,
    },
)
```

---

### Generate VOA With Income Report
> Generate a Verification of Assets with Income (VOAI) report for all checking, savings, money market, and investment accounts for the given customer. This service retrieves up to 24 months of transaction history for each account and uses this information to generate the VOAI report. The report includes 1 - 6 months of all debit and credit transactions for asset verification. By default, the history is set to 61 days, however, you can change the transaction history in this section by setting the `fromDate` parameter. The report also includes up to 24 months of income credit transactions (ordered by account and confidence level) regardless of `fromDate` for income verification.
> 
> This is a premium service. The billable event is the successful generation of a VOAI report.
> 
> Before calling this API, a consumer must be created for the given customer ID (see Consumers APIs).
> 
> If no account of type checking, savings, money market, or investment is found, the service will return HTTP 400 Bad Request.
> 
> _Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

```python
client.decisioning.v2.customers.voa_history.create(
    customer_id="1005061234",
    callback_url="https://finicity-test/webhook",
    data={
        "account_ids": "1000535275",
        "from_date": 1580558400,
        "income_stream_confidence_minimum": 50,
        "report_custom_fields": [
            {"label": "loanID", "shown": True, "value": "12345"},
            {"label": "trackingID", "shown": True, "value": "5555"},
            {"label": "loanType", "shown": False, "value": "car"},
            {"label": "vendorID", "shown": True, "value": "1613aa23"},
            {"label": "vendorName", "shown": False, "value": "PSC Finance"},
        ],
        "show_nsf": False,
    },
)
```

---

### Generate VOE - Payroll Report
> Generate or refresh a VOE - Payroll report. Often used as a complementary report to the VOIE-Payroll report to fulfill the pre-close VOE requirements. It retrieves the customer's employment details and employment status through the payroll source without any income information.
> 
> This is a premium service. The billable event is the successful generation of a VOE - Payroll report.
> 
> _Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

```python
client.decisioning.v2.customers.voe_payroll.create(
    customer_id="1005061234",
    callback_url="https://finicity-test/webhook",
    data={
        "exclude_emp_info": False,
        "market_segment": "Mortgage",
        "pay_statements_from_date": 1580558400,
        "payroll_data": {
            "dob": "315576000",
            "report_id": "abcdefghijkl-voiepayroll",
            "ssn": "999990000",
        },
        "purpose": "31",
        "report_custom_fields": [{"label": "loanID", "shown": True, "value": "12345"}],
    },
)
```

---

### Generate VOE - Transactions Report
> Premium Service: A billable event when the API response is successful.
> 
> MVS-Direct integration developers only.
> 
> Used as a complimentary report to the VOA with Income and VOIE - Paystub (with TXVerify) reports and used to fulfill the pre-close VOE requirements.
> 
> Retrieve the latest credit transaction information from the borrower's connected bank accounts and groups them into income streams so that you can view their payment history to ensure a direct deport was made within the expected cadence. The report displays transaction descriptions without any dollar amounts so that income re-verification isn't necessary.
> 
> _Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

```python
client.decisioning.v2.customers.voe_transactions.create(
    customer_id="1005061234",
    callback_url="https://finicity-test/webhook",
    data={
        "account_ids": "123456789",
        "from_date": 1580558400,
        "income_stream_confidence_minimum": 50,
        "report_custom_fields": [
            {"label": "loanID", "shown": True, "value": "12345"},
            {"label": "trackingID", "shown": True, "value": "5555"},
            {"label": "loanType", "shown": False, "value": "car"},
            {"label": "vendorID", "shown": True, "value": "1613aa23"},
            {"label": "vendorName", "shown": False, "value": "PSC Finance"},
        ],
        "report_id": "j7k8qbgwsa7d-voietxverify",
    },
)
```

---

### Generate VOI Report
> Generate a Verification of Income (VOI) report for all checking, savings, and money market accounts for the given customer. This service retrieves up to two years of transaction history for each account and uses this information to generate the VOI report.
> 
> This is a premium service. The billing rate is the variable rate for Verification of Income under the current subscription plan. The billable event is the successful generation of a VOI report.
> 
> If no account of type checking, savings, or money market is found, the service will return HTTP 400 Bad Request.
> 
> _Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

```python
client.decisioning.v2.customers.voi.create(
    customer_id="1005061234",
    callback_url="https://finicity-test/webhook",
    data={
        "account_ids": "1000535275 1000535276",
        "from_date": 1577986990,
        "income_stream_confidence_minimum": 50,
        "report_custom_fields": [
            {"label": "loanID", "shown": True, "value": "12345"},
            {"label": "trackingID", "shown": True, "value": "5555"},
            {"label": "loanType", "shown": False, "value": "car"},
            {"label": "vendorID", "shown": True, "value": "1613aa23"},
            {"label": "vendorName", "shown": False, "value": "PSC Finance"},
        ],
    },
)
```

---

### Generate VOIE - Payroll Report
> Generate or refresh a VOIE - Payroll report. For clients using the product via a consumer permissioning experience via Connect, the original VOIE - Payroll report generates when the consumer completes the Connect experience, and this API is only used for future report refreshes without reengaging the consumer.
> 
> This is a premium service. The billable event is the successful generation of a VOIE - Payroll report.
> 
> _Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

```python
client.decisioning.v2.customers.voie_payroll.create(
    customer_id="1005061234",
    callback_url="https://finicity-test/webhook",
    data={
        "exclude_emp_info": False,
        "market_segment": "Mortgage",
        "pay_statements_from_date": 1580558400,
        "payroll_data": {
            "dob": "315576000",
            "report_id": "abcdefghijkl-voiepayroll",
            "ssn": "999990000",
        },
        "purpose": "31",
        "report_custom_fields": [{"label": "loanID", "shown": True, "value": "12345"}],
    },
)
```

---

### Generate VOIE - Paystub (with TXVerify) Report
> Generate a VOIE - Paystub (with TXVerify) report for all checking and savings under the given customer. This service retrieves up to two years of transaction history for the given accounts. It then uses this information as well as the provided paystub(s), which are passed into the request body as asset IDs (generated using the Store Customer Pay Statement API) to generate the VOIE - Paystub (with TXVerify) report.
> 
> Note: if you are using this API to refresh the bank transactions, use the same asset ID from the first report. A new paystub is not required unless the paystub is too old for underwriting requirements. Using the same asset ID that was on the original report and the previously extracted details will be used to speed up report generation response time.
> 
> This is a premium service. The billing rate is the variable rate for VOIE TXVerify under the current subscription plan. The billable event is the successful generation of a VOIE TXVerify Report.
> 
> _Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

```python
client.decisioning.v2.customers.voie_tx_verify.with_interview.create(
    customer_id="1005061234",
    callback_url="https://finicity-test/webhook",
    data={
        "account_ids": "1028361677",
        "from_date": 1607450357,
        "income_stream_confidence_minimum": 50,
        "report_custom_fields": [{"label": "loanID", "shown": True, "value": "123456"}],
        "voie_with_interview_data": {
            "extract_deductions": True,
            "extract_direct_deposit": True,
            "extract_earnings": True,
            "tx_verify_interview": [
                {
                    "accounts": ["5011648377", "5011648378", "5011648379"],
                    "asset_id": "7eb57060-6d98-4449-992d-4dd4490448f3-1236011097",
                }
            ],
        },
    },
)
```

---

### Generate VOIE - Paystub Report
> Generate a VOIE - Paystub report. This service uses the provided paystub(s), which are passed into the request body as asset IDs (generated using the Store Customer Pay Statement API) to generate the VOIE - Paystub report with digitized paystub details.
> 
> This is a premium service. The billing rate is the variable rate for VOIE - Paystub under the current subscription plan. The billable event is the successful generation of a VOIE - Paystub Report.
> 
> _Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

```python
client.decisioning.v2.customers.voie_tx_verify.with_statement.create(
    customer_id="1005061234",
    callback_url="https://finicity-test/webhook",
    data={
        "report_custom_fields": [
            {"label": "loanID", "shown": True, "value": "123456"},
            {"label": "trackingID", "shown": True, "value": "5555"},
        ],
        "voie_with_statement_data": {
            "asset_ids": ["d50ed92f-543b-431c-8286-c8b8f6556679"],
            "extract_deductions": True,
            "extract_direct_deposit": True,
            "extract_earnings": True,
        },
    },
)
```

---

### Initiate Micro Entries
> Initiate the micro entries to customer's account.
> 
> Two random micro amounts less than a dollar each will be deposited to provided customer's account.
> 
>   _Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

```python
client.microentry.v1.customers.create(
    customer_id="1005061234",
    data={
        "callback_url": "https://www.mydomain.com/listener",
        "institution_login_id": "1007302745",
        "receiver": {
            "account_number": "123456",
            "account_type": "personalChecking",
            "memo": "micro deposit transfer",
            "name": "Bob Smith",
            "routing_number": "123456789",
        },
    },
)
```

---

### Verify Micro Entries
> Verify the micro entries as received by customer in customer's account.
> Customer needs to verify the micro amounts received in customer's account. `customerId` and `accountId` are the identifiers of the customer and account  receiving the micro entries.
> 
>   _Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

```python
client.microentry.v1.customers.accounts.amounts.create(
    customer_id="1005061234", account_id="5011648377", data={"amounts": [0.12, 0.15]}
)
```

---

### Modify Customer by ID
> Modify an enrolled customer by ID.
> 
> You must specify either `firstName`, `lastName`, or both in the request.
> 
> _Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

```python
client.aggregation.v1.customers.put(
    customer_id="1005061234", data={"first_name": "John", "last_name": "Smith"}
)
```

---

### Set Customer App ID
> If you have multiple applications for a single client, and you want to register their applications to access financial institutions using OAuth connections, then use this API to assign applications to an existing customer.
> 
> _Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

```python
client.aggregation.v1.customers.applications.put(
    customer_id="1005061234", application_id="123456789"
)
```

---

### Update Third Party Access
> Update access for third party partners

```python
client.aggregation.v1.partners.access_key.put(
    consent_receipt_id="cr_4pfI3r1X8aOHrDDwrwC01NHFxOXlT1",
    data={
        "customer_id": "1005061234",
        "partner_id": "1234583871234",
        "products": [
            {
                "access_period": {
                    "end_time": "2022-03-10T06:06:20.042584549Z",
                    "start_time": "2022-03-10T06:06:20.042584549Z",
                    "type": "timeframe",
                },
                "account_id": "5011648377",
                "max_calls": 200,
                "payor_id": "2445581559892",
                "product": "moneyTransferDetails",
            }
        ],
        "provenance": {
            "client_fingerprint": "LU9ZYxcDNQCwEmAxH52XFzaRiGMAAAAABclSKxW5S9P8pUMDV4fbpg",
            "ip_address": "8.8.8.8",
            "token_field": "P9YbR+srNVyQI35893d+BzPrhGMAAAAAuacVUt+3m4svbaFjVSbHEA==",
        },
        "third_party_partner_id": "1234583871234",
    },
)
```

---

### Modify App Registration
> Update a registered application.
> 
> _Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

```python
client.aggregation.v1.partners.applications.put(
    pre_app_id="2581",
    data={
        "app_description": "The app that makes your budgeting experience awesome",
        "app_name": "Awesome Budget App",
        "app_url": "https://www.finicity.com/",
        "image": "PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiIHN0YW5kYWxvbmU9Im5vIj8+CjxzdmcgICAKICAgeG1sbnM6c3ZnPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIKICAgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIgogICB2ZXJzaW9uPSIxLjEiCiAgIHZpZXdCb3g9IjAgMCAwIDAiCiAgIGhlaWdodD0iMCIKICAgd2lkdGg9IjAiPgogICAgPGcvPgo8L3N2Zz4K",
        "owner_address_line1": "434 W Ascension Way",
        "owner_address_line2": "Suite #200",
        "owner_city": "Murray",
        "owner_country": "USA",
        "owner_name": "Finicity",
        "owner_postal_code": "84123",
        "owner_state": "UT",
    },
)
```

---

### Migrate Institution Login Accounts
> The `institutionLoginId` parameter uses Finicity's internal FI mapping to move accounts from the current FI legacy connection to the new OAuth FI connection.
> 
> This API returns a list of accounts for the given institution login ID.
> 
> _Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

```python
client.aggregation.v2.customers.institution_logins.migration.put(
    customer_id="1005061234", institution_login_id="1007302745"
)
```

---

### Modify Partner Secret
> Change the Partner Secret used to authenticate this partner.
> 
> The secret does not expire, but can be changed by calling this API. A valid Partner Secret may contain upper and lowercase characters, numbers, and the characters !, @, #, $, %, &, *, _, -, +. It must include at least one number and at least one letter, and its length should be between 12 and 255 characters.
> 
> _Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

```python
client.aggregation.v2.partners.authentication.put(data={})
```

---

### Update Business by ID
> Update the details of a business based on its unique identifier. By providing the specific business ID and the updated information in the request, modifications can be made to the business's profile.
> 
> _Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

```python
client.business_services.businesses.put(
    business_id="1112",
    data={
        "address": {
            "address_line1": "434 W Ascension Way",
            "address_line2": "Suite #200",
            "city": "Murray",
            "country": "US",
            "postal_code": "84123",
            "state": "UT",
        },
        "email_field": "myname@mycompany.com",
        "name": "ABC Tires Inc",
        "personally_liable": True,
        "phone_number": {"country_code": "1", "phone_no": "8042221111"},
        "tax_id": "A1234561Z",
        "type": "Nonprofit",
        "url": "https://www.finicity.com/",
    },
)
```

---

### Modify Consumer by ID
> Modify an existing consumer. All fields are required for a consumer record, but individual fields for this call are optional because fields that are not specified will be left unchanged.
> 
> _Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

```python
client.decisioning.v1.consumers.put(
    consumer_id="0bf46322c167b562e6cbed9d40e19a4c",
    data={
        "address": "434 W Ascension Way Suite #200 Murray UT 84123",
        "birthday": {"day_of_month": 13, "month": 8, "year": 1989},
        "city": "Murray",
        "email_field": "myname@mycompany.com",
        "end_user": {
            "address": "434 W Ascension Way",
            "city": "Murray",
            "email_field": "myname@mycompany.com",
            "name": "John",
            "phone": "1-801-984-4200",
            "state": "UT",
            "url": "testurl.com",
            "zip": "84123",
        },
        "first_name": "John",
        "last_name": "Smith",
        "phone": "1-801-984-4200",
        "ssn": "999-99-9999",
        "state": "UT",
        "suffix": "PhD",
        "zip": "84123",
    },
)
```


