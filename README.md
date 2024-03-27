<div align="left">

[![Visit Remote](./header.png)](https://remote.com)

# Remote<a id="remote"></a>

Talent is everywhere. Opportunity is not. Remote's mission is to create opportunity everywhere, empowering employers to find and hire the best talent, and enabling individuals to build financial and personal freedom. 

Remote is a Global HR Platform that helps companies hire, manage, and pay their entire team — and more effectively compete in the modern global economy through our comprehensive set of core solutions including, HRIS, payroll, international employment, contractor management, and more. 

Whether you're just starting your global journey, or looking to optimize your existing operations, sign up or book a demo - and see how Remote makes global HR simple.


</div>

## Table of Contents<a id="table-of-contents"></a>

<!-- toc -->

- [Requirements](#requirements)
- [Installation](#installation)
- [Getting Started](#getting-started)
- [Async](#async)
- [Raw HTTP Response](#raw-http-response)
- [Reference](#reference)
  * [`remote.benefits_country_summary.list_summary`](#remotebenefits_country_summarylist_summary)
  * [`remote.billing_documents.download_pdf`](#remotebilling_documentsdownload_pdf)
  * [`remote.billing_documents.list`](#remotebilling_documentslist)
  * [`remote.billing_documents.show_details`](#remotebilling_documentsshow_details)
  * [`remote.companies.create_new_company`](#remotecompaniescreate_new_company)
  * [Creating a company with only the required request body parameters](#creating-a-company-with-only-the-required-request-body-parameters)
  * [Accepting the Terms of Service](#accepting-the-terms-of-service)
  * [`remote.companies.list_all`](#remotecompanieslist_all)
  * [`remote.companies.show_company`](#remotecompaniesshow_company)
  * [`remote.companies.update_company`](#remotecompaniesupdate_company)
  * [Getting a company and its owner to `active` status](#getting-a-company-and-its-owner-to-active-status)
  * [`remote.companies.update_company_0`](#remotecompaniesupdate_company_0)
  * [Getting a company and its owner to `active` status](#getting-a-company-and-its-owner-to-active-status-1)
  * [`remote.company_department.create_new_department`](#remotecompany_departmentcreate_new_department)
  * [`remote.company_department.list`](#remotecompany_departmentlist)
  * [`remote.company_managers.create_invite`](#remotecompany_managerscreate_invite)
  * [`remote.company_managers.delete_user`](#remotecompany_managersdelete_user)
  * [`remote.company_managers.list_managers`](#remotecompany_managerslist_managers)
  * [`remote.company_managers.show_user`](#remotecompany_managersshow_user)
  * [`remote.contract_amendments.approve_amendment`](#remotecontract_amendmentsapprove_amendment)
  * [`remote.contract_amendments.check_automatability`](#remotecontract_amendmentscheck_automatability)
  * [`remote.contract_amendments.create_request`](#remotecontract_amendmentscreate_request)
  * [`remote.contract_amendments.get_form_schema`](#remotecontract_amendmentsget_form_schema)
  * [`remote.contract_amendments.list_requests`](#remotecontract_amendmentslist_requests)
  * [`remote.contract_amendments.show_single_request`](#remotecontract_amendmentsshow_single_request)
  * [`remote.cost_calculator.create_employment_estimation`](#remotecost_calculatorcreate_employment_estimation)
  * [`remote.cost_calculator.generate_estimation_pdf`](#remotecost_calculatorgenerate_estimation_pdf)
  * [`remote.cost_calculator.list_countries`](#remotecost_calculatorlist_countries)
  * [`remote.cost_calculator.show_region_fields`](#remotecost_calculatorshow_region_fields)
  * [`remote.countries.get_form_schema`](#remotecountriesget_form_schema)
  * [`remote.countries.list_alphabetically`](#remotecountrieslist_alphabetically)
  * [`remote.countries.list_holidays_by_year`](#remotecountrieslist_holidays_by_year)
  * [`remote.custom_fields.list_definitions`](#remotecustom_fieldslist_definitions)
  * [`remote.custom_fields.show_value`](#remotecustom_fieldsshow_value)
  * [`remote.employment_contracts.get_pending_changes`](#remoteemployment_contractsget_pending_changes)
  * [`remote.employments.complete_onboarding`](#remoteemploymentscomplete_onboarding)
  * [`remote.employments.create_employment`](#remoteemploymentscreate_employment)
  * [`remote.employments.get_employment_info`](#remoteemploymentsget_employment_info)
  * [`remote.employments.invite_start_enrollment`](#remoteemploymentsinvite_start_enrollment)
  * [`remote.employments.list_all`](#remoteemploymentslist_all)
  * [`remote.employments.update_data`](#remoteemploymentsupdate_data)
  * [`remote.employments.update_details`](#remoteemploymentsupdate_details)
  * [`remote.expenses.create_approved_expense`](#remoteexpensescreate_approved_expense)
  * [`remote.expenses.download_receipt`](#remoteexpensesdownload_receipt)
  * [`remote.expenses.download_receipt_by_id`](#remoteexpensesdownload_receipt_by_id)
  * [`remote.expenses.list_records`](#remoteexpenseslist_records)
  * [`remote.expenses.show_record`](#remoteexpensesshow_record)
  * [`remote.expenses.update_expense`](#remoteexpensesupdate_expense)
  * [`remote.expenses.update_record`](#remoteexpensesupdate_record)
  * [`remote.files.download_file`](#remotefilesdownload_file)
  * [`remote.files.upload_employment_file`](#remotefilesupload_employment_file)
  * [`remote.identity.get_token_info`](#remoteidentityget_token_info)
  * [`remote.incentives.create_incentive`](#remoteincentivescreate_incentive)
  * [`remote.incentives.list_all`](#remoteincentiveslist_all)
  * [`remote.incentives.remove_incentive`](#remoteincentivesremove_incentive)
  * [`remote.incentives.show_details`](#remoteincentivesshow_details)
  * [`remote.incentives.update_incentive`](#remoteincentivesupdate_incentive)
  * [`remote.incentives.update_incentive_0`](#remoteincentivesupdate_incentive_0)
  * [`remote.o_auth2.exchange_token`](#remoteo_auth2exchange_token)
  * [`remote.offboarding.create_request`](#remoteoffboardingcreate_request)
  * [`remote.offboarding.list_requests`](#remoteoffboardinglist_requests)
  * [`remote.offboarding.show_request`](#remoteoffboardingshow_request)
  * [`remote.payslips.download_pdf`](#remotepayslipsdownload_pdf)
  * [`remote.payslips.list_all`](#remotepayslipslist_all)
  * [`remote.payslips.show_payslip`](#remotepayslipsshow_payslip)
  * [`remote.recurring_incentives.create_monthly_incentive`](#remoterecurring_incentivescreate_monthly_incentive)
  * [`remote.recurring_incentives.delete_scheduled`](#remoterecurring_incentivesdelete_scheduled)
  * [`remote.recurring_incentives.list_incentives`](#remoterecurring_incentiveslist_incentives)
  * [`remote.resignation.download_letter`](#remoteresignationdownload_letter)
  * [`remote.sandbox.create_employment_without_validations`](#remotesandboxcreate_employment_without_validations)
  * [`remote.sandbox.employment_update`](#remotesandboxemployment_update)
  * [`remote.sandbox.trigger_webhook_callback`](#remotesandboxtrigger_webhook_callback)
  * [`remote.sandbox.update_employment_state`](#remotesandboxupdate_employment_state)
  * [`remote.time_off.get_record`](#remotetime_offget_record)
  * [`remote.time_off.list_records`](#remotetime_offlist_records)
  * [`remote.time_off.list_types`](#remotetime_offlist_types)
  * [`remote.time_off.record_create`](#remotetime_offrecord_create)
  * [`remote.time_off.update_record`](#remotetime_offupdate_record)
  * [`remote.time_off.update_record_0`](#remotetime_offupdate_record_0)
  * [`remote.time_off_balances.show_balance`](#remotetime_off_balancesshow_balance)
  * [`remote.webhook_callbacks.delete_callback`](#remotewebhook_callbacksdelete_callback)
  * [`remote.webhook_callbacks.register_callback`](#remotewebhook_callbacksregister_callback)

<!-- tocstop -->

## Requirements<a id="requirements"></a>

Python >=3.7

## Installation<a id="installation"></a>
<div align="center">
  <a href="https://konfigthis.com/sdk-sign-up?company=Remote&language=Python">
    <img src="https://raw.githubusercontent.com/konfig-dev/brand-assets/HEAD/cta-images/python-cta.png" width="70%">
  </a>
</div>

## Getting Started<a id="getting-started"></a>

```python
from pprint import pprint
from remote_python_sdk import Remote, ApiException

remote = Remote(

    client_id = 'YOUR_CLIENT_ID',
    client_secret = 'YOUR_CLIENT_SECRET',,

    client_id = 'YOUR_CLIENT_ID',
    client_secret = 'YOUR_CLIENT_SECRET',
)

try:
    # List Benefits Country Summary
    list_summary_response = remote.benefits_country_summary.list_summary()
    print(list_summary_response)
except ApiException as e:
    print("Exception when calling BenefitsCountrySummaryApi.list_summary: %s\n" % e)
    pprint(e.body)
    if e.status == 422:
    if e.status == 404:
        pprint(e.body["message"])
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```

## Async<a id="async"></a>

`async` support is available by prepending `a` to any method.

```python

import asyncio
from pprint import pprint
from remote_python_sdk import Remote, ApiException

remote = Remote(

    client_id = 'YOUR_CLIENT_ID',
    client_secret = 'YOUR_CLIENT_SECRET',,

    client_id = 'YOUR_CLIENT_ID',
    client_secret = 'YOUR_CLIENT_SECRET',
)

async def main():
    try:
        # List Benefits Country Summary
        list_summary_response = await remote.benefits_country_summary.alist_summary()
        print(list_summary_response)
    except ApiException as e:
        print("Exception when calling BenefitsCountrySummaryApi.list_summary: %s\n" % e)
        pprint(e.body)
        if e.status == 422:
        if e.status == 404:
            pprint(e.body["message"])
        pprint(e.headers)
        pprint(e.status)
        pprint(e.reason)
        pprint(e.round_trip_time)

asyncio.run(main())
```

## Raw HTTP Response<a id="raw-http-response"></a>

To access raw HTTP response values, use the `.raw` namespace.

```python
from pprint import pprint
from remote_python_sdk import Remote, ApiException

remote = Remote(

    client_id = 'YOUR_CLIENT_ID',
    client_secret = 'YOUR_CLIENT_SECRET',,

    client_id = 'YOUR_CLIENT_ID',
    client_secret = 'YOUR_CLIENT_SECRET',
)

try:
    # List Benefits Country Summary
    list_summary_response = remote.benefits_country_summary.raw.list_summary()
    pprint(list_summary_response.body)
    pprint(list_summary_response.body["data"])
    pprint(list_summary_response.headers)
    pprint(list_summary_response.status)
    pprint(list_summary_response.round_trip_time)
except ApiException as e:
    print("Exception when calling BenefitsCountrySummaryApi.list_summary: %s\n" % e)
    pprint(e.body)
    if e.status == 422:
    if e.status == 404:
        pprint(e.body["message"])
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```


## Reference<a id="reference"></a>
### `remote.benefits_country_summary.list_summary`<a id="remotebenefits_country_summarylist_summary"></a>

List benefits summary for each country with the number of enrolled employees.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_summary_response = remote.benefits_country_summary.list_summary()
```

#### 🔄 Return<a id="🔄-return"></a>

[`ListBenefitsCountrySummaryResponse`](./remote_python_sdk/pydantic/list_benefits_country_summary_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/benefits/country-summary` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `remote.billing_documents.download_pdf`<a id="remotebilling_documentsdownload_pdf"></a>

Downloads a billing document PDF

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
download_pdf_response = remote.billing_documents.download_pdf(
    billing_document_id="93t3j-billing-doc-id-9suej43",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### billing_document_id: `str`<a id="billing_document_id-str"></a>

The billing document's ID

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/billing-documents/{billing_document_id}/pdf` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `remote.billing_documents.list`<a id="remotebilling_documentslist"></a>

List billing documents for a company

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_response = remote.billing_documents.list(
    period="\"2023-01\"",
    page=1,
    page_size=30,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### period: `str`<a id="period-str"></a>

The month for the billing documents (in ISO-8601 format)

##### page: `int`<a id="page-int"></a>

Starts fetching records after the given page

##### page_size: `int`<a id="page_size-int"></a>

Change the amount of records returned per page, defaults to 20, limited to 100

#### 🔄 Return<a id="🔄-return"></a>

[`BillingDocumentsResponse`](./remote_python_sdk/pydantic/billing_documents_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/billing-documents` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `remote.billing_documents.show_details`<a id="remotebilling_documentsshow_details"></a>

Shows a billing document details.

Please contact api-support@remote.com to request access to this endpoint.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
show_details_response = remote.billing_documents.show_details(
    billing_document_id="93t3j-billing-doc-id-9suej43",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### billing_document_id: `str`<a id="billing_document_id-str"></a>

The billing document's ID

#### 🔄 Return<a id="🔄-return"></a>

[`BillingDocumentResponse`](./remote_python_sdk/pydantic/billing_document_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/billing-documents/{billing_document_id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `remote.companies.create_new_company`<a id="remotecompaniescreate_new_company"></a>

  Creates a new company.

  ### Creating a company with only the required request body parameters
  When you call this endpoint and omit all the optional parameters in the request body,
  the following resources get created upon a successful response:
  * A new company with status `pending`.
  * A company owner for the new company with status `initiated`.

  See the [update a company endpoint](https://gateway.remote.com/v1/docs/openapi.html) for
  more details on how to get your company and its owner to `active` status.

  If you'd like to create a company and its owner with `active` status in a single request,
  please provide the optional `address_details` parameter as well.

  ### Accepting the Terms of Service

  A required step for creating a company in Remote is to accept our Terms of Service (ToS).

  Company managers need to be aware of our Terms of Service and Privacy Policy,
  hence **it's the responsibility of our partners to advise and ensure company managers read
  and accept the ToS**. The terms have to be accepted only once, before creating a company,
  and the Remote API will collect the acceptance timestamp as its confirmation.

  To ensure users read the most recent version of Remote's Terms of Service, their **acceptance
  must be done within the last fifteen minutes prior the company creation action**.

  To retrieve this information, partners can provide an element with any text and a description
  explaining that by performing that action they are accepting Remote's Term of Service. For
  instance, the partner can add a checkbox or a "Create Remote Account" button followed by a
  description saying "By creating an account, you agree to
  [Remote's Terms of Service](https://remote.com/terms-of-service). Also see Remote's
  [Privacy Policy](https://remote.com/privacy-policy)".


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_new_company_response = remote.companies.create_new_company(
    company_owner_email="ceo@techvision.com",
    company_owner_name="Joe Smith",
    country_code="USA",
    desired_currency="USD",
    name="Tech Vision",
    terms_of_service_accepted_at="1970-01-01T00:00:00.00Z",
    address_details={},
    bank_account_details={},
    email_domain="string_example",
    external_id="00001111",
    phone_number="+11123123456",
    registration_number="string_example",
    tax_number="123456789",
    action="get_oauth_access_tokens,send_create_password_email",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_owner_email: `str`<a id="company_owner_email-str"></a>

The company owner email.  This value cannot be changed once set. 

##### company_owner_name: `str`<a id="company_owner_name-str"></a>

The company owner name.  This value cannot be changed from the Remote API once set. 

##### country_code: `str`<a id="country_code-str"></a>

3-letter country code of the country the company address is located in.  For a list of countries supported through the Remote API, make a call to the [list countries endpoint](https://gateway.remote.com/v1/docs/openapi.html). This endpoint will also include the 3-letter country codes you can use for this field. 

##### desired_currency: `str`<a id="desired_currency-str"></a>

Desired currency for invoicing and displaying converted salaries in Remote UI regardless of the employee's country.

##### name: `str`<a id="name-str"></a>

The company name

##### terms_of_service_accepted_at: `datetime`<a id="terms_of_service_accepted_at-datetime"></a>

Date and time the Terms of Service were accepted. To ensure users read the most recent version of Remote's Terms of Service, their action cannot have been done more than fifteen minutes ago. The UTC offset must be included in the ISO 8601 format: `YYYY-MM-DD HOURS:MINUTES:SECONDSZ`

##### address_details: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="address_details-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

Fields can vary depending on the country. Please, check the required fields structure using the [Show form schema endpoint](https://gateway.remote.com/v1/docs/openapi.html). Use the desired country and `address_details` as the form name for the placeholders. The response complies with the [JSON Schema](https://remote.com/resources/api/how-json-schemas-work) specification. 

##### bank_account_details: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="bank_account_details-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

Fields can vary depending on the country. Please, check the required fields structure using the [Show form schema endpoint](https://gateway.remote.com/v1/docs/openapi.html). Use the desired country and `bank_account_details` as the form name for the placeholders. The response complies with the [JSON Schema](https://remote.com/resources/api/how-json-schemas-work) specification. 

##### email_domain: `str`<a id="email_domain-str"></a>

The domain of the company. Use this field to specify the company domain name when it's different from the domain in the company owner's email.

##### external_id: `str`<a id="external_id-str"></a>

Id of the company as represented in the external partner system.

##### phone_number: `str`<a id="phone_number-str"></a>

A phone number the company can be contacted with.

##### registration_number: `str`<a id="registration_number-str"></a>

The company registration number. This field or `tax_number` (but not both) should be submitted.

##### tax_number: `str`<a id="tax_number-str"></a>

The tax identifier of the company. This field or `registration_number` (but not both) should be submitted.

##### action: `str`<a id="action-str"></a>

Complementary action(s) to perform when creating a company:  - `get_oauth_access_tokens` returns the user's access and refresh tokens - `send_create_password_email ` sends a reset password token to the company owner's email so they can log in using Remote UI (not needed if integration plans to use SSO only)  If `action` contains `send_create_password_email` you can redirect the user to [https://employ.remote.com/api-integration-new-password-send](https://employ.remote.com/api-integration-new-password-send) 

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CreateCompanyParams`](./remote_python_sdk/type/create_company_params.py)
Create Company params

#### 🔄 Return<a id="🔄-return"></a>

[`CompanyCreationResponse`](./remote_python_sdk/pydantic/company_creation_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/companies` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `remote.companies.list_all`<a id="remotecompanieslist_all"></a>

List all companies that authorized your integration to act on their behalf. In other words, these are all the companies that your integration can manage. Any company that has completed the authorization flow for your integration will be included in the response.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_all_response = remote.companies.list_all()
```

#### 🔄 Return<a id="🔄-return"></a>

[`CompaniesResponse`](./remote_python_sdk/pydantic/companies_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/companies` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `remote.companies.show_company`<a id="remotecompaniesshow_company"></a>

Given an ID, shows a company

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
show_company_response = remote.companies.show_company(
    company_id="0a8s2d1-company-id-2e3f4th",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_id: `str`<a id="company_id-str"></a>

Company ID

#### 🔄 Return<a id="🔄-return"></a>

[`CompanyResponse`](./remote_python_sdk/pydantic/company_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/companies/{company_id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `remote.companies.update_company`<a id="remotecompaniesupdate_company"></a>

Given an ID and a request object with new information, updates a company.

### Getting a company and its owner to `active` status<a id="getting-a-company-and-its-owner-to-active-status"></a>
If you created a company using the
[create a company endpoint](https://gateway.remote.com/v1/docs/openapi.html) without all the required
request body parameters, you can use this endpoint to provide the missing data. Once the company
and its owner have all the necessary data, both their statuses will be set to `active` and the company
onboarding will be marked as "completed".

The following constitutes a company with "all the necessary data":
* Complete `address`, with valid `address`, `postal_code`, `country` and `state` parameters (Varies by country. Use the
[show form schema endpoint](https://gateway.remote.com/v1/docs/openapi.html) to see which address parameters
are required).
* Company `tax_number` or `registration_number` is not nil
* Company `name` is not nil (already required when creating the company)
* Company has a `desired_currency` in their bank account (already required when creating the company)
* Company has accepted terms of service (already required when creating the company)


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_company_response = remote.companies.update_company(
    company_id="0a8s2d1-company-id-2e3f4th",
    address_details={},
    bank_account_details={},
    country_code="USA",
    desired_currency="USD",
    name="Tech Vision",
    phone_number="+11123123456",
    registration_number="string_example",
    tax_number="123456789",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_id: `str`<a id="company_id-str"></a>

Company ID

##### address_details: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="address_details-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

Fields can vary depending on the country. Please, check the required fields structure using the [Show form schema endpoint](https://gateway.remote.com/v1/docs/openapi.html). Use the desired country and `address_details` as the form name for the placeholders. The response complies with the [JSON Schema](https://remote.com/resources/api/how-json-schemas-work) specification. 

##### bank_account_details: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="bank_account_details-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

Fields can vary depending on the country. Please, check the required fields structure using the [Show form schema endpoint](https://gateway.remote.com/v1/docs/openapi.html). Use the desired country and `bank_account_details` as the form name for the placeholders. The response complies with the [JSON Schema](https://remote.com/resources/api/how-json-schemas-work) specification. 

##### country_code: `str`<a id="country_code-str"></a>

Country of company address

##### desired_currency: `str`<a id="desired_currency-str"></a>

Desired currency for invoicing and displaying converted salaries in Remote UI regardless of the employee's country.  This field is only accepted if company is in status `pending`. Please contact Remote if you wish to update it. 

##### name: `str`<a id="name-str"></a>

This field is only accepted if company is in status `pending`. Please contact Remote if you wish to update it. 

##### phone_number: `str`<a id="phone_number-str"></a>

A phone number the company can be contacted with.

##### registration_number: `str`<a id="registration_number-str"></a>

The company registration number. This field or tax_number (but not both) should be submitted.  This field is only accepted if company is in status `pending`. 

##### tax_number: `str`<a id="tax_number-str"></a>

  The tax identifier of the company. This field or registration_number (but not both) should be submitted.    This field is only accepted if company is in status `pending`. 

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UpdateCompanyParams`](./remote_python_sdk/type/update_company_params.py)
Update Company params

#### 🔄 Return<a id="🔄-return"></a>

[`CompanyResponse`](./remote_python_sdk/pydantic/company_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/companies/{company_id}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `remote.companies.update_company_0`<a id="remotecompaniesupdate_company_0"></a>

Given an ID and a request object with new information, updates a company.

### Getting a company and its owner to `active` status<a id="getting-a-company-and-its-owner-to-active-status"></a>
If you created a company using the
[create a company endpoint](https://gateway.remote.com/v1/docs/openapi.html) without all the required
request body parameters, you can use this endpoint to provide the missing data. Once the company
and its owner have all the necessary data, both their statuses will be set to `active` and the company
onboarding will be marked as "completed".

The following constitutes a company with "all the necessary data":
* Complete `address`, with valid `address`, `postal_code`, `country` and `state` parameters (Varies by country. Use the
[show form schema endpoint](https://gateway.remote.com/v1/docs/openapi.html) to see which address parameters
are required).
* Company `tax_number` or `registration_number` is not nil
* Company `name` is not nil (already required when creating the company)
* Company has a `desired_currency` in their bank account (already required when creating the company)
* Company has accepted terms of service (already required when creating the company)


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_company_0_response = remote.companies.update_company_0(
    company_id="0a8s2d1-company-id-2e3f4th",
    address_details={},
    bank_account_details={},
    country_code="USA",
    desired_currency="USD",
    name="Tech Vision",
    phone_number="+11123123456",
    registration_number="string_example",
    tax_number="123456789",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_id: `str`<a id="company_id-str"></a>

Company ID

##### address_details: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="address_details-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

Fields can vary depending on the country. Please, check the required fields structure using the [Show form schema endpoint](https://gateway.remote.com/v1/docs/openapi.html). Use the desired country and `address_details` as the form name for the placeholders. The response complies with the [JSON Schema](https://remote.com/resources/api/how-json-schemas-work) specification. 

##### bank_account_details: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="bank_account_details-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

Fields can vary depending on the country. Please, check the required fields structure using the [Show form schema endpoint](https://gateway.remote.com/v1/docs/openapi.html). Use the desired country and `bank_account_details` as the form name for the placeholders. The response complies with the [JSON Schema](https://remote.com/resources/api/how-json-schemas-work) specification. 

##### country_code: `str`<a id="country_code-str"></a>

Country of company address

##### desired_currency: `str`<a id="desired_currency-str"></a>

Desired currency for invoicing and displaying converted salaries in Remote UI regardless of the employee's country.  This field is only accepted if company is in status `pending`. Please contact Remote if you wish to update it. 

##### name: `str`<a id="name-str"></a>

This field is only accepted if company is in status `pending`. Please contact Remote if you wish to update it. 

##### phone_number: `str`<a id="phone_number-str"></a>

A phone number the company can be contacted with.

##### registration_number: `str`<a id="registration_number-str"></a>

The company registration number. This field or tax_number (but not both) should be submitted.  This field is only accepted if company is in status `pending`. 

##### tax_number: `str`<a id="tax_number-str"></a>

  The tax identifier of the company. This field or registration_number (but not both) should be submitted.    This field is only accepted if company is in status `pending`. 

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UpdateCompanyParams`](./remote_python_sdk/type/update_company_params.py)
Update Company params

#### 🔄 Return<a id="🔄-return"></a>

[`CompanyResponse`](./remote_python_sdk/pydantic/company_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/companies/{company_id}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `remote.company_department.create_new_department`<a id="remotecompany_departmentcreate_new_department"></a>

Creates a new department in the specified company. Department names may be non-unique and must be non-empty with no more than 255 characters (Unicode code points).

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_new_department_response = remote.company_department.create_new_department(
    company_id="669f9e18-889f-4c2c-95b8-67795a3113cc",
    name="Marketing",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_id: `str`<a id="company_id-str"></a>

The Company ID. Required in all cases, whether the API credentials have access to multiple companies or just one.

##### name: `str`<a id="name-str"></a>

The name of the company department. May be non-unique and limited to 255 characters, maximum.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CreateCompanyDepartmentParams`](./remote_python_sdk/type/create_company_department_params.py)
Create Company Department request params

#### 🔄 Return<a id="🔄-return"></a>

[`CompanyDepartmentCreatedResponse`](./remote_python_sdk/pydantic/company_department_created_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/company-departments` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `remote.company_department.list`<a id="remotecompany_departmentlist"></a>

Lists all departments for the authorized company specified in the request.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_response = remote.company_department.list(
    company_id="d2091b1e-b1a4-437a-91ea-2809ffbb6d59",
    paginate=False,
    page=1,
    page_size=20,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_id: `str`<a id="company_id-str"></a>

Company ID

##### paginate: `bool`<a id="paginate-bool"></a>

Paginate option. Default: true. When true, paginates response; otherwise, does not.

##### page: `int`<a id="page-int"></a>

Starts fetching records after the given page

##### page_size: `int`<a id="page_size-int"></a>

Number of items per page

#### 🔄 Return<a id="🔄-return"></a>

[`ListCompanyDepartmentsPaginatedResponse`](./remote_python_sdk/pydantic/list_company_departments_paginated_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/company-departments` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `remote.company_managers.create_invite`<a id="remotecompany_managerscreate_invite"></a>

Create a Company Manager and sends the invitation email for signing in to the Remote Platform.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_invite_response = remote.company_managers.create_invite(
    email="string_example",
    name="string_example",
    role="string_example",
    company_id="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### email: `str`<a id="email-str"></a>

The work email of the company manager

##### name: `str`<a id="name-str"></a>

The name of the company manager

##### role: `str`<a id="role-str"></a>

The role assigned for the new manager. The value should be one of the following:  - `admin`: an Admin can manage most of the resources in remote. - `onboarding_manager`: an Onboarding Manager can add, see and manage new hires. - `people_manager`: a People Manager can view employee profiles of the team members they manage and approve and decline time off and expenses for their employees. 

##### company_id: `str`<a id="company_id-str"></a>

The Company ID. Required if the access token can access multiple companies. Optional otherwise.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CompanyManagerParams`](./remote_python_sdk/type/company_manager_params.py)
Company Manager params

#### 🔄 Return<a id="🔄-return"></a>

[`CompanyManagerData`](./remote_python_sdk/pydantic/company_manager_data.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/company-managers` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `remote.company_managers.delete_user`<a id="remotecompany_managersdelete_user"></a>

Deletes a Company Manager user

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
delete_user_response = remote.company_managers.delete_user(
    user_id="1a8s2d1-user-id-2e3f4tz",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### user_id: `str`<a id="user_id-str"></a>

User ID

#### 🔄 Return<a id="🔄-return"></a>

[`SuccessResponse`](./remote_python_sdk/pydantic/success_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/company-managers/{user_id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `remote.company_managers.list_managers`<a id="remotecompany_managerslist_managers"></a>

List all company managers of an integration. If filtered by the company_id param,
it lists only company managers belonging to the specified company.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_managers_response = remote.company_managers.list_managers(
    company_id="0a8s2d1-company-id-2e3f4th",
    page=1,
    page_size=30,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_id: `str`<a id="company_id-str"></a>

A Company ID to filter the results (only applicable for Integration Partners).

##### page: `int`<a id="page-int"></a>

Starts fetching records after the given page

##### page_size: `int`<a id="page_size-int"></a>

Change the amount of records returned per page, defaults to 20, limited to 100

#### 🔄 Return<a id="🔄-return"></a>

[`CompanyManagersResponse`](./remote_python_sdk/pydantic/company_managers_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/company-managers` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `remote.company_managers.show_user`<a id="remotecompany_managersshow_user"></a>

Shows a single company manager user

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
show_user_response = remote.company_managers.show_user(
    user_id="1a8s2d1-user-id-2e3f4tz",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### user_id: `str`<a id="user_id-str"></a>

User ID

#### 🔄 Return<a id="🔄-return"></a>

[`CompanyManagerResponse`](./remote_python_sdk/pydantic/company_manager_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/company-managers/{user_id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `remote.contract_amendments.approve_amendment`<a id="remotecontract_amendmentsapprove_amendment"></a>

Approves a contract amendment request without the intervention of a Remote admin.
Approvals done via this endpoint are effective immediately,
regardless of the effective date entered on the contract amendment creation.

This endpoint is only available in Sandbox, otherwise it will respond with a 404.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
approve_amendment_response = remote.contract_amendments.approve_amendment(
    contract_amendment_request_id="6d947344-b053-4a4f-acf0-79d296cbd082",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### contract_amendment_request_id: `str`<a id="contract_amendment_request_id-str"></a>

Contract amendment request ID

#### 🔄 Return<a id="🔄-return"></a>

[`ContractAmendmentResponse`](./remote_python_sdk/pydantic/contract_amendment_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/sandbox/contract-amendments/{contract_amendment_request_id}/approve` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `remote.contract_amendments.check_automatability`<a id="remotecontract_amendmentscheck_automatability"></a>

Check if a contract amendment request is automatable.
If the contract amendment request is automatable, then after submission, it will instantly amend the employee's contract
and send them an updated document.

This endpoint requires and returns country-specific data. The exact required and returned fields will
vary depending on which country the employment is in. To see the list of parameters for each country,
see the **Show form schema** endpoint under the [Contract Amendments](https://gateway.remote.com/v1/docs/openapi.html) category.

Please note that the compliance requirements for each country are subject to change according to local
laws. Given its continual updates, using Remote's [json-schema-form](https://remote.com/resources/api/how-json-schemas-work) should be considered in order to avoid
compliance issues and to have the latest version of a country requirements.

If you are using this endpoint to build an integration, make sure you are dynamically collecting or
displaying the latest parameters for each country by querying the _"Show form schema"_ endpoint.

For more information on JSON Schemas, see the **How JSON Schemas work** documentation.

To learn how you can dynamically generate forms to display in your UI, see the documentation for
the [json-schema-form](https://remote.com/resources/api/how-json-schemas-work) tool.



#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
check_automatability_response = remote.contract_amendments.check_automatability(
    amendment_contract_id="c15993d8-aa8a-4fbb-b395-8b7a54f57db1",
    contract_amendment={},
    employment_id="e31adae1-company-id-af5fba7dd803",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### amendment_contract_id: `str`<a id="amendment_contract_id-str"></a>

The contract ID of the contract that needs to be amended.

##### contract_amendment: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="contract_amendment-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

Contract amendment informations. As its properties may vary depending on the country,                 you must query the [Show form schema](https://gateway.remote.com/v1/docs/openapi.html) endpoint             passing the country code, `contract_amendment` and the employment ID as request body.

##### employment_id: `str`<a id="employment_id-str"></a>

The employment ID that is related to the contract amendment request.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CreateContractAmendmentParams`](./remote_python_sdk/type/create_contract_amendment_params.py)
Contract Amendment Params

#### 🔄 Return<a id="🔄-return"></a>

[`ContractAmendmentAutomatableResponse`](./remote_python_sdk/pydantic/contract_amendment_automatable_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/contract-amendments/automatable` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `remote.contract_amendments.create_request`<a id="remotecontract_amendmentscreate_request"></a>

Creates a Contract Amendment request.

This endpoint requires and returns country-specific data. The exact required and returned fields will
vary depending on which country the employment is in. To see the list of parameters for each country,
see the **Show form schema** endpoint under the [Contract Amendments](https://gateway.remote.com/v1/docs/openapi.html) category.

Please note that the compliance requirements for each country are subject to change according to local
laws. Given its continual updates, using Remote's [json-schema-form](https://remote.com/resources/api/how-json-schemas-work) should be considered in order to avoid
compliance issues and to have the latest version of a country requirements.

If you are using this endpoint to build an integration, make sure you are dynamically collecting or
displaying the latest parameters for each country by querying the _"Show form schema"_ endpoint.

For more information on JSON Schemas, see the **How JSON Schemas work** documentation.

To learn how you can dynamically generate forms to display in your UI, see the documentation for
the [json-schema-form](https://remote.com/resources/api/how-json-schemas-work) tool.



#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_request_response = remote.contract_amendments.create_request(
    amendment_contract_id="c15993d8-aa8a-4fbb-b395-8b7a54f57db1",
    contract_amendment={},
    employment_id="e31adae1-company-id-af5fba7dd803",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### amendment_contract_id: `str`<a id="amendment_contract_id-str"></a>

The contract ID of the contract that needs to be amended.

##### contract_amendment: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="contract_amendment-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

Contract amendment informations. As its properties may vary depending on the country,                 you must query the [Show form schema](https://gateway.remote.com/v1/docs/openapi.html) endpoint             passing the country code, `contract_amendment` and the employment ID as request body.

##### employment_id: `str`<a id="employment_id-str"></a>

The employment ID that is related to the contract amendment request.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CreateContractAmendmentParams`](./remote_python_sdk/type/create_contract_amendment_params.py)
Contract Amendment

#### 🔄 Return<a id="🔄-return"></a>

[`ContractAmendmentResponse`](./remote_python_sdk/pydantic/contract_amendment_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/contract-amendments` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `remote.contract_amendments.get_form_schema`<a id="remotecontract_amendmentsget_form_schema"></a>

Returns the json schema of the `contract_amendment` form.
This endpoint requires a company access token, as forms are dependent on certain
properties of companies and their current employments.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_form_schema_response = remote.contract_amendments.get_form_schema(
    country_code="string_example",
    employment_id="string_example",
    form="contract_amendment",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### country_code: `str`<a id="country_code-str"></a>

Country code according to ISO 3-digit alphabetic codes.

##### employment_id: `str`<a id="employment_id-str"></a>

The ID of the employment concerned by the contract amendment request.

##### form: `str`<a id="form-str"></a>

Name of the desired form

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ContractAmendmentSchemaParams`](./remote_python_sdk/type/contract_amendment_schema_params.py)
Contract Amendment Form

#### 🔄 Return<a id="🔄-return"></a>

[`ContractAmendmentFormResponse`](./remote_python_sdk/pydantic/contract_amendment_form_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/contract-amendments/schema` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `remote.contract_amendments.list_requests`<a id="remotecontract_amendmentslist_requests"></a>

List Contract Amendment requests.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_requests_response = remote.contract_amendments.list_requests()
```

#### 🔄 Return<a id="🔄-return"></a>

[`ListContractAmendmentResponse`](./remote_python_sdk/pydantic/list_contract_amendment_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/contract-amendments` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `remote.contract_amendments.show_single_request`<a id="remotecontract_amendmentsshow_single_request"></a>

Show a single Contract Amendment request.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
show_single_request_response = remote.contract_amendments.show_single_request(
    id="93t3j-contract_amendment_id-9suej43",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

Contract amendment request ID

#### 🔄 Return<a id="🔄-return"></a>

[`ContractAmendmentResponse`](./remote_python_sdk/pydantic/contract_amendment_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/contract-amendments/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `remote.cost_calculator.create_employment_estimation`<a id="remotecost_calculatorcreate_employment_estimation"></a>

Creates a cost estimation of employments

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_employment_estimation_response = remote.cost_calculator.create_employment_estimation(
    employer_currency_slug="663e0b79-c893-45ff-a1b2-f6dcabc098b5",
    employments=[
        {
            "employment_term": "fixed",
            "region_slug": "region_slug_example",
        }
    ],
    include_benefits=True,
    include_cost_breakdowns=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### employer_currency_slug: `str`<a id="employer_currency_slug-str"></a>

Currency Slug

##### employments: List[`CostCalculatorEmploymentParam`]<a id="employments-listcostcalculatoremploymentparam"></a>

##### include_benefits: `bool`<a id="include_benefits-bool"></a>

##### include_cost_breakdowns: `bool`<a id="include_cost_breakdowns-bool"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CostCalculatorEstimateParams`](./remote_python_sdk/type/cost_calculator_estimate_params.py)
Estimate params

#### 🔄 Return<a id="🔄-return"></a>

[`CostCalculatorEstimateResponse`](./remote_python_sdk/pydantic/cost_calculator_estimate_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/cost-calculator/estimation` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `remote.cost_calculator.generate_estimation_pdf`<a id="remotecost_calculatorgenerate_estimation_pdf"></a>

Creates a cost estimation of employments

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
generate_estimation_pdf_response = remote.cost_calculator.generate_estimation_pdf(
    employer_currency_slug="663e0b79-c893-45ff-a1b2-f6dcabc098b5",
    employments=[
        {
            "employment_term": "fixed",
            "region_slug": "region_slug_example",
        }
    ],
    include_benefits=True,
    include_cost_breakdowns=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### employer_currency_slug: `str`<a id="employer_currency_slug-str"></a>

Currency Slug

##### employments: List[`CostCalculatorEmploymentParam`]<a id="employments-listcostcalculatoremploymentparam"></a>

##### include_benefits: `bool`<a id="include_benefits-bool"></a>

##### include_cost_breakdowns: `bool`<a id="include_cost_breakdowns-bool"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CostCalculatorEstimateParams`](./remote_python_sdk/type/cost_calculator_estimate_params.py)
Estimate params

#### 🔄 Return<a id="🔄-return"></a>

[`CostCalculatorEstimatePDFResponse`](./remote_python_sdk/pydantic/cost_calculator_estimate_pdf_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/cost-calculator/estimation-pdf` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `remote.cost_calculator.list_countries`<a id="remotecost_calculatorlist_countries"></a>

Lists active and processing countries

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_countries_response = remote.cost_calculator.list_countries()
```

#### 🔄 Return<a id="🔄-return"></a>

[`CostCalculatorListCountryResponse`](./remote_python_sdk/pydantic/cost_calculator_list_country_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/cost-calculator/countries` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `remote.cost_calculator.show_region_fields`<a id="remotecost_calculatorshow_region_fields"></a>

Returns required fields JSON Schema for a given region. These are required in order to calculate
      the cost of employment for the region. These fields are based on employer contributions that are associated
      with the region or any of it's parent regions.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
show_region_fields_response = remote.cost_calculator.show_region_fields(
    slug="slug_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### slug: `str`<a id="slug-str"></a>

Slug

#### 🔄 Return<a id="🔄-return"></a>

[`JSONSchemaResponse`](./remote_python_sdk/pydantic/json_schema_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/cost-calculator/regions/{slug}/fields` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `remote.countries.get_form_schema`<a id="remotecountriesget_form_schema"></a>

Returns the json schema of a supported form. Possible form names are:
```
- address_details 
- administrative_details 
- bank_account_details 
- employment_basic_information 
- billing_address_details 
- contract_details 
- emergency_contact 
- employment_document_details 
- personal_details 
- pricing_plan_details 

```

This endpoint requires a company access token, as forms are dependent on certain
properties of companies and their current employments.



#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_form_schema_response = remote.countries.get_form_schema(
    country_code="PRT",
    form="address_details",
    employment_id="663e0b79-c893-45ff-a1b2-f6dcabc098b5",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### country_code: `str`<a id="country_code-str"></a>

Country code according to ISO 3-digit alphabetic codes

##### form: `str`<a id="form-str"></a>

Name of the desired form

##### employment_id: `str`<a id="employment_id-str"></a>

Required for `contract_amendment` form

#### 🔄 Return<a id="🔄-return"></a>

[`CountryFormResponse`](./remote_python_sdk/pydantic/country_form_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/countries/{country_code}/{form}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `remote.countries.list_alphabetically`<a id="remotecountrieslist_alphabetically"></a>

Returns a list of all countries that are supported by Remote API alphabetically ordered. The supported list accounts for creating employment with basic information and it does not imply fully onboarding employment via JSON Schema.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_alphabetically_response = remote.countries.list_alphabetically()
```

#### 🔄 Return<a id="🔄-return"></a>

[`CountriesResponse`](./remote_python_sdk/pydantic/countries_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/countries` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `remote.countries.list_holidays_by_year`<a id="remotecountrieslist_holidays_by_year"></a>

List all holidays of a country for a specific year. Optionally, it can be filtered by country subdivision.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_holidays_by_year_response = remote.countries.list_holidays_by_year(
    country_code="PRT",
    year="2022",
    country_subdivision_code="PT-10",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### country_code: `str`<a id="country_code-str"></a>

Country code according to ISO 3166-1 3-digit alphabetic codes

##### year: `str`<a id="year-str"></a>

Year for the holidays

##### country_subdivision_code: `str`<a id="country_subdivision_code-str"></a>

Country subdivision code according to ISO 3166-2 codes

#### 🔄 Return<a id="🔄-return"></a>

[`HolidaysResponse`](./remote_python_sdk/pydantic/holidays_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/countries/{country_code}/holidays/{year}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `remote.custom_fields.list_definitions`<a id="remotecustom_fieldslist_definitions"></a>

Returns custom fields definitions

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_definitions_response = remote.custom_fields.list_definitions(
    page=1,
    page_size=30,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### page: `int`<a id="page-int"></a>

Starts fetching records after the given page

##### page_size: `int`<a id="page_size-int"></a>

Change the amount of records returned per page, defaults to 20, limited to 100

#### 🔄 Return<a id="🔄-return"></a>

[`ListEmploymentCustomFieldsResponse`](./remote_python_sdk/pydantic/list_employment_custom_fields_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/custom-fields` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `remote.custom_fields.show_value`<a id="remotecustom_fieldsshow_value"></a>

Returns a custom field value for a given employment

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
show_value_response = remote.custom_fields.show_value(
    custom_field_id="custom_field_id_example",
    employment_id="employment_id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### custom_field_id: `str`<a id="custom_field_id-str"></a>

Custom field ID

##### employment_id: `str`<a id="employment_id-str"></a>

Employment ID

#### 🔄 Return<a id="🔄-return"></a>

[`EmploymentCustomFieldValueResponse`](./remote_python_sdk/pydantic/employment_custom_field_value_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/custom-fields/{custom_field_id}/values/{employment_id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `remote.employment_contracts.get_pending_changes`<a id="remoteemployment_contractsget_pending_changes"></a>

Get all the pending changes (waiting for aproval or signature) for the employment contract.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_pending_changes_response = remote.employment_contracts.get_pending_changes(
    employment_id="93t3j-employment_id-9suej43",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### employment_id: `str`<a id="employment_id-str"></a>

Employment ID

#### 🔄 Return<a id="🔄-return"></a>

[`EmploymentContractPendingChangesResponse`](./remote_python_sdk/pydantic/employment_contract_pending_changes_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/employment-contracts/{employment_id}/pending-changes` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `remote.employments.complete_onboarding`<a id="remoteemploymentscomplete_onboarding"></a>

Completes the employee onboarding. When all tasks are completed, the employee is marked as in `review` status

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
complete_onboarding_response = remote.employments.complete_onboarding(
    employment_id="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### employment_id: `str`<a id="employment_id-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CompleteOnboarding`](./remote_python_sdk/type/complete_onboarding.py)
Employment slug

#### 🔄 Return<a id="🔄-return"></a>

[`EmploymentResponse`](./remote_python_sdk/pydantic/employment_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/ready` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `remote.employments.create_employment`<a id="remoteemploymentscreate_employment"></a>

Creates an employment. We support creating employees and contractors.

This endpoint requires and returns country-specific data. The exact required and returned fields will
vary depending on which country the employment is in. To see the list of parameters for each country,
see the **Show form schema** endpoint under the [Countries](https://gateway.remote.com/v1/docs/openapi.html) category.

Please note that the compliance requirements for each country are subject to change according to local
laws. Given its continual updates, using Remote's [json-schema-form](https://remote.com/resources/api/how-json-schemas-work) should be considered in order to avoid
compliance issues and to have the latest version of a country requirements.

If you are using this endpoint to build an integration, make sure you are dynamically collecting or
displaying the latest parameters for each country by querying the _"Show form schema"_ endpoint.

For more information on JSON Schemas, see the **How JSON Schemas work** documentation.

To learn how you can dynamically generate forms to display in your UI, see the documentation for
the [json-schema-form](https://remote.com/resources/api/how-json-schemas-work) tool.



#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_employment_response = remote.employments.create_employment(
    country_code="string_example",
    full_name="string_example",
    job_title="string_example",
    personal_email="string_example",
    basic_information={},
    company_id="string_example",
    type="employee",
    provisional_start_date="Fri Jul 02 17:00:00 PDT 2021",
    seniority_date="2022-03-21",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### country_code: `str`<a id="country_code-str"></a>

##### full_name: `str`<a id="full_name-str"></a>

##### job_title: `str`<a id="job_title-str"></a>

##### personal_email: `str`<a id="personal_email-str"></a>

##### basic_information: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="basic_information-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

Employment basic information. When using this field, the same other root level fields (name, personal_email, job_title, provisional_start_date, and seniority_date) will be ignored. Its properties may vary depending on the country, you must query the [Show form schema](https://gateway.remote.com/v1/docs/openapi.html) endpoint passing the country code and `employment_basic_information` as path parameters. 

##### company_id: `str`<a id="company_id-str"></a>

This optional field is deprecated.

##### type: `str`<a id="type-str"></a>

If not provided, it will default to `employee`.

##### provisional_start_date: `date`<a id="provisional_start_date-date"></a>

Indicates the expected start date of the employee or contractor.  Required for employees, but optional for contractors. Date format is in ISO8601 without the time component.  See the **Date and Time Format** documentation for more details on how the Remote API works with dates. 

##### seniority_date: `datetime`<a id="seniority_date-datetime"></a>

The date the employee first started working for your company. If you don’t include a seniority date, the employee’s start date with Remote will be deemed as the start of the employee’s seniority.  **Example**: Your employee started working for your company on Feb 1, 2022. On Aug 1, 2022, you transferred the employee to Remote and started managing them on the platform. Feb 1, 2022 would be their seniority date. Aug 1, 2022 would be their starting date. 

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`EmploymentBasicParams`](./remote_python_sdk/type/employment_basic_params.py)
Employment params

#### 🔄 Return<a id="🔄-return"></a>

[`EmploymentCreationResponse`](./remote_python_sdk/pydantic/employment_creation_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/employments` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `remote.employments.get_employment_info`<a id="remoteemploymentsget_employment_info"></a>

Shows all the information of an employment.

This endpoint requires and returns country-specific data. The exact required and returned fields will
vary depending on which country the employment is in. To see the list of parameters for each country,
see the **Show form schema** endpoint under the [Countries](https://gateway.remote.com/v1/docs/openapi.html) category.

Please note that the compliance requirements for each country are subject to change according to local
laws. Given its continual updates, using Remote's [json-schema-form](https://remote.com/resources/api/how-json-schemas-work) should be considered in order to avoid
compliance issues and to have the latest version of a country requirements.

If you are using this endpoint to build an integration, make sure you are dynamically collecting or
displaying the latest parameters for each country by querying the _"Show form schema"_ endpoint.

For more information on JSON Schemas, see the **How JSON Schemas work** documentation.

To learn how you can dynamically generate forms to display in your UI, see the documentation for
the [json-schema-form](https://remote.com/resources/api/how-json-schemas-work) tool.



#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_employment_info_response = remote.employments.get_employment_info(
    employment_id="93t3j-employment-id-9suej43",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### employment_id: `str`<a id="employment_id-str"></a>

Employment ID

#### 🔄 Return<a id="🔄-return"></a>

[`EmploymentResponse`](./remote_python_sdk/pydantic/employment_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/employments/{employment_id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `remote.employments.invite_start_enrollment`<a id="remoteemploymentsinvite_start_enrollment"></a>

Invite an employment to start the self-enrollment.

Requirements for the invitation to succeed:

* Employment needs to have the following JSON Schema forms filled: `contract_details` and `pricing_plan_details`
* `provisional_start_date` must consider the minimum onbaording time of the employment's country

If there are validations errors, they are returned with a Conflict HTTP Status (409) and a descriptive message.
HTTP Status OK (200) is returned in case of success.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
invite_start_enrollment_response = remote.employments.invite_start_enrollment(
    employment_id="31b8e49b-aa1c-47af-849c-3d0a53e20e0d",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### employment_id: `str`<a id="employment_id-str"></a>

Employment ID

#### 🔄 Return<a id="🔄-return"></a>

[`SuccessResponse`](./remote_python_sdk/pydantic/success_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/employments/{employment_id}/invite` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `remote.employments.list_all`<a id="remoteemploymentslist_all"></a>

Lists all employments, except for the deleted ones.

This endpoint requires and returns country-specific data. The exact required and returned fields will
vary depending on which country the employment is in. To see the list of parameters for each country,
see the **Show form schema** endpoint under the [Countries](https://gateway.remote.com/v1/docs/openapi.html) category.

Please note that the compliance requirements for each country are subject to change according to local
laws. Given its continual updates, using Remote's [json-schema-form](https://remote.com/resources/api/how-json-schemas-work) should be considered in order to avoid
compliance issues and to have the latest version of a country requirements.

If you are using this endpoint to build an integration, make sure you are dynamically collecting or
displaying the latest parameters for each country by querying the _"Show form schema"_ endpoint.

For more information on JSON Schemas, see the **How JSON Schemas work** documentation.

To learn how you can dynamically generate forms to display in your UI, see the documentation for
the [json-schema-form](https://remote.com/resources/api/how-json-schemas-work) tool.



#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_all_response = remote.employments.list_all(
    company_id="93t3j-company-id-9suej43",
    email="anna@example.com",
    status="active",
    page=1,
    page_size=30,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_id: `str`<a id="company_id-str"></a>

Company ID

##### email: `str`<a id="email-str"></a>

Filters the results by employments whose login email matches the value

##### status: `str`<a id="status-str"></a>

Filters the results by employments whose status matches the value

##### page: `int`<a id="page-int"></a>

Starts fetching records after the given page

##### page_size: `int`<a id="page_size-int"></a>

Change the amount of records returned per page, defaults to 20, limited to 100

#### 🔄 Return<a id="🔄-return"></a>

[`ListEmploymentsResponse`](./remote_python_sdk/pydantic/list_employments_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/employments` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `remote.employments.update_data`<a id="remoteemploymentsupdate_data"></a>

Updates an employment.

**For `created` employments:** You can change all basic params and onboarding tasks or perform a per onboarding task update. You can also update basic_information.

**For `active` employments:** You can update the manager (`manager_id` field), emergency_contact_details and address_details.

This endpoint requires and returns country-specific data. The exact required and returned fields will
vary depending on which country the employment is in. To see the list of parameters for each country,
see the **Show form schema** endpoint under the [Countries](https://gateway.remote.com/v1/docs/openapi.html) category.

Please note that the compliance requirements for each country are subject to change according to local
laws. Given its continual updates, using Remote's [json-schema-form](https://remote.com/resources/api/how-json-schemas-work) should be considered in order to avoid
compliance issues and to have the latest version of a country requirements.

If you are using this endpoint to build an integration, make sure you are dynamically collecting or
displaying the latest parameters for each country by querying the _"Show form schema"_ endpoint.

For more information on JSON Schemas, see the **How JSON Schemas work** documentation.

To learn how you can dynamically generate forms to display in your UI, see the documentation for
the [json-schema-form](https://remote.com/resources/api/how-json-schemas-work) tool.


#### Automatically inviting an employee<a id="automatically-inviting-an-employee"></a>

When you submit the `contract_details` and `pricing_plan_details`, Remote should have all the required data to automatically
send an invite to the employee. You can tell if an automatic invite has been sent by looking at the `employment_lifecycle_stage`
field value. If its value is `employee_self_enrollment`, it means the employee has received an email to join the Remote platform
at their `personal_email`.

After an automatic invite is sent to an employee, **you will not be able to update employment data through the Remote API**.
After onboarding, only a limited set of employment data will be available for updates, such as `emergency_contact_details`.
If you want to provide additional information for an employment, please make sure to do so **before** the employee is invited.
We block updates to some employment data because employees need to agree to amendments in certain cases,
such as when there are changes to their contract_details.
Currently, these amendments can only be done through the Remote UI.

Please contact Remote if you need to update contractors via API since it's currently not supported.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_data_response = remote.employments.update_data(
    full_name="string_example",
    job_title="string_example",
    personal_email="string_example",
    employment_id="93t3j-employment-id-9suej43",
    address_details={},
    administrative_details={},
    bank_account_details={},
    billing_address_details={},
    company_id="string_example",
    contract_details={},
    country={
        "alpha_2_code": "PT",
        "code": "PRT",
        "name": "Portugal",
    },
    emergency_contact_details={},
    manager_id="string_example",
    personal_details={},
    pricing_plan_details={
        "frequency": "annually",
    },
    provisional_start_date="Fri Jul 02 17:00:00 PDT 2021",
    seniority_date="2022-03-21",
    basic_information={},
    department_id="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### full_name: `str`<a id="full_name-str"></a>

##### job_title: `str`<a id="job_title-str"></a>

##### personal_email: `str`<a id="personal_email-str"></a>

##### employment_id: `str`<a id="employment_id-str"></a>

Employment ID

##### address_details: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="address_details-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

Home address information. As its properties may vary depending on the country,                you must query the [Show form schema](https://gateway.remote.com/v1/docs/openapi.html) endpoint             passing the country code and `address_details` as path parameters.

##### administrative_details: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="administrative_details-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

Administrative information. As its properties may vary depending on the country,                you must query the [Show form schema](https://gateway.remote.com/v1/docs/openapi.html) endpoint             passing the country code and `administrative_details` as path parameters.

##### bank_account_details: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="bank_account_details-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

Bank account information. As its properties may vary depending on the country,                you must query the [Show form schema](https://gateway.remote.com/v1/docs/openapi.html) endpoint             passing the country code and `bank_account_details` as path parameters.

##### billing_address_details: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="billing_address_details-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

Billing address information. As its properties may vary depending on the country,                you must query the [Show form schema](https://gateway.remote.com/v1/docs/openapi.html) endpoint             passing the country code and `billing_address_details` as path parameters.

##### company_id: `str`<a id="company_id-str"></a>

##### contract_details: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="contract_details-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

Contract information. As its properties may vary depending on the country,                you must query the [Show form schema](https://gateway.remote.com/v1/docs/openapi.html) endpoint             passing the country code and `contract_details` as path parameters.

##### country: [`Country`](./remote_python_sdk/type/country.py)<a id="country-countryremote_python_sdktypecountrypy"></a>


##### emergency_contact_details: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="emergency_contact_details-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

Emergency contact information. As its properties may vary depending on the country,                you must query the [Show form schema](https://gateway.remote.com/v1/docs/openapi.html) endpoint             passing the country code and `emergency_contact_details` as path parameters.

##### manager_id: `str`<a id="manager_id-str"></a>

The user id of the manager, who should have an `admin`, `owner` or `people_manager` role. You can find these users by querying the [Company Managers endpoint](https://gateway.remote.com/v1/docs/openapi.html). **Update of this field is only available for active employments.** 

##### personal_details: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="personal_details-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

Personal details information. As its properties may vary depending on the country,                you must query the [Show form schema](https://gateway.remote.com/v1/docs/openapi.html) endpoint             passing the country code and `personal_details` as path parameters.

##### pricing_plan_details: [`PricingPlanDetails`](./remote_python_sdk/type/pricing_plan_details.py)<a id="pricing_plan_details-pricingplandetailsremote_python_sdktypepricing_plan_detailspy"></a>


##### provisional_start_date: `date`<a id="provisional_start_date-date"></a>

Indicates the expected start date of the employee or contractor.  Required for employees, but optional for contractors. Date format is in ISO8601 without the time component.  See the **Date and Time Format** documentation for more details on how the Remote API works with dates. 

##### seniority_date: `datetime`<a id="seniority_date-datetime"></a>

The date the employee first started working for your company. If you don’t include a seniority date, the employee’s start date with Remote will be deemed as the start of the employee’s seniority.  **Example**: Your employee started working for your company on Feb 1, 2022. On Aug 1, 2022, you transferred the employee to Remote and started managing them on the platform. Feb 1, 2022 would be their seniority date. Aug 1, 2022 would be their starting date. 

##### basic_information: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="basic_information-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

Employment basic information. As its properties may vary depending on the country,                you must query the [Show form schema](https://gateway.remote.com/v1/docs/openapi.html) endpoint             passing the country code and `employment_basic_information` as path parameters.

##### department_id: `str`<a id="department_id-str"></a>

The department of the employment. The department must belong to the same company as the employment. 

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`EmploymentFullParams`](./remote_python_sdk/type/employment_full_params.py)
Employment params

#### 🔄 Return<a id="🔄-return"></a>

[`EmploymentResponse`](./remote_python_sdk/pydantic/employment_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/employments/{employment_id}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `remote.employments.update_details`<a id="remoteemploymentsupdate_details"></a>

Updates an employment.

**For `created` employments:** You can change all basic params and onboarding tasks or perform a per onboarding task update. You can also update basic_information.

**For `active` employments:** You can update the manager (`manager_id` field), emergency_contact_details and address_details.

This endpoint requires and returns country-specific data. The exact required and returned fields will
vary depending on which country the employment is in. To see the list of parameters for each country,
see the **Show form schema** endpoint under the [Countries](https://gateway.remote.com/v1/docs/openapi.html) category.

Please note that the compliance requirements for each country are subject to change according to local
laws. Given its continual updates, using Remote's [json-schema-form](https://remote.com/resources/api/how-json-schemas-work) should be considered in order to avoid
compliance issues and to have the latest version of a country requirements.

If you are using this endpoint to build an integration, make sure you are dynamically collecting or
displaying the latest parameters for each country by querying the _"Show form schema"_ endpoint.

For more information on JSON Schemas, see the **How JSON Schemas work** documentation.

To learn how you can dynamically generate forms to display in your UI, see the documentation for
the [json-schema-form](https://remote.com/resources/api/how-json-schemas-work) tool.


#### Automatically inviting an employee<a id="automatically-inviting-an-employee"></a>

When you submit the `contract_details` and `pricing_plan_details`, Remote should have all the required data to automatically
send an invite to the employee. You can tell if an automatic invite has been sent by looking at the `employment_lifecycle_stage`
field value. If its value is `employee_self_enrollment`, it means the employee has received an email to join the Remote platform
at their `personal_email`.

After an automatic invite is sent to an employee, **you will not be able to update employment data through the Remote API**.
After onboarding, only a limited set of employment data will be available for updates, such as `emergency_contact_details`.
If you want to provide additional information for an employment, please make sure to do so **before** the employee is invited.
We block updates to some employment data because employees need to agree to amendments in certain cases,
such as when there are changes to their contract_details.
Currently, these amendments can only be done through the Remote UI.

Please contact Remote if you need to update contractors via API since it's currently not supported.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_details_response = remote.employments.update_details(
    full_name="string_example",
    job_title="string_example",
    personal_email="string_example",
    employment_id="93t3j-employment-id-9suej43",
    address_details={},
    administrative_details={},
    bank_account_details={},
    billing_address_details={},
    company_id="string_example",
    contract_details={},
    country={
        "alpha_2_code": "PT",
        "code": "PRT",
        "name": "Portugal",
    },
    emergency_contact_details={},
    manager_id="string_example",
    personal_details={},
    pricing_plan_details={
        "frequency": "annually",
    },
    provisional_start_date="Fri Jul 02 17:00:00 PDT 2021",
    seniority_date="2022-03-21",
    basic_information={},
    department_id="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### full_name: `str`<a id="full_name-str"></a>

##### job_title: `str`<a id="job_title-str"></a>

##### personal_email: `str`<a id="personal_email-str"></a>

##### employment_id: `str`<a id="employment_id-str"></a>

Employment ID

##### address_details: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="address_details-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

Home address information. As its properties may vary depending on the country,                you must query the [Show form schema](https://gateway.remote.com/v1/docs/openapi.html) endpoint             passing the country code and `address_details` as path parameters.

##### administrative_details: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="administrative_details-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

Administrative information. As its properties may vary depending on the country,                you must query the [Show form schema](https://gateway.remote.com/v1/docs/openapi.html) endpoint             passing the country code and `administrative_details` as path parameters.

##### bank_account_details: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="bank_account_details-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

Bank account information. As its properties may vary depending on the country,                you must query the [Show form schema](https://gateway.remote.com/v1/docs/openapi.html) endpoint             passing the country code and `bank_account_details` as path parameters.

##### billing_address_details: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="billing_address_details-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

Billing address information. As its properties may vary depending on the country,                you must query the [Show form schema](https://gateway.remote.com/v1/docs/openapi.html) endpoint             passing the country code and `billing_address_details` as path parameters.

##### company_id: `str`<a id="company_id-str"></a>

##### contract_details: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="contract_details-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

Contract information. As its properties may vary depending on the country,                you must query the [Show form schema](https://gateway.remote.com/v1/docs/openapi.html) endpoint             passing the country code and `contract_details` as path parameters.

##### country: [`Country`](./remote_python_sdk/type/country.py)<a id="country-countryremote_python_sdktypecountrypy"></a>


##### emergency_contact_details: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="emergency_contact_details-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

Emergency contact information. As its properties may vary depending on the country,                you must query the [Show form schema](https://gateway.remote.com/v1/docs/openapi.html) endpoint             passing the country code and `emergency_contact_details` as path parameters.

##### manager_id: `str`<a id="manager_id-str"></a>

The user id of the manager, who should have an `admin`, `owner` or `people_manager` role. You can find these users by querying the [Company Managers endpoint](https://gateway.remote.com/v1/docs/openapi.html). **Update of this field is only available for active employments.** 

##### personal_details: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="personal_details-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

Personal details information. As its properties may vary depending on the country,                you must query the [Show form schema](https://gateway.remote.com/v1/docs/openapi.html) endpoint             passing the country code and `personal_details` as path parameters.

##### pricing_plan_details: [`PricingPlanDetails`](./remote_python_sdk/type/pricing_plan_details.py)<a id="pricing_plan_details-pricingplandetailsremote_python_sdktypepricing_plan_detailspy"></a>


##### provisional_start_date: `date`<a id="provisional_start_date-date"></a>

Indicates the expected start date of the employee or contractor.  Required for employees, but optional for contractors. Date format is in ISO8601 without the time component.  See the **Date and Time Format** documentation for more details on how the Remote API works with dates. 

##### seniority_date: `datetime`<a id="seniority_date-datetime"></a>

The date the employee first started working for your company. If you don’t include a seniority date, the employee’s start date with Remote will be deemed as the start of the employee’s seniority.  **Example**: Your employee started working for your company on Feb 1, 2022. On Aug 1, 2022, you transferred the employee to Remote and started managing them on the platform. Feb 1, 2022 would be their seniority date. Aug 1, 2022 would be their starting date. 

##### basic_information: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="basic_information-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

Employment basic information. As its properties may vary depending on the country,                you must query the [Show form schema](https://gateway.remote.com/v1/docs/openapi.html) endpoint             passing the country code and `employment_basic_information` as path parameters.

##### department_id: `str`<a id="department_id-str"></a>

The department of the employment. The department must belong to the same company as the employment. 

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`EmploymentFullParams`](./remote_python_sdk/type/employment_full_params.py)
Employment params

#### 🔄 Return<a id="🔄-return"></a>

[`EmploymentResponse`](./remote_python_sdk/pydantic/employment_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/employments/{employment_id}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `remote.expenses.create_approved_expense`<a id="remoteexpensescreate_approved_expense"></a>

Creates an **approved** expense

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_approved_expense_response = remote.expenses.create_approved_expense(
    title="new keyboard",
    amount=8000,
    currency="EUR",
    employment_id="d4ebc714-4950-47a9-a464-28e1f1ab2a90",
    expense_date="2020-12-11",
    category="home_office",
    receipt={
        "content": "[B@3e3f1dc1",
        "name": "receipt.pdf",
    },
    receipts=[
        {
            "content": "[B@3e3f1dc1",
            "name": "receipt.pdf",
        }
    ],
    reviewed_at="1970-01-01",
    reviewer_id="14c14128-f5f4-475a-8ec0-6329b4832a61",
    tax_amount=0,
    timezone="Etc/UTC",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### title: `str`<a id="title-str"></a>

##### amount: `int`<a id="amount-int"></a>

##### currency: `str`<a id="currency-str"></a>

  The three-letter code for the expense currency.<br/>   Examples: `\\\"USD\\\"`, `\\\"EUR\\\"`, `\\\"CAD\\\"` 

##### employment_id: `str`<a id="employment_id-str"></a>

The ID for the employment to which this expense relates.

##### expense_date: `str`<a id="expense_date-str"></a>

Date of the purchase, which must be in the past

##### category: `str`<a id="category-str"></a>

Categories allowed for an expense

##### receipt: [`Base64File`](./remote_python_sdk/type/base64_file.py)<a id="receipt-base64fileremote_python_sdktypebase64_filepy"></a>


##### receipts: List[`Base64File`]<a id="receipts-listbase64file"></a>

##### reviewed_at: `date`<a id="reviewed_at-date"></a>

The date and time that the expense was reviewed in ISO8601 format. If not provided, it defaults to the current datetime.

##### reviewer_id: `str`<a id="reviewer_id-str"></a>

If the person reviewing the expense is a user in Remote, you can provide its user id for this field. If a value is not provided, defaults to the user that generated the API token.

##### tax_amount: `int`<a id="tax_amount-int"></a>

##### timezone: `str`<a id="timezone-str"></a>

[TZ identifier](https://www.iana.org/time-zones)

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ParamsToCreateExpense`](./remote_python_sdk/type/params_to_create_expense.py)
Expenses

#### 🔄 Return<a id="🔄-return"></a>

[`ExpenseResponse`](./remote_python_sdk/pydantic/expense_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/expenses` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `remote.expenses.download_receipt`<a id="remoteexpensesdownload_receipt"></a>

  Downloads an expense receipt.

  Deprecated since late February 2024 in favour of **[Download a receipt by id](https://gateway.remote.com/v1/docs/openapi.html)** endpoint.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
download_receipt_response = remote.expenses.download_receipt(
    expense_id="3ab2e491-ad1c-47af-849c-3d0a53e20e0d",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### expense_id: `str`<a id="expense_id-str"></a>

The expense ID

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/expenses/{expense_id}/receipt` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `remote.expenses.download_receipt_by_id`<a id="remoteexpensesdownload_receipt_by_id"></a>

Download a receipt by id.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
download_receipt_by_id_response = remote.expenses.download_receipt_by_id(
    expense_id="3ab2e491-ad1c-47af-849c-3d0a53e20e0d",
    receipt_id="6ab2e49o-ad1c-47af-849c-3d0a53e21e0e",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### expense_id: `str`<a id="expense_id-str"></a>

The expense ID

##### receipt_id: `str`<a id="receipt_id-str"></a>

The receipt ID

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/expenses/{expense_id}/receipts/{receipt_id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `remote.expenses.list_records`<a id="remoteexpenseslist_records"></a>

Lists all expenses records

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_records_response = remote.expenses.list_records(
    page=1,
    page_size=30,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### page: `int`<a id="page-int"></a>

Starts fetching records after the given page

##### page_size: `int`<a id="page_size-int"></a>

Change the amount of records returned per page, defaults to 20, limited to 100

#### 🔄 Return<a id="🔄-return"></a>

[`ListExpenseResponse`](./remote_python_sdk/pydantic/list_expense_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/expenses` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `remote.expenses.show_record`<a id="remoteexpensesshow_record"></a>

Shows a single expense record

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
show_record_response = remote.expenses.show_record(
    id="id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

Expense ID

#### 🔄 Return<a id="🔄-return"></a>

[`ExpenseResponse`](./remote_python_sdk/pydantic/expense_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/expenses/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `remote.expenses.update_expense`<a id="remoteexpensesupdate_expense"></a>

Updates an expense

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_expense_response = remote.expenses.update_expense(
    id="id_example",
    status="declined",
    reason="Expense not refundable",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

Expense ID

##### status: `str`<a id="status-str"></a>

##### reason: `str`<a id="reason-str"></a>

Reason for declination.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UpdateExpenseParams`](./remote_python_sdk/type/update_expense_params.py)
Expenses

#### 🔄 Return<a id="🔄-return"></a>

[`ExpenseResponse`](./remote_python_sdk/pydantic/expense_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/expenses/{id}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `remote.expenses.update_record`<a id="remoteexpensesupdate_record"></a>

Updates an expense

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_record_response = remote.expenses.update_record(
    id="id_example",
    status="declined",
    reason="Expense not refundable",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

Expense ID

##### status: `str`<a id="status-str"></a>

##### reason: `str`<a id="reason-str"></a>

Reason for declination.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UpdateExpenseParams`](./remote_python_sdk/type/update_expense_params.py)
Expenses

#### 🔄 Return<a id="🔄-return"></a>

[`ExpenseResponse`](./remote_python_sdk/pydantic/expense_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/expenses/{id}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `remote.files.download_file`<a id="remotefilesdownload_file"></a>

Downloads a file.

Please contact api-support@remote.com to request access to this endpoint.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
download_file_response = remote.files.download_file(
    id="93t3j-file-id-9suej43",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

File ID

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/files/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `remote.files.upload_employment_file`<a id="remotefilesupload_employment_file"></a>

Uploads a file associated with a specified employment.

Please contact api-support@remote.com to request access to this endpoint.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
upload_employment_file_response = remote.files.upload_employment_file(
    employment_id="string_example",
    file=open('/path/to/file', 'rb'),
    type="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### employment_id: `str`<a id="employment_id-str"></a>

##### file: `IO`<a id="file-io"></a>

##### type: `str`<a id="type-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`FileParams`](./remote_python_sdk/type/file_params.py)
The file to be uploaded

#### 🔄 Return<a id="🔄-return"></a>

[`FileResponse`](./remote_python_sdk/pydantic/file_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/documents` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `remote.identity.get_token_info`<a id="remoteidentityget_token_info"></a>

Shows information about the entities that can be controlled by the current auth token.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_token_info_response = remote.identity.get_token_info()
```

#### 🔄 Return<a id="🔄-return"></a>

[`IdentityCurrentResponse`](./remote_python_sdk/pydantic/identity_current_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/identity/current` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `remote.incentives.create_incentive`<a id="remoteincentivescreate_incentive"></a>

Creates an Incentive.

Incentives use the currency of the employment specified provided in the `employment_id` field.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_incentive_response = remote.incentives.create_incentive(
    amount=50000,
    amount_tax_type="net",
    effective_date="Sun Dec 19 16:00:00 PST 2021",
    employment_id="string_example",
    type="acting_up_allowance",
    note="Bonus for moving start date to an earlier date",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### amount: `int`<a id="amount-int"></a>

The amount (in the currency of the employment) to be given to the employee.  This field accepts fractional amounts as well. However to avoid precision issues and errors that can arise from storing fractional amounts, the Remote API only accepts currencies and their fractional amounts as integers. This means you should append fractional amounts to the end of the amount you're passing in with this field.  For example, if the incentive you're offering is EUR 500.25, you would specify `50025` as the amount for this field. 

##### amount_tax_type: [`AmountTaxType`](./remote_python_sdk/type/amount_tax_type.py)<a id="amount_tax_type-amounttaxtyperemote_python_sdktypeamount_tax_typepy"></a>

##### effective_date: `date`<a id="effective_date-date"></a>

The date at which the incentive should take effect.  Note that the incentive is not paid out on the effective date, but during the next payroll cycle. The effective date determines which payroll cycle the incentive will be paid out in.  The effective date needs to be today or a future date.  Note for recurring incentives: since the months don't have the same amount of days, if day of month of `effective_date` is one of [28, 29, 30, 31] it will be transformed to the last day of each month, avoiding the possibility of skipping a month in the recurrence. 

##### employment_id: `str`<a id="employment_id-str"></a>

##### type: `str`<a id="type-str"></a>

##### note: `Optional[str]`<a id="note-optionalstr"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CreateOneTimeIncentiveParams`](./remote_python_sdk/type/create_one_time_incentive_params.py)
Incentive

#### 🔄 Return<a id="🔄-return"></a>

[`IncentiveResponse`](./remote_python_sdk/pydantic/incentive_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/incentives` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `remote.incentives.list_all`<a id="remoteincentiveslist_all"></a>

Lists all Incentives of a company

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_all_response = remote.incentives.list_all(
    employment_id="93t3j-employment-id-9suej43",
    status="paid",
    recurring_incentive_id="2f900aaf-4952-4ec4-ac7c-2b917a2b4da9",
    page=1,
    page_size=30,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### employment_id: `str`<a id="employment_id-str"></a>

Filter by Employment ID

##### status: `str`<a id="status-str"></a>

Filter by Incentive status

##### recurring_incentive_id: `str`<a id="recurring_incentive_id-str"></a>

Filter by Recurring Incentive id

##### page: `int`<a id="page-int"></a>

Starts fetching records after the given page

##### page_size: `int`<a id="page_size-int"></a>

Change the amount of records returned per page, defaults to 20, limited to 100

#### 🔄 Return<a id="🔄-return"></a>

[`ListIncentivesResponse`](./remote_python_sdk/pydantic/list_incentives_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/incentives` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `remote.incentives.remove_incentive`<a id="remoteincentivesremove_incentive"></a>

Delete an incentive.

`one_time` incentives that have the following status **CANNOT** be deleted:
* `processing`
* `paid`


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
remove_incentive_response = remote.incentives.remove_incentive(
    id="id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

Incentive ID

#### 🔄 Return<a id="🔄-return"></a>

[`SuccessResponse`](./remote_python_sdk/pydantic/success_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/incentives/{id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `remote.incentives.show_details`<a id="remoteincentivesshow_details"></a>

Show an Incentive's details

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
show_details_response = remote.incentives.show_details(
    id="id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

Incentive ID

#### 🔄 Return<a id="🔄-return"></a>

[`IncentiveResponse`](./remote_python_sdk/pydantic/incentive_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/incentives/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `remote.incentives.update_incentive`<a id="remoteincentivesupdate_incentive"></a>

Updates an Incentive.

Incentives use the currency of the employment specified provided in the `employment_id` field.

The API doesn't support updating paid incentives.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_incentive_response = remote.incentives.update_incentive(
    id="id_example",
    amount=50000,
    amount_tax_type="net",
    effective_date="Sun Dec 19 16:00:00 PST 2021",
    note="Bonus for moving start date to an earlier date",
    type="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

Incentive ID

##### amount: `int`<a id="amount-int"></a>

The amount (in the currency of the employment) to be given to the employee.  This field accepts fractional amounts as well. However to avoid precision issues and errors that can arise from storing fractional amounts, the Remote API only accepts currencies and their fractional amounts as integers. This means you should append fractional amounts to the end of the amount you're passing in with this field.  For example, if the incentive you're offering is EUR 500.25, you would specify `50025` as the amount for this field. 

##### amount_tax_type: [`AmountTaxType`](./remote_python_sdk/type/amount_tax_type.py)<a id="amount_tax_type-amounttaxtyperemote_python_sdktypeamount_tax_typepy"></a>

##### effective_date: `date`<a id="effective_date-date"></a>

The date at which the incentive should take effect.  Note that the incentive is not paid out on the effective date, but during the next payroll cycle. The effective date determines which payroll cycle the incentive will be paid out in.  The effective date needs to be today or a future date.  Note for recurring incentives: since the months don't have the same amount of days, if day of month of `effective_date` is one of [28, 29, 30, 31] it will be transformed to the last day of each month, avoiding the possibility of skipping a month in the recurrence. 

##### note: `Optional[str]`<a id="note-optionalstr"></a>

##### type: `str`<a id="type-str"></a>

A valid type according to the payment frequency

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UpdateIncentiveParams`](./remote_python_sdk/type/update_incentive_params.py)
Incentive

#### 🔄 Return<a id="🔄-return"></a>

[`IncentiveResponse`](./remote_python_sdk/pydantic/incentive_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/incentives/{id}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `remote.incentives.update_incentive_0`<a id="remoteincentivesupdate_incentive_0"></a>

Updates an Incentive.

Incentives use the currency of the employment specified provided in the `employment_id` field.

The API doesn't support updating paid incentives.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_incentive_0_response = remote.incentives.update_incentive_0(
    id="id_example",
    amount=50000,
    amount_tax_type="net",
    effective_date="Sun Dec 19 16:00:00 PST 2021",
    note="Bonus for moving start date to an earlier date",
    type="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

Incentive ID

##### amount: `int`<a id="amount-int"></a>

The amount (in the currency of the employment) to be given to the employee.  This field accepts fractional amounts as well. However to avoid precision issues and errors that can arise from storing fractional amounts, the Remote API only accepts currencies and their fractional amounts as integers. This means you should append fractional amounts to the end of the amount you're passing in with this field.  For example, if the incentive you're offering is EUR 500.25, you would specify `50025` as the amount for this field. 

##### amount_tax_type: [`AmountTaxType`](./remote_python_sdk/type/amount_tax_type.py)<a id="amount_tax_type-amounttaxtyperemote_python_sdktypeamount_tax_typepy"></a>

##### effective_date: `date`<a id="effective_date-date"></a>

The date at which the incentive should take effect.  Note that the incentive is not paid out on the effective date, but during the next payroll cycle. The effective date determines which payroll cycle the incentive will be paid out in.  The effective date needs to be today or a future date.  Note for recurring incentives: since the months don't have the same amount of days, if day of month of `effective_date` is one of [28, 29, 30, 31] it will be transformed to the last day of each month, avoiding the possibility of skipping a month in the recurrence. 

##### note: `Optional[str]`<a id="note-optionalstr"></a>

##### type: `str`<a id="type-str"></a>

A valid type according to the payment frequency

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UpdateIncentiveParams`](./remote_python_sdk/type/update_incentive_params.py)
Incentive

#### 🔄 Return<a id="🔄-return"></a>

[`IncentiveResponse`](./remote_python_sdk/pydantic/incentive_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/incentives/{id}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `remote.o_auth2.exchange_token`<a id="remoteo_auth2exchange_token"></a>

Endpoint to exchange tokens in the Authorization Code, Client Credentials and Refresh Token flows

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
exchange_token_response = remote.o_auth2.exchange_token(
    code="eyJhbG...xb6H0",
    grant_type="refresh_token",
    client_id="<client_id>",
    refresh_token="b480036a-d229-49ef-a606-7e8fba58a5eb",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### code: `str`<a id="code-str"></a>

The authorization code generated in Authorization Code flow

##### grant_type: `str`<a id="grant_type-str"></a>

The Authorization flow

##### client_id: `str`<a id="client_id-str"></a>

The client id generated during registration

##### refresh_token: `str`<a id="refresh_token-str"></a>

The refresh token generated in the Authorization Code flow

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`OAuth2TokenParams`](./remote_python_sdk/type/o_auth2_token_params.py)
OAuth2Token

#### 🔄 Return<a id="🔄-return"></a>

[`OAuth2Tokens`](./remote_python_sdk/pydantic/o_auth2_tokens.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/auth/oauth2/token` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `remote.offboarding.create_request`<a id="remoteoffboardingcreate_request"></a>

Creates an Offboarding request.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_request_response = remote.offboarding.create_request(
    employment_id="5e55386e-4f4f-4def-92f4-bdc19a5ce77d",
    termination_details={
        "additional_comments": "additional comments regarding the termination reason",
        "confidential": False,
        "proposed_termination_date": "Tue Dec 19 16:00:00 PST 2023",
        "reason_description": "termination reason",
        "risk_assessment_reasons": [
            "caring_responsibilities"
        ],
        "termination_reason": "workforce_reduction",
        "will_challenge_termination": True,
        "will_challenge_termination_description": "additional details for the offboarding risk assessment",
    },
    type="termination",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### employment_id: `str`<a id="employment_id-str"></a>

##### termination_details: [`TerminationDetailsParams`](./remote_python_sdk/type/termination_details_params.py)<a id="termination_details-terminationdetailsparamsremote_python_sdktypetermination_details_paramspy"></a>


##### type: `str`<a id="type-str"></a>

The type of the offboarding request. For now, only `termination` is allowed.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CreateOffboardingParams`](./remote_python_sdk/type/create_offboarding_params.py)
Incentive

#### 🔄 Return<a id="🔄-return"></a>

[`OffboardingResponse`](./remote_python_sdk/pydantic/offboarding_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/offboardings` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `remote.offboarding.list_requests`<a id="remoteoffboardinglist_requests"></a>

Lists Offboarding requests.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_requests_response = remote.offboarding.list_requests(
    employment_id="93t3j-employment-id-9suej43",
    type="paid",
    include_confidential="true",
    page=1,
    page_size=30,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### employment_id: `str`<a id="employment_id-str"></a>

Filter by Employment ID

##### type: `str`<a id="type-str"></a>

Filter by offboarding type

##### include_confidential: `str`<a id="include_confidential-str"></a>

By default, the results do not include confidential termination requests. Send `include_confidential=true` to include confidential requests in the response. 

##### page: `int`<a id="page-int"></a>

Starts fetching records after the given page

##### page_size: `int`<a id="page_size-int"></a>

Change the amount of records returned per page, defaults to 20, limited to 100

#### 🔄 Return<a id="🔄-return"></a>

[`ListOffboardingResponse`](./remote_python_sdk/pydantic/list_offboarding_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/offboardings` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `remote.offboarding.show_request`<a id="remoteoffboardingshow_request"></a>

Shows an Offboarding request.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
show_request_response = remote.offboarding.show_request(
    id="id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

Offboarding request ID

#### 🔄 Return<a id="🔄-return"></a>

[`OffboardingResponse`](./remote_python_sdk/pydantic/offboarding_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/offboardings/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `remote.payslips.download_pdf`<a id="remotepayslipsdownload_pdf"></a>

Given a Payslip ID, downloads a payslip.
It is important to note that each country has a different payslip format and they are not authored by Remote.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
download_pdf_response = remote.payslips.download_pdf(
    payslip_id="93t3j-payslip-id-9suej43",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### payslip_id: `str`<a id="payslip_id-str"></a>

Payslip ID

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/payslips/{payslip_id}/pdf` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `remote.payslips.list_all`<a id="remotepayslipslist_all"></a>

Lists all payslips belonging to a company. Can also filter for a single employment belonging
to that company.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_all_response = remote.payslips.list_all(
    employment_id="93t3j-employment-id-9suej43",
    start_date="\"2022-12-15\"",
    end_date="\"2023-12-15\"",
    expected_payout_start_date="\"2022-12-15\"",
    expected_payout_end_date="\"2023-12-15\"",
    page=1,
    page_size=30,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### employment_id: `str`<a id="employment_id-str"></a>

Employment ID

##### start_date: `str`<a id="start_date-str"></a>

Filters by payslips `issued_at` field, after or on the same day than the given date

##### end_date: `str`<a id="end_date-str"></a>

Filters by payslips `issued_at` field, before or or the same day than the given date

##### expected_payout_start_date: `str`<a id="expected_payout_start_date-str"></a>

Filters by payslips `expected_payout_date` field, after or on the same day than the given date

##### expected_payout_end_date: `str`<a id="expected_payout_end_date-str"></a>

Filters by payslips `expected_payout_date` field, before or or the same day than the given date

##### page: `int`<a id="page-int"></a>

Starts fetching records after the given page

##### page_size: `int`<a id="page_size-int"></a>

Change the amount of records returned per page, defaults to 20, limited to 100

#### 🔄 Return<a id="🔄-return"></a>

[`ListPayslipsResponse`](./remote_python_sdk/pydantic/list_payslips_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/payslips` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `remote.payslips.show_payslip`<a id="remotepayslipsshow_payslip"></a>

Given an ID, shows a payslip.

Please contact api-support@remote.com to request access to this endpoint.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
show_payslip_response = remote.payslips.show_payslip(
    id="93t3j-payslip-id-9suej43",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

Payslip ID

#### 🔄 Return<a id="🔄-return"></a>

[`PayslipResponse`](./remote_python_sdk/pydantic/payslip_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/payslips/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `remote.recurring_incentives.create_monthly_incentive`<a id="remoterecurring_incentivescreate_monthly_incentive"></a>

Create a Recurring Incentive, that is, a monthly paid incentive.

Incentives use the currency of the employment specified provided in the `employment_id` field.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_monthly_incentive_response = remote.recurring_incentives.create_monthly_incentive(
    amount=50000,
    amount_tax_type="net",
    effective_date="Sun Dec 19 16:00:00 PST 2021",
    employment_id="string_example",
    type="acting_up_allowance",
    note="Bonus for moving start date to an earlier date",
    duration_in_months="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### amount: `int`<a id="amount-int"></a>

The amount (in the currency of the employment) to be given to the employee.  This field accepts fractional amounts as well. However to avoid precision issues and errors that can arise from storing fractional amounts, the Remote API only accepts currencies and their fractional amounts as integers. This means you should append fractional amounts to the end of the amount you're passing in with this field.  For example, if the incentive you're offering is EUR 500.25, you would specify `50025` as the amount for this field. 

##### amount_tax_type: [`AmountTaxType`](./remote_python_sdk/type/amount_tax_type.py)<a id="amount_tax_type-amounttaxtyperemote_python_sdktypeamount_tax_typepy"></a>

##### effective_date: `date`<a id="effective_date-date"></a>

The date at which the incentive should take effect.  Note that the incentive is not paid out on the effective date, but during the next payroll cycle. The effective date determines which payroll cycle the incentive will be paid out in.  The effective date needs to be today or a future date.  Note for recurring incentives: since the months don't have the same amount of days, if day of month of `effective_date` is one of [28, 29, 30, 31] it will be transformed to the last day of each month, avoiding the possibility of skipping a month in the recurrence. 

##### employment_id: `str`<a id="employment_id-str"></a>

##### type: `str`<a id="type-str"></a>

##### note: `Optional[str]`<a id="note-optionalstr"></a>

##### duration_in_months: `int`<a id="duration_in_months-int"></a>

How many times the payment will repeat. At the moment we only fully support monthly frequency.  This field is only necessary if the recurring incentive has an end date. 

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CreateRecurringIncentiveParams`](./remote_python_sdk/type/create_recurring_incentive_params.py)
RecurringIncentive

#### 🔄 Return<a id="🔄-return"></a>

[`RecurringIncentiveResponse`](./remote_python_sdk/pydantic/recurring_incentive_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/incentives/recurring` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `remote.recurring_incentives.delete_scheduled`<a id="remoterecurring_incentivesdelete_scheduled"></a>

Delete a Recurring Incentive, that is, a monthly paid incentive.

Internally, Remote schedules upcoming incentives. As such, when you attempt to
delete a recurring incentive, Remote will **ONLY** delete scheduled incentives
with the `pending` status.

Incentives payments that are already scheduled and cannot be deleted will be
included in the response, in case you need to reference them.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
delete_scheduled_response = remote.recurring_incentives.delete_scheduled(
    id="id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

Recurring Incentive ID

#### 🔄 Return<a id="🔄-return"></a>

[`DeleteRecurringIncentiveResponse`](./remote_python_sdk/pydantic/delete_recurring_incentive_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/incentives/recurring/{id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `remote.recurring_incentives.list_incentives`<a id="remoterecurring_incentiveslist_incentives"></a>

List all Recurring Incentives of a company.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_incentives_response = remote.recurring_incentives.list_incentives(
    status="active",
    type="meal_allowance",
    note="meal",
    page=1,
    page_size=30,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### status: `str`<a id="status-str"></a>

Filter by recurring incentive status: active or deactive.

##### type: `str`<a id="type-str"></a>

Filter by recurring incentive type.

##### note: `str`<a id="note-str"></a>

Filter by recurring incentives that contain the value in their notes.

##### page: `int`<a id="page-int"></a>

Starts fetching records after the given page

##### page_size: `int`<a id="page_size-int"></a>

Change the amount of records returned per page, defaults to 20, limited to 100

#### 🔄 Return<a id="🔄-return"></a>

[`ListRecurringIncentivesResponse`](./remote_python_sdk/pydantic/list_recurring_incentives_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/incentives/recurring` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `remote.resignation.download_letter`<a id="remoteresignationdownload_letter"></a>

Downloads a resignation letter from an employment request.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
download_letter_response = remote.resignation.download_letter(
    employment_request_id="3ab2e491-ad1c-47af-849c-3d0a53e20e0d",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### employment_request_id: `str`<a id="employment_request_id-str"></a>

The employment request ID

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/resignations/{employment_request_id}/resignation-letter` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `remote.sandbox.create_employment_without_validations`<a id="remotesandboxcreate_employment_without_validations"></a>

Creates an employment without provisional_start_date validation.

This endpoint is only available in Sandbox and allows creating employments which
`provisional_start_date` is in the past. This is especially helpful for:
  * Testing the Timeoff Balance endpoints
  * Testing the Offboarding endpoints
  * Testing features around probation periods

This endpoint will respond with a 404 outside of the Sandbox environment.

For creating an employment's parameters outside of testing purposes, use [this
Employment create endpoint](https://gateway.remote.com/v1/docs/openapi.html)


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_employment_without_validations_response = remote.sandbox.create_employment_without_validations(
    country_code="string_example",
    full_name="string_example",
    job_title="string_example",
    personal_email="string_example",
    basic_information={},
    company_id="string_example",
    type="employee",
    provisional_start_date="Fri Jul 02 17:00:00 PDT 2021",
    seniority_date="2022-03-21",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### country_code: `str`<a id="country_code-str"></a>

##### full_name: `str`<a id="full_name-str"></a>

##### job_title: `str`<a id="job_title-str"></a>

##### personal_email: `str`<a id="personal_email-str"></a>

##### basic_information: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="basic_information-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

Employment basic information. When using this field, the same other root level fields (name, personal_email, job_title, provisional_start_date, and seniority_date) will be ignored. Its properties may vary depending on the country, you must query the [Show form schema](https://gateway.remote.com/v1/docs/openapi.html) endpoint passing the country code and `employment_basic_information` as path parameters. 

##### company_id: `str`<a id="company_id-str"></a>

This optional field is deprecated.

##### type: `str`<a id="type-str"></a>

If not provided, it will default to `employee`.

##### provisional_start_date: `date`<a id="provisional_start_date-date"></a>

Indicates the expected start date of the employee or contractor.  Required for employees, but optional for contractors. Date format is in ISO8601 without the time component.  See the **Date and Time Format** documentation for more details on how the Remote API works with dates. 

##### seniority_date: `datetime`<a id="seniority_date-datetime"></a>

The date the employee first started working for your company. If you don’t include a seniority date, the employee’s start date with Remote will be deemed as the start of the employee’s seniority.  **Example**: Your employee started working for your company on Feb 1, 2022. On Aug 1, 2022, you transferred the employee to Remote and started managing them on the platform. Feb 1, 2022 would be their seniority date. Aug 1, 2022 would be their starting date. 

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`EmploymentBasicParams`](./remote_python_sdk/type/employment_basic_params.py)
Employment params

#### 🔄 Return<a id="🔄-return"></a>

[`EmploymentCreationResponse`](./remote_python_sdk/pydantic/employment_creation_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/sandbox/employments` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `remote.sandbox.employment_update`<a id="remotesandboxemployment_update"></a>

Updates an employment. Use this endpoint to modify employment states for testing
in the Sandbox environment. This endpoint will respond with a 404 outside of the
Sandbox environment.

For updating an employment's parameters outside of testing purposes, use [this
Employment update endpoint](https://gateway.remote.com/v1/docs/openapi.html).


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
employment_update_response = remote.sandbox.employment_update(
    employment_id="e3ee69d7-1293-4664-92fc-02625dae5247",
    status="active",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### employment_id: `str`<a id="employment_id-str"></a>

Employment ID

##### status: [`EmploymentStatus`](./remote_python_sdk/type/employment_status.py)<a id="status-employmentstatusremote_python_sdktypeemployment_statuspy"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`EmploymentUpdateParams`](./remote_python_sdk/type/employment_update_params.py)
Employment params

#### 🔄 Return<a id="🔄-return"></a>

[`EmploymentResponse`](./remote_python_sdk/pydantic/employment_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/sandbox/employments/{employment_id}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `remote.sandbox.trigger_webhook_callback`<a id="remotesandboxtrigger_webhook_callback"></a>

Triggers a callback previously registered for webhooks. Use this endpoint to
emit a webhook for testing in the Sandbox environment. This endpoint will
respond with a 404 outside of the Sandbox environment.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trigger_webhook_callback_response = remote.sandbox.trigger_webhook_callback(
    employment_id="e966a8b8-1076-11ee-a5f2-9b3997a968f6",
    event_type="employment.onboarding_task.completed",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### employment_id: `str`<a id="employment_id-str"></a>

##### event_type: `str`<a id="event_type-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`WebhookTriggerParams`](./remote_python_sdk/type/webhook_trigger_params.py)
Webhook Trigger Params

#### 🔄 Return<a id="🔄-return"></a>

[`SuccessResponse`](./remote_python_sdk/pydantic/success_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/sandbox/webhook-callbacks/trigger` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `remote.sandbox.update_employment_state`<a id="remotesandboxupdate_employment_state"></a>

Updates an employment. Use this endpoint to modify employment states for testing
in the Sandbox environment. This endpoint will respond with a 404 outside of the
Sandbox environment.

For updating an employment's parameters outside of testing purposes, use [this
Employment update endpoint](https://gateway.remote.com/v1/docs/openapi.html).


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_employment_state_response = remote.sandbox.update_employment_state(
    employment_id="e3ee69d7-1293-4664-92fc-02625dae5247",
    status="active",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### employment_id: `str`<a id="employment_id-str"></a>

Employment ID

##### status: [`EmploymentStatus`](./remote_python_sdk/type/employment_status.py)<a id="status-employmentstatusremote_python_sdktypeemployment_statuspy"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`EmploymentUpdateParams`](./remote_python_sdk/type/employment_update_params.py)
Employment params

#### 🔄 Return<a id="🔄-return"></a>

[`EmploymentResponse`](./remote_python_sdk/pydantic/employment_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/sandbox/employments/{employment_id}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `remote.time_off.get_record`<a id="remotetime_offget_record"></a>

Shows a single Time Off record

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_record_response = remote.time_off.get_record(
    id="93t3j-timeoff-id-9suej43",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

Timeoff ID

#### 🔄 Return<a id="🔄-return"></a>

[`TimeoffResponse`](./remote_python_sdk/pydantic/timeoff_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/timeoff/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `remote.time_off.list_records`<a id="remotetime_offlist_records"></a>

Lists all Time Off records.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_records_response = remote.time_off.list_records(
    employment_id="31b8e49b-aa1c-47af-849c-3d0a53e20e0d",
    timeoff_type="sick_leave",
    status="approved",
    order="asc",
    sort_by="timeoff_type",
    page=1,
    page_size=20,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### employment_id: `str`<a id="employment_id-str"></a>

Only show time off for a specific employment

##### timeoff_type: [`TimeoffType`](./remote_python_sdk/type/.py)<a id="timeoff_type-timeofftyperemote_python_sdktypepy"></a>

Filter time off by its type

##### status: [`TimeoffStatus`](./remote_python_sdk/type/.py)<a id="status-timeoffstatusremote_python_sdktypepy"></a>

Filter time off by its status

##### order: `str`<a id="order-str"></a>

Sort order

##### sort_by: `str`<a id="sort_by-str"></a>

Field to sort by

##### page: `int`<a id="page-int"></a>

Starts fetching records after the given page

##### page_size: `int`<a id="page_size-int"></a>

Number of items per page

#### 🔄 Return<a id="🔄-return"></a>

[`ListTimeoffResponse`](./remote_python_sdk/pydantic/list_timeoff_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/timeoff` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `remote.time_off.list_types`<a id="remotetime_offlist_types"></a>

Lists all time off types that can be used for the `timeoff_type` parameter

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_types_response = remote.time_off.list_types()
```

#### 🔄 Return<a id="🔄-return"></a>

[`ListTimeoffTypesResponse`](./remote_python_sdk/pydantic/list_timeoff_types_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/timeoff/types` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `remote.time_off.record_create`<a id="remotetime_offrecord_create"></a>

Creates a Time Off record

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
record_create_response = remote.time_off.record_create(
    approved_at="2021-07-15T18:18:17Z",
    approver_id="51546f60-dd71-4223-9312-4efede68a497",
    status="approved",
    document={
        "content": "content_example",
        "name": "name_example",
    },
    employment_id="string_example",
    end_date="string_example",
    notes="string_example",
    start_date="string_example",
    timeoff_days=[
        {
            "day": "2021-07-01",
        }
    ],
    timeoff_type="sick_leave",
    timezone="Etc/UTC",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### approved_at: `datetime`<a id="approved_at-datetime"></a>

UTC date time in [ISO 8601][] format.  [ISO 8601]: https://en.wikipedia.org/wiki/ISO_8601 

##### approver_id: [`NullableApproverId`](./remote_python_sdk/type/nullable_approver_id.py)<a id="approver_id-nullableapproveridremote_python_sdktypenullable_approver_idpy"></a>

##### status: `str`<a id="status-str"></a>

##### document: [`TimeoffDocumentParams`](./remote_python_sdk/type/timeoff_document_params.py)<a id="document-timeoffdocumentparamsremote_python_sdktypetimeoff_document_paramspy"></a>


##### employment_id: `str`<a id="employment_id-str"></a>

##### end_date: `str`<a id="end_date-str"></a>

##### notes: `str`<a id="notes-str"></a>

##### start_date: `str`<a id="start_date-str"></a>

##### timeoff_days: List[`TimeoffDaysParams`]<a id="timeoff_days-listtimeoffdaysparams"></a>

##### timeoff_type: [`TimeoffType`](./remote_python_sdk/type/timeoff_type.py)<a id="timeoff_type-timeofftyperemote_python_sdktypetimeoff_typepy"></a>

##### timezone: `str`<a id="timezone-str"></a>

[TZ identifier](https://www.iana.org/time-zones)

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CreateApprovedTimeoffParams`](./remote_python_sdk/type/create_approved_timeoff_params.py)
Timeoff

#### 🔄 Return<a id="🔄-return"></a>

[`TimeoffResponse`](./remote_python_sdk/pydantic/timeoff_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/timeoff` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `remote.time_off.update_record`<a id="remotetime_offupdate_record"></a>

Updates a Time Off record. This endpoint can also be used for cancelling a time off.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_record_response = remote.time_off.update_record(
    cancel_reason="string_example",
    edit_reason="string_example",
    id="93t3j-timeoff-id-9suej43",
    approved_at="2021-07-15T18:18:17Z",
    approver_id="51546f60-dd71-4223-9312-4efede68a497",
    document={
        "content": "content_example",
        "name": "name_example",
    },
    end_date="2021-07-01",
    notes="string_example",
    start_date="2021-07-01",
    status="approved",
    timeoff_days=[
        {
            "day": "2021-07-01",
        }
    ],
    timeoff_type="sick_leave",
    timezone="Etc/UTC",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### cancel_reason: `str`<a id="cancel_reason-str"></a>

The reason for cancelling a time off. Required when updating to status `cancelled`.

##### edit_reason: `str`<a id="edit_reason-str"></a>

The reason for the update. Required when updating the time off data but not changing the status.

##### id: `str`<a id="id-str"></a>

Timeoff ID

##### approved_at: `datetime`<a id="approved_at-datetime"></a>

UTC date time in [ISO 8601][] format.  [ISO 8601]: https://en.wikipedia.org/wiki/ISO_8601 

##### approver_id: [`NullableApproverId`](./remote_python_sdk/type/nullable_approver_id.py)<a id="approver_id-nullableapproveridremote_python_sdktypenullable_approver_idpy"></a>

##### document: [`TimeoffDocumentParams`](./remote_python_sdk/type/timeoff_document_params.py)<a id="document-timeoffdocumentparamsremote_python_sdktypetimeoff_document_paramspy"></a>


##### end_date: `date`<a id="end_date-date"></a>

UTC date in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format

##### notes: `str`<a id="notes-str"></a>

##### start_date: `date`<a id="start_date-date"></a>

UTC date in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format

##### status: `str`<a id="status-str"></a>

##### timeoff_days: List[`TimeoffDaysParams`]<a id="timeoff_days-listtimeoffdaysparams"></a>

##### timeoff_type: [`TimeoffType`](./remote_python_sdk/type/timeoff_type.py)<a id="timeoff_type-timeofftyperemote_python_sdktypetimeoff_typepy"></a>

##### timezone: `str`<a id="timezone-str"></a>

[TZ identifier](https://www.iana.org/time-zones)

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UpdateApprovedTimeoffParams`](./remote_python_sdk/type/update_approved_timeoff_params.py)
UpdateTimeoff

#### 🔄 Return<a id="🔄-return"></a>

[`TimeoffResponse`](./remote_python_sdk/pydantic/timeoff_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/timeoff/{id}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `remote.time_off.update_record_0`<a id="remotetime_offupdate_record_0"></a>

Updates a Time Off record. This endpoint can also be used for cancelling a time off.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_record_0_response = remote.time_off.update_record_0(
    cancel_reason="string_example",
    edit_reason="string_example",
    id="93t3j-timeoff-id-9suej43",
    approved_at="2021-07-15T18:18:17Z",
    approver_id="51546f60-dd71-4223-9312-4efede68a497",
    document={
        "content": "content_example",
        "name": "name_example",
    },
    end_date="2021-07-01",
    notes="string_example",
    start_date="2021-07-01",
    status="approved",
    timeoff_days=[
        {
            "day": "2021-07-01",
        }
    ],
    timeoff_type="sick_leave",
    timezone="Etc/UTC",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### cancel_reason: `str`<a id="cancel_reason-str"></a>

The reason for cancelling a time off. Required when updating to status `cancelled`.

##### edit_reason: `str`<a id="edit_reason-str"></a>

The reason for the update. Required when updating the time off data but not changing the status.

##### id: `str`<a id="id-str"></a>

Timeoff ID

##### approved_at: `datetime`<a id="approved_at-datetime"></a>

UTC date time in [ISO 8601][] format.  [ISO 8601]: https://en.wikipedia.org/wiki/ISO_8601 

##### approver_id: [`NullableApproverId`](./remote_python_sdk/type/nullable_approver_id.py)<a id="approver_id-nullableapproveridremote_python_sdktypenullable_approver_idpy"></a>

##### document: [`TimeoffDocumentParams`](./remote_python_sdk/type/timeoff_document_params.py)<a id="document-timeoffdocumentparamsremote_python_sdktypetimeoff_document_paramspy"></a>


##### end_date: `date`<a id="end_date-date"></a>

UTC date in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format

##### notes: `str`<a id="notes-str"></a>

##### start_date: `date`<a id="start_date-date"></a>

UTC date in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format

##### status: `str`<a id="status-str"></a>

##### timeoff_days: List[`TimeoffDaysParams`]<a id="timeoff_days-listtimeoffdaysparams"></a>

##### timeoff_type: [`TimeoffType`](./remote_python_sdk/type/timeoff_type.py)<a id="timeoff_type-timeofftyperemote_python_sdktypetimeoff_typepy"></a>

##### timezone: `str`<a id="timezone-str"></a>

[TZ identifier](https://www.iana.org/time-zones)

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UpdateApprovedTimeoffParams`](./remote_python_sdk/type/update_approved_timeoff_params.py)
UpdateTimeoff

#### 🔄 Return<a id="🔄-return"></a>

[`TimeoffResponse`](./remote_python_sdk/pydantic/timeoff_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/timeoff/{id}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `remote.time_off_balances.show_balance`<a id="remotetime_off_balancesshow_balance"></a>

Shows the time off balance for the given employment_id.

Please note, this endpoint is only supported for employments in certain countries.
For countries where it's not supported, this endpoint will respond with a `404 Not Found`.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
show_balance_response = remote.time_off_balances.show_balance(
    employment_id="03675381-50c9-492d-b8ed-e84e99046091",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### employment_id: `str`<a id="employment_id-str"></a>

Employment ID for which to show the time off balance

#### 🔄 Return<a id="🔄-return"></a>

[`TimeoffBalanceResponse`](./remote_python_sdk/pydantic/timeoff_balance_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/timeoff-balances/{employment_id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `remote.webhook_callbacks.delete_callback`<a id="remotewebhook_callbacksdelete_callback"></a>

Delete a callback previously registered for webhooks

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
delete_callback_response = remote.webhook_callbacks.delete_callback(
    id="id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

Webhook Callback ID

#### 🔄 Return<a id="🔄-return"></a>

[`SuccessResponse`](./remote_python_sdk/pydantic/success_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/webhook-callbacks/{id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `remote.webhook_callbacks.register_callback`<a id="remotewebhook_callbacksregister_callback"></a>

Register a callback to be used for webhooks

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
register_callback_response = remote.webhook_callbacks.register_callback(
    url="https://example.com/callback",
    subscribed_events=[
        "string_example"
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### url: `str`<a id="url-str"></a>

##### subscribed_events: [`CreateWebhookCallbackParamsSubscribedEvents`](./remote_python_sdk/type/create_webhook_callback_params_subscribed_events.py)<a id="subscribed_events-createwebhookcallbackparamssubscribedeventsremote_python_sdktypecreate_webhook_callback_params_subscribed_eventspy"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CreateWebhookCallbackParams`](./remote_python_sdk/type/create_webhook_callback_params.py)
WebhookCallback

#### 🔄 Return<a id="🔄-return"></a>

[`WebhookCallbackResponse`](./remote_python_sdk/pydantic/webhook_callback_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/webhook-callbacks` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---


## Author<a id="author"></a>
This Python package is automatically generated by [Konfig](https://konfigthis.com)
