import typing_extensions

from remote_python_sdk.paths import PathValues
from remote_python_sdk.apis.paths.v1_contract_amendments import V1ContractAmendments
from remote_python_sdk.apis.paths.v1_timeoff_id import V1TimeoffId
from remote_python_sdk.apis.paths.v1_incentives import V1Incentives
from remote_python_sdk.apis.paths.v1_custom_fields import V1CustomFields
from remote_python_sdk.apis.paths.v1_cost_calculator_estimation_pdf import V1CostCalculatorEstimationPdf
from remote_python_sdk.apis.paths.v1_incentives_id import V1IncentivesId
from remote_python_sdk.apis.paths.v1_payslips import V1Payslips
from remote_python_sdk.apis.paths.auth_oauth2_token import AuthOauth2Token
from remote_python_sdk.apis.paths.v1_employment_contracts_employment_id_pending_changes import V1EmploymentContractsEmploymentIdPendingChanges
from remote_python_sdk.apis.paths.v1_timeoff import V1Timeoff
from remote_python_sdk.apis.paths.v1_employments_employment_id import V1EmploymentsEmploymentId
from remote_python_sdk.apis.paths.v1_payslips_id import V1PayslipsId
from remote_python_sdk.apis.paths.v1_incentives_recurring_id import V1IncentivesRecurringId
from remote_python_sdk.apis.paths.v1_sandbox_employments_employment_id import V1SandboxEmploymentsEmploymentId
from remote_python_sdk.apis.paths.v1_resignations_employment_request_id_resignation_letter import V1ResignationsEmploymentRequestIdResignationLetter
from remote_python_sdk.apis.paths.v1_expenses import V1Expenses
from remote_python_sdk.apis.paths.v1_company_departments import V1CompanyDepartments
from remote_python_sdk.apis.paths.v1_expenses_id import V1ExpensesId
from remote_python_sdk.apis.paths.v1_benefits_country_summary import V1BenefitsCountrySummary
from remote_python_sdk.apis.paths.v1_company_managers import V1CompanyManagers
from remote_python_sdk.apis.paths.v1_payslips_payslip_id_pdf import V1PayslipsPayslipIdPdf
from remote_python_sdk.apis.paths.v1_identity_current import V1IdentityCurrent
from remote_python_sdk.apis.paths.v1_files_id import V1FilesId
from remote_python_sdk.apis.paths.v1_offboardings import V1Offboardings
from remote_python_sdk.apis.paths.v1_company_managers_user_id import V1CompanyManagersUserId
from remote_python_sdk.apis.paths.v1_custom_fields_custom_field_id_values_employment_id import V1CustomFieldsCustomFieldIdValuesEmploymentId
from remote_python_sdk.apis.paths.v1_contract_amendments_id import V1ContractAmendmentsId
from remote_python_sdk.apis.paths.v1_companies import V1Companies
from remote_python_sdk.apis.paths.v1_contract_amendments_automatable import V1ContractAmendmentsAutomatable
from remote_python_sdk.apis.paths.v1_sandbox_employments import V1SandboxEmployments
from remote_python_sdk.apis.paths.v1_contract_amendments_schema import V1ContractAmendmentsSchema
from remote_python_sdk.apis.paths.v1_billing_documents import V1BillingDocuments
from remote_python_sdk.apis.paths.v1_incentives_recurring import V1IncentivesRecurring
from remote_python_sdk.apis.paths.v1_countries import V1Countries
from remote_python_sdk.apis.paths.v1_cost_calculator_regions_slug_fields import V1CostCalculatorRegionsSlugFields
from remote_python_sdk.apis.paths.v1_webhook_callbacks_id import V1WebhookCallbacksId
from remote_python_sdk.apis.paths.v1_countries_country_code_holidays_year import V1CountriesCountryCodeHolidaysYear
from remote_python_sdk.apis.paths.v1_billing_documents_billing_document_id_pdf import V1BillingDocumentsBillingDocumentIdPdf
from remote_python_sdk.apis.paths.v1_documents import V1Documents
from remote_python_sdk.apis.paths.v1_webhook_callbacks import V1WebhookCallbacks
from remote_python_sdk.apis.paths.v1_cost_calculator_estimation import V1CostCalculatorEstimation
from remote_python_sdk.apis.paths.v1_expenses_expense_id_receipt import V1ExpensesExpenseIdReceipt
from remote_python_sdk.apis.paths.v1_employments_employment_id_invite import V1EmploymentsEmploymentIdInvite
from remote_python_sdk.apis.paths.v1_timeoff_balances_employment_id import V1TimeoffBalancesEmploymentId
from remote_python_sdk.apis.paths.v1_billing_documents_billing_document_id import V1BillingDocumentsBillingDocumentId
from remote_python_sdk.apis.paths.v1_expenses_expense_id_receipts_receipt_id import V1ExpensesExpenseIdReceiptsReceiptId
from remote_python_sdk.apis.paths.v1_employments import V1Employments
from remote_python_sdk.apis.paths.v1_cost_calculator_countries import V1CostCalculatorCountries
from remote_python_sdk.apis.paths.v1_offboardings_id import V1OffboardingsId
from remote_python_sdk.apis.paths.v1_sandbox_webhook_callbacks_trigger import V1SandboxWebhookCallbacksTrigger
from remote_python_sdk.apis.paths.v1_timeoff_types import V1TimeoffTypes
from remote_python_sdk.apis.paths.v1_companies_company_id import V1CompaniesCompanyId
from remote_python_sdk.apis.paths.v1_ready import V1Ready
from remote_python_sdk.apis.paths.v1_sandbox_contract_amendments_contract_amendment_request_id_approve import V1SandboxContractAmendmentsContractAmendmentRequestIdApprove
from remote_python_sdk.apis.paths.v1_countries_country_code_form import V1CountriesCountryCodeForm

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.V1_CONTRACTAMENDMENTS: V1ContractAmendments,
        PathValues.V1_TIMEOFF_ID: V1TimeoffId,
        PathValues.V1_INCENTIVES: V1Incentives,
        PathValues.V1_CUSTOMFIELDS: V1CustomFields,
        PathValues.V1_COSTCALCULATOR_ESTIMATIONPDF: V1CostCalculatorEstimationPdf,
        PathValues.V1_INCENTIVES_ID: V1IncentivesId,
        PathValues.V1_PAYSLIPS: V1Payslips,
        PathValues.AUTH_OAUTH2_TOKEN: AuthOauth2Token,
        PathValues.V1_EMPLOYMENTCONTRACTS_EMPLOYMENT_ID_PENDINGCHANGES: V1EmploymentContractsEmploymentIdPendingChanges,
        PathValues.V1_TIMEOFF: V1Timeoff,
        PathValues.V1_EMPLOYMENTS_EMPLOYMENT_ID: V1EmploymentsEmploymentId,
        PathValues.V1_PAYSLIPS_ID: V1PayslipsId,
        PathValues.V1_INCENTIVES_RECURRING_ID: V1IncentivesRecurringId,
        PathValues.V1_SANDBOX_EMPLOYMENTS_EMPLOYMENT_ID: V1SandboxEmploymentsEmploymentId,
        PathValues.V1_RESIGNATIONS_EMPLOYMENT_REQUEST_ID_RESIGNATIONLETTER: V1ResignationsEmploymentRequestIdResignationLetter,
        PathValues.V1_EXPENSES: V1Expenses,
        PathValues.V1_COMPANYDEPARTMENTS: V1CompanyDepartments,
        PathValues.V1_EXPENSES_ID: V1ExpensesId,
        PathValues.V1_BENEFITS_COUNTRYSUMMARY: V1BenefitsCountrySummary,
        PathValues.V1_COMPANYMANAGERS: V1CompanyManagers,
        PathValues.V1_PAYSLIPS_PAYSLIP_ID_PDF: V1PayslipsPayslipIdPdf,
        PathValues.V1_IDENTITY_CURRENT: V1IdentityCurrent,
        PathValues.V1_FILES_ID: V1FilesId,
        PathValues.V1_OFFBOARDINGS: V1Offboardings,
        PathValues.V1_COMPANYMANAGERS_USER_ID: V1CompanyManagersUserId,
        PathValues.V1_CUSTOMFIELDS_CUSTOM_FIELD_ID_VALUES_EMPLOYMENT_ID: V1CustomFieldsCustomFieldIdValuesEmploymentId,
        PathValues.V1_CONTRACTAMENDMENTS_ID: V1ContractAmendmentsId,
        PathValues.V1_COMPANIES: V1Companies,
        PathValues.V1_CONTRACTAMENDMENTS_AUTOMATABLE: V1ContractAmendmentsAutomatable,
        PathValues.V1_SANDBOX_EMPLOYMENTS: V1SandboxEmployments,
        PathValues.V1_CONTRACTAMENDMENTS_SCHEMA: V1ContractAmendmentsSchema,
        PathValues.V1_BILLINGDOCUMENTS: V1BillingDocuments,
        PathValues.V1_INCENTIVES_RECURRING: V1IncentivesRecurring,
        PathValues.V1_COUNTRIES: V1Countries,
        PathValues.V1_COSTCALCULATOR_REGIONS_SLUG_FIELDS: V1CostCalculatorRegionsSlugFields,
        PathValues.V1_WEBHOOKCALLBACKS_ID: V1WebhookCallbacksId,
        PathValues.V1_COUNTRIES_COUNTRY_CODE_HOLIDAYS_YEAR: V1CountriesCountryCodeHolidaysYear,
        PathValues.V1_BILLINGDOCUMENTS_BILLING_DOCUMENT_ID_PDF: V1BillingDocumentsBillingDocumentIdPdf,
        PathValues.V1_DOCUMENTS: V1Documents,
        PathValues.V1_WEBHOOKCALLBACKS: V1WebhookCallbacks,
        PathValues.V1_COSTCALCULATOR_ESTIMATION: V1CostCalculatorEstimation,
        PathValues.V1_EXPENSES_EXPENSE_ID_RECEIPT: V1ExpensesExpenseIdReceipt,
        PathValues.V1_EMPLOYMENTS_EMPLOYMENT_ID_INVITE: V1EmploymentsEmploymentIdInvite,
        PathValues.V1_TIMEOFFBALANCES_EMPLOYMENT_ID: V1TimeoffBalancesEmploymentId,
        PathValues.V1_BILLINGDOCUMENTS_BILLING_DOCUMENT_ID: V1BillingDocumentsBillingDocumentId,
        PathValues.V1_EXPENSES_EXPENSE_ID_RECEIPTS_RECEIPT_ID: V1ExpensesExpenseIdReceiptsReceiptId,
        PathValues.V1_EMPLOYMENTS: V1Employments,
        PathValues.V1_COSTCALCULATOR_COUNTRIES: V1CostCalculatorCountries,
        PathValues.V1_OFFBOARDINGS_ID: V1OffboardingsId,
        PathValues.V1_SANDBOX_WEBHOOKCALLBACKS_TRIGGER: V1SandboxWebhookCallbacksTrigger,
        PathValues.V1_TIMEOFF_TYPES: V1TimeoffTypes,
        PathValues.V1_COMPANIES_COMPANY_ID: V1CompaniesCompanyId,
        PathValues.V1_READY: V1Ready,
        PathValues.V1_SANDBOX_CONTRACTAMENDMENTS_CONTRACT_AMENDMENT_REQUEST_ID_APPROVE: V1SandboxContractAmendmentsContractAmendmentRequestIdApprove,
        PathValues.V1_COUNTRIES_COUNTRY_CODE_FORM: V1CountriesCountryCodeForm,
    }
)

