import typing_extensions

from remote_python_sdk.apis.tags import TagValues
from remote_python_sdk.apis.tags.employments_api import EmploymentsApi
from remote_python_sdk.apis.tags.expenses_api import ExpensesApi
from remote_python_sdk.apis.tags.contract_amendments_api import ContractAmendmentsApi
from remote_python_sdk.apis.tags.time_off_api import TimeOffApi
from remote_python_sdk.apis.tags.incentives_api import IncentivesApi
from remote_python_sdk.apis.tags.companies_api import CompaniesApi
from remote_python_sdk.apis.tags.cost_calculator_api import CostCalculatorApi
from remote_python_sdk.apis.tags.sandbox_api import SandboxApi
from remote_python_sdk.apis.tags.company_managers_api import CompanyManagersApi
from remote_python_sdk.apis.tags.payslips_api import PayslipsApi
from remote_python_sdk.apis.tags.recurring_incentives_api import RecurringIncentivesApi
from remote_python_sdk.apis.tags.offboarding_api import OffboardingApi
from remote_python_sdk.apis.tags.billing_documents_api import BillingDocumentsApi
from remote_python_sdk.apis.tags.countries_api import CountriesApi
from remote_python_sdk.apis.tags.custom_fields_api import CustomFieldsApi
from remote_python_sdk.apis.tags.company_department_api import CompanyDepartmentApi
from remote_python_sdk.apis.tags.files_api import FilesApi
from remote_python_sdk.apis.tags.webhook_callbacks_api import WebhookCallbacksApi
from remote_python_sdk.apis.tags.o_auth2_api import OAuth2Api
from remote_python_sdk.apis.tags.employment_contracts_api import EmploymentContractsApi
from remote_python_sdk.apis.tags.resignation_api import ResignationApi
from remote_python_sdk.apis.tags.benefits_country_summary_api import BenefitsCountrySummaryApi
from remote_python_sdk.apis.tags.identity_api import IdentityApi
from remote_python_sdk.apis.tags.time_off_balances_api import TimeOffBalancesApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.EMPLOYMENTS: EmploymentsApi,
        TagValues.EXPENSES: ExpensesApi,
        TagValues.CONTRACT_AMENDMENTS: ContractAmendmentsApi,
        TagValues.TIME_OFF: TimeOffApi,
        TagValues.INCENTIVES: IncentivesApi,
        TagValues.COMPANIES: CompaniesApi,
        TagValues.COST_CALCULATOR: CostCalculatorApi,
        TagValues.SANDBOX: SandboxApi,
        TagValues.COMPANY_MANAGERS: CompanyManagersApi,
        TagValues.PAYSLIPS: PayslipsApi,
        TagValues.RECURRING_INCENTIVES: RecurringIncentivesApi,
        TagValues.OFFBOARDING: OffboardingApi,
        TagValues.BILLING_DOCUMENTS: BillingDocumentsApi,
        TagValues.COUNTRIES: CountriesApi,
        TagValues.CUSTOM_FIELDS: CustomFieldsApi,
        TagValues.COMPANY_DEPARTMENT: CompanyDepartmentApi,
        TagValues.FILES: FilesApi,
        TagValues.WEBHOOK_CALLBACKS: WebhookCallbacksApi,
        TagValues.OAUTH2: OAuth2Api,
        TagValues.EMPLOYMENT_CONTRACTS: EmploymentContractsApi,
        TagValues.RESIGNATION: ResignationApi,
        TagValues.BENEFITS_COUNTRY_SUMMARY: BenefitsCountrySummaryApi,
        TagValues.IDENTITY: IdentityApi,
        TagValues.TIME_OFF_BALANCES: TimeOffBalancesApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.EMPLOYMENTS: EmploymentsApi,
        TagValues.EXPENSES: ExpensesApi,
        TagValues.CONTRACT_AMENDMENTS: ContractAmendmentsApi,
        TagValues.TIME_OFF: TimeOffApi,
        TagValues.INCENTIVES: IncentivesApi,
        TagValues.COMPANIES: CompaniesApi,
        TagValues.COST_CALCULATOR: CostCalculatorApi,
        TagValues.SANDBOX: SandboxApi,
        TagValues.COMPANY_MANAGERS: CompanyManagersApi,
        TagValues.PAYSLIPS: PayslipsApi,
        TagValues.RECURRING_INCENTIVES: RecurringIncentivesApi,
        TagValues.OFFBOARDING: OffboardingApi,
        TagValues.BILLING_DOCUMENTS: BillingDocumentsApi,
        TagValues.COUNTRIES: CountriesApi,
        TagValues.CUSTOM_FIELDS: CustomFieldsApi,
        TagValues.COMPANY_DEPARTMENT: CompanyDepartmentApi,
        TagValues.FILES: FilesApi,
        TagValues.WEBHOOK_CALLBACKS: WebhookCallbacksApi,
        TagValues.OAUTH2: OAuth2Api,
        TagValues.EMPLOYMENT_CONTRACTS: EmploymentContractsApi,
        TagValues.RESIGNATION: ResignationApi,
        TagValues.BENEFITS_COUNTRY_SUMMARY: BenefitsCountrySummaryApi,
        TagValues.IDENTITY: IdentityApi,
        TagValues.TIME_OFF_BALANCES: TimeOffBalancesApi,
    }
)
