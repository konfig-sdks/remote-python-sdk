# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from remote_python_sdk.apis.tag_to_api import tag_to_api

import enum


class TagValues(str, enum.Enum):
    EMPLOYMENTS = "Employments"
    EXPENSES = "Expenses"
    CONTRACT_AMENDMENTS = "Contract Amendments"
    TIME_OFF = "Time Off"
    INCENTIVES = "Incentives"
    COMPANIES = "Companies"
    COST_CALCULATOR = "Cost Calculator"
    SANDBOX = "Sandbox"
    COMPANY_MANAGERS = "Company Managers"
    PAYSLIPS = "Payslips"
    RECURRING_INCENTIVES = "Recurring Incentives"
    OFFBOARDING = "Offboarding"
    BILLING_DOCUMENTS = "Billing Documents"
    COUNTRIES = "Countries"
    CUSTOM_FIELDS = "Custom Fields"
    COMPANY_DEPARTMENT = "Company Department"
    FILES = "Files"
    WEBHOOK_CALLBACKS = "Webhook Callbacks"
    OAUTH2 = "OAuth2"
    EMPLOYMENT_CONTRACTS = "Employment Contracts"
    RESIGNATION = "Resignation"
    BENEFITS_COUNTRY_SUMMARY = "Benefits Country Summary"
    IDENTITY = "Identity"
    TIME_OFF_BALANCES = "Time Off Balances"