path_to_api = PathToApi(
    {
        PathValues.V1_CONTRACTAMENDMENTS: V1ContractAmendments,
        PathValues.V1_TIMEOFF_ID: V1TimeoffId,
        PathValues.V1_INCENTIVES: V1Incentives,
        PathValues.V1_CUSTOMFIELDS: V1CustomFields,
        PathValues.V1_COSTCALCULATOR_ESTIMATIONPDF: V1CostCalculatorEstimationPdf,
        PathValues.V1_INCENTIVES_ID: V1IncentivesId,
        PathValues.V1_PAYSLIPS: V1Payslips,
        PathValues.AUTH_OAUTH2_TOKEN: AuthOauth2Token,
        PathValues.V1_EMPLOYMENTCONTRACTS_EMPLOYMENT_ID_PENDINGCHANGES: V1EmploymentContractsEmploymentIdPendingChanges,
        PathValues.V1_TIMEOFF: V1Timeoff,
        PathValues.V1_EMPLOYMENTS_EMPLOYMENT_ID: V1EmploymentsEmploymentId,
        PathValues.V1_PAYSLIPS_ID: V1PayslipsId,
        PathValues.V1_INCENTIVES_RECURRING_ID: V1IncentivesRecurringId,
        PathValues.V1_SANDBOX_EMPLOYMENTS_EMPLOYMENT_ID: V1SandboxEmploymentsEmploymentId,
        PathValues.V1_RESIGNATIONS_EMPLOYMENT_REQUEST_ID_RESIGNATIONLETTER: V1ResignationsEmploymentRequestIdResignationLetter,
        PathValues.V1_EXPENSES: V1Expenses,
        PathValues.V1_COMPANYDEPARTMENTS: V1CompanyDepartments,
        PathValues.V1_EXPENSES_ID: V1ExpensesId,
        PathValues.V1_BENEFITS_COUNTRYSUMMARY: V1BenefitsCountrySummary,
        PathValues.V1_COMPANYMANAGERS: V1CompanyManagers,
        PathValues.V1_PAYSLIPS_PAYSLIP_ID_PDF: V1PayslipsPayslipIdPdf,
        PathValues.V1_IDENTITY_CURRENT: V1IdentityCurrent,
        PathValues.V1_FILES_ID: V1FilesId,
        PathValues.V1_OFFBOARDINGS: V1Offboardings,
        PathValues.V1_COMPANYMANAGERS_USER_ID: V1CompanyManagersUserId,
        PathValues.V1_CUSTOMFIELDS_CUSTOM_FIELD_ID_VALUES_EMPLOYMENT_ID: V1CustomFieldsCustomFieldIdValuesEmploymentId,
        PathValues.V1_CONTRACTAMENDMENTS_ID: V1ContractAmendmentsId,
        PathValues.V1_COMPANIES: V1Companies,
        PathValues.V1_CONTRACTAMENDMENTS_AUTOMATABLE: V1ContractAmendmentsAutomatable,
        PathValues.V1_SANDBOX_EMPLOYMENTS: V1SandboxEmployments,
        PathValues.V1_CONTRACTAMENDMENTS_SCHEMA: V1ContractAmendmentsSchema,
        PathValues.V1_BILLINGDOCUMENTS: V1BillingDocuments,
        PathValues.V1_INCENTIVES_RECURRING: V1IncentivesRecurring,
        PathValues.V1_COUNTRIES: V1Countries,
        PathValues.V1_COSTCALCULATOR_REGIONS_SLUG_FIELDS: V1CostCalculatorRegionsSlugFields,
        PathValues.V1_WEBHOOKCALLBACKS_ID: V1WebhookCallbacksId,
        PathValues.V1_COUNTRIES_COUNTRY_CODE_HOLIDAYS_YEAR: V1CountriesCountryCodeHolidaysYear,
        PathValues.V1_BILLINGDOCUMENTS_BILLING_DOCUMENT_ID_PDF: V1BillingDocumentsBillingDocumentIdPdf,
        PathValues.V1_DOCUMENTS: V1Documents,
        PathValues.V1_WEBHOOKCALLBACKS: V1WebhookCallbacks,
        PathValues.V1_COSTCALCULATOR_ESTIMATION: V1CostCalculatorEstimation,
        PathValues.V1_EXPENSES_EXPENSE_ID_RECEIPT: V1ExpensesExpenseIdReceipt,
        PathValues.V1_EMPLOYMENTS_EMPLOYMENT_ID_INVITE: V1EmploymentsEmploymentIdInvite,
        PathValues.V1_TIMEOFFBALANCES_EMPLOYMENT_ID: V1TimeoffBalancesEmploymentId,
        PathValues.V1_BILLINGDOCUMENTS_BILLING_DOCUMENT_ID: V1BillingDocumentsBillingDocumentId,
        PathValues.V1_EXPENSES_EXPENSE_ID_RECEIPTS_RECEIPT_ID: V1ExpensesExpenseIdReceiptsReceiptId,
        PathValues.V1_EMPLOYMENTS: V1Employments,
        PathValues.V1_COSTCALCULATOR_COUNTRIES: V1CostCalculatorCountries,
        PathValues.V1_OFFBOARDINGS_ID: V1OffboardingsId,
        PathValues.V1_SANDBOX_WEBHOOKCALLBACKS_TRIGGER: V1SandboxWebhookCallbacksTrigger,
        PathValues.V1_TIMEOFF_TYPES: V1TimeoffTypes,
        PathValues.V1_COMPANIES_COMPANY_ID: V1CompaniesCompanyId,
        PathValues.V1_READY: V1Ready,
        PathValues.V1_SANDBOX_CONTRACTAMENDMENTS_CONTRACT_AMENDMENT_REQUEST_ID_APPROVE: V1SandboxContractAmendmentsContractAmendmentRequestIdApprove,
        PathValues.V1_COUNTRIES_COUNTRY_CODE_FORM: V1CountriesCountryCodeForm,
    }
)
