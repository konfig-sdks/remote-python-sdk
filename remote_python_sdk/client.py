# coding: utf-8
"""
    Remote API

    Talent is everywhere. Opportunity is not. Remote's mission is to create opportunity everywhere, empowering employers to find and hire the best talent, and enabling individuals to build financial and personal freedom.   Remote is a Global HR Platform that helps companies hire, manage, and pay their entire team — and more effectively compete in the modern global economy through our comprehensive set of core solutions including, HRIS, payroll, international employment, contractor management, and more.   Whether you're just starting your global journey, or looking to optimize your existing operations, sign up or book a demo - and see how Remote makes global HR simple.

    The version of the OpenAPI document: 0.1.0
    Generated by: https://konfigthis.com
"""

import typing
import inspect
from datetime import date, datetime
from remote_python_sdk.client_custom import ClientCustom
from remote_python_sdk.configuration import Configuration
from remote_python_sdk.api_client import ApiClient
from remote_python_sdk.type_util import copy_signature
from remote_python_sdk.apis.tags.benefits_country_summary_api import BenefitsCountrySummaryApi
from remote_python_sdk.apis.tags.billing_documents_api import BillingDocumentsApi
from remote_python_sdk.apis.tags.companies_api import CompaniesApi
from remote_python_sdk.apis.tags.company_department_api import CompanyDepartmentApi
from remote_python_sdk.apis.tags.company_managers_api import CompanyManagersApi
from remote_python_sdk.apis.tags.contract_amendments_api import ContractAmendmentsApi
from remote_python_sdk.apis.tags.cost_calculator_api import CostCalculatorApi
from remote_python_sdk.apis.tags.countries_api import CountriesApi
from remote_python_sdk.apis.tags.custom_fields_api import CustomFieldsApi
from remote_python_sdk.apis.tags.employment_contracts_api import EmploymentContractsApi
from remote_python_sdk.apis.tags.employments_api import EmploymentsApi
from remote_python_sdk.apis.tags.expenses_api import ExpensesApi
from remote_python_sdk.apis.tags.files_api import FilesApi
from remote_python_sdk.apis.tags.identity_api import IdentityApi
from remote_python_sdk.apis.tags.incentives_api import IncentivesApi
from remote_python_sdk.apis.tags.o_auth2_api import OAuth2Api
from remote_python_sdk.apis.tags.offboarding_api import OffboardingApi
from remote_python_sdk.apis.tags.payslips_api import PayslipsApi
from remote_python_sdk.apis.tags.recurring_incentives_api import RecurringIncentivesApi
from remote_python_sdk.apis.tags.resignation_api import ResignationApi
from remote_python_sdk.apis.tags.sandbox_api import SandboxApi
from remote_python_sdk.apis.tags.time_off_api import TimeOffApi
from remote_python_sdk.apis.tags.time_off_balances_api import TimeOffBalancesApi
from remote_python_sdk.apis.tags.webhook_callbacks_api import WebhookCallbacksApi



class Remote(ClientCustom):

    def __init__(self, configuration: typing.Union[Configuration, None] = None, **kwargs):
        super().__init__(configuration, **kwargs)
        if (len(kwargs) > 0):
            configuration = Configuration(**kwargs)
        if (configuration is None):
            raise Exception("configuration is required")
        api_client = ApiClient(configuration)
        self.benefits_country_summary: BenefitsCountrySummaryApi = BenefitsCountrySummaryApi(api_client)
        self.billing_documents: BillingDocumentsApi = BillingDocumentsApi(api_client)
        self.companies: CompaniesApi = CompaniesApi(api_client)
        self.company_department: CompanyDepartmentApi = CompanyDepartmentApi(api_client)
        self.company_managers: CompanyManagersApi = CompanyManagersApi(api_client)
        self.contract_amendments: ContractAmendmentsApi = ContractAmendmentsApi(api_client)
        self.cost_calculator: CostCalculatorApi = CostCalculatorApi(api_client)
        self.countries: CountriesApi = CountriesApi(api_client)
        self.custom_fields: CustomFieldsApi = CustomFieldsApi(api_client)
        self.employment_contracts: EmploymentContractsApi = EmploymentContractsApi(api_client)
        self.employments: EmploymentsApi = EmploymentsApi(api_client)
        self.expenses: ExpensesApi = ExpensesApi(api_client)
        self.files: FilesApi = FilesApi(api_client)
        self.identity: IdentityApi = IdentityApi(api_client)
        self.incentives: IncentivesApi = IncentivesApi(api_client)
        self.o_auth2: OAuth2Api = OAuth2Api(api_client)
        self.offboarding: OffboardingApi = OffboardingApi(api_client)
        self.payslips: PayslipsApi = PayslipsApi(api_client)
        self.recurring_incentives: RecurringIncentivesApi = RecurringIncentivesApi(api_client)
        self.resignation: ResignationApi = ResignationApi(api_client)
        self.sandbox: SandboxApi = SandboxApi(api_client)
        self.time_off: TimeOffApi = TimeOffApi(api_client)
        self.time_off_balances: TimeOffBalancesApi = TimeOffBalancesApi(api_client)
        self.webhook_callbacks: WebhookCallbacksApi = WebhookCallbacksApi(api_client)