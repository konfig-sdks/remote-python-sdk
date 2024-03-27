operation_parameter_map = {
    '/v1/benefits/country-summary-GET': {
        'parameters': [
        ]
    },
    '/v1/billing-documents/{billing_document_id}/pdf-GET': {
        'parameters': [
            {
                'name': 'billing_document_id'
            },
        ]
    },
    '/v1/billing-documents-GET': {
        'parameters': [
            {
                'name': 'period'
            },
            {
                'name': 'page'
            },
            {
                'name': 'page_size'
            },
        ]
    },
    '/v1/billing-documents/{billing_document_id}-GET': {
        'parameters': [
            {
                'name': 'billing_document_id'
            },
        ]
    },
    '/v1/companies-POST': {
        'parameters': [
            {
                'name': 'company_owner_email'
            },
            {
                'name': 'company_owner_name'
            },
            {
                'name': 'country_code'
            },
            {
                'name': 'desired_currency'
            },
            {
                'name': 'name'
            },
            {
                'name': 'terms_of_service_accepted_at'
            },
            {
                'name': 'address_details'
            },
            {
                'name': 'bank_account_details'
            },
            {
                'name': 'email_domain'
            },
            {
                'name': 'external_id'
            },
            {
                'name': 'phone_number'
            },
            {
                'name': 'registration_number'
            },
            {
                'name': 'tax_number'
            },
            {
                'name': 'action'
            },
        ]
    },
    '/v1/companies-GET': {
        'parameters': [
        ]
    },
    '/v1/companies/{company_id}-GET': {
        'parameters': [
            {
                'name': 'company_id'
            },
        ]
    },
    '/v1/companies/{company_id}-PUT': {
        'parameters': [
            {
                'name': 'company_id'
            },
            {
                'name': 'address_details'
            },
            {
                'name': 'bank_account_details'
            },
            {
                'name': 'country_code'
            },
            {
                'name': 'desired_currency'
            },
            {
                'name': 'name'
            },
            {
                'name': 'phone_number'
            },
            {
                'name': 'registration_number'
            },
            {
                'name': 'tax_number'
            },
        ]
    },
    '/v1/companies/{company_id}-PATCH': {
        'parameters': [
            {
                'name': 'company_id'
            },
            {
                'name': 'address_details'
            },
            {
                'name': 'bank_account_details'
            },
            {
                'name': 'country_code'
            },
            {
                'name': 'desired_currency'
            },
            {
                'name': 'name'
            },
            {
                'name': 'phone_number'
            },
            {
                'name': 'registration_number'
            },
            {
                'name': 'tax_number'
            },
        ]
    },
    '/v1/company-departments-POST': {
        'parameters': [
            {
                'name': 'company_id'
            },
            {
                'name': 'name'
            },
        ]
    },
    '/v1/company-departments-GET': {
        'parameters': [
            {
                'name': 'company_id'
            },
            {
                'name': 'paginate'
            },
            {
                'name': 'page'
            },
            {
                'name': 'page_size'
            },
        ]
    },
    '/v1/company-managers-POST': {
        'parameters': [
            {
                'name': 'email'
            },
            {
                'name': 'name'
            },
            {
                'name': 'role'
            },
            {
                'name': 'company_id'
            },
        ]
    },
    '/v1/company-managers/{user_id}-DELETE': {
        'parameters': [
            {
                'name': 'user_id'
            },
        ]
    },
    '/v1/company-managers-GET': {
        'parameters': [
            {
                'name': 'company_id'
            },
            {
                'name': 'page'
            },
            {
                'name': 'page_size'
            },
        ]
    },
    '/v1/company-managers/{user_id}-GET': {
        'parameters': [
            {
                'name': 'user_id'
            },
        ]
    },
    '/v1/sandbox/contract-amendments/{contract_amendment_request_id}/approve-PUT': {
        'parameters': [
            {
                'name': 'contract_amendment_request_id'
            },
        ]
    },
    '/v1/contract-amendments/automatable-POST': {
        'parameters': [
            {
                'name': 'amendment_contract_id'
            },
            {
                'name': 'contract_amendment'
            },
            {
                'name': 'employment_id'
            },
        ]
    },
    '/v1/contract-amendments-POST': {
        'parameters': [
            {
                'name': 'amendment_contract_id'
            },
            {
                'name': 'contract_amendment'
            },
            {
                'name': 'employment_id'
            },
        ]
    },
    '/v1/contract-amendments/schema-POST': {
        'parameters': [
            {
                'name': 'country_code'
            },
            {
                'name': 'employment_id'
            },
            {
                'name': 'form'
            },
        ]
    },
    '/v1/contract-amendments-GET': {
        'parameters': [
        ]
    },
    '/v1/contract-amendments/{id}-GET': {
        'parameters': [
            {
                'name': 'id'
            },
        ]
    },
    '/v1/cost-calculator/estimation-POST': {
        'parameters': [
            {
                'name': 'employer_currency_slug'
            },
            {
                'name': 'employments'
            },
            {
                'name': 'include_benefits'
            },
            {
                'name': 'include_cost_breakdowns'
            },
        ]
    },
    '/v1/cost-calculator/estimation-pdf-POST': {
        'parameters': [
            {
                'name': 'employer_currency_slug'
            },
            {
                'name': 'employments'
            },
            {
                'name': 'include_benefits'
            },
            {
                'name': 'include_cost_breakdowns'
            },
        ]
    },
    '/v1/cost-calculator/countries-GET': {
        'parameters': [
        ]
    },
    '/v1/cost-calculator/regions/{slug}/fields-GET': {
        'parameters': [
            {
                'name': 'slug'
            },
        ]
    },
    '/v1/countries/{country_code}/{form}-GET': {
        'parameters': [
            {
                'name': 'country_code'
            },
            {
                'name': 'form'
            },
            {
                'name': 'employment_id'
            },
        ]
    },
    '/v1/countries-GET': {
        'parameters': [
        ]
    },
    '/v1/countries/{country_code}/holidays/{year}-GET': {
        'parameters': [
            {
                'name': 'country_code'
            },
            {
                'name': 'year'
            },
            {
                'name': 'country_subdivision_code'
            },
        ]
    },
    '/v1/custom-fields-GET': {
        'parameters': [
            {
                'name': 'page'
            },
            {
                'name': 'page_size'
            },
        ]
    },
    '/v1/custom-fields/{custom_field_id}/values/{employment_id}-GET': {
        'parameters': [
            {
                'name': 'custom_field_id'
            },
            {
                'name': 'employment_id'
            },
        ]
    },
    '/v1/employment-contracts/{employment_id}/pending-changes-GET': {
        'parameters': [
            {
                'name': 'employment_id'
            },
        ]
    },
    '/v1/ready-POST': {
        'parameters': [
            {
                'name': 'employment_id'
            },
        ]
    },
    '/v1/employments-POST': {
        'parameters': [
            {
                'name': 'country_code'
            },
            {
                'name': 'full_name'
            },
            {
                'name': 'job_title'
            },
            {
                'name': 'personal_email'
            },
            {
                'name': 'basic_information'
            },
            {
                'name': 'company_id'
            },
            {
                'name': 'type'
            },
            {
                'name': 'provisional_start_date'
            },
            {
                'name': 'seniority_date'
            },
        ]
    },
    '/v1/employments/{employment_id}-GET': {
        'parameters': [
            {
                'name': 'employment_id'
            },
        ]
    },
    '/v1/employments/{employment_id}/invite-POST': {
        'parameters': [
            {
                'name': 'employment_id'
            },
        ]
    },
    '/v1/employments-GET': {
        'parameters': [
            {
                'name': 'company_id'
            },
            {
                'name': 'email'
            },
            {
                'name': 'status'
            },
            {
                'name': 'page'
            },
            {
                'name': 'page_size'
            },
        ]
    },
    '/v1/employments/{employment_id}-PATCH': {
        'parameters': [
            {
                'name': 'full_name'
            },
            {
                'name': 'job_title'
            },
            {
                'name': 'personal_email'
            },
            {
                'name': 'employment_id'
            },
            {
                'name': 'address_details'
            },
            {
                'name': 'administrative_details'
            },
            {
                'name': 'bank_account_details'
            },
            {
                'name': 'billing_address_details'
            },
            {
                'name': 'company_id'
            },
            {
                'name': 'contract_details'
            },
            {
                'name': 'country'
            },
            {
                'name': 'emergency_contact_details'
            },
            {
                'name': 'manager_id'
            },
            {
                'name': 'personal_details'
            },
            {
                'name': 'pricing_plan_details'
            },
            {
                'name': 'provisional_start_date'
            },
            {
                'name': 'seniority_date'
            },
            {
                'name': 'basic_information'
            },
            {
                'name': 'department_id'
            },
        ]
    },
    '/v1/employments/{employment_id}-PUT': {
        'parameters': [
            {
                'name': 'full_name'
            },
            {
                'name': 'job_title'
            },
            {
                'name': 'personal_email'
            },
            {
                'name': 'employment_id'
            },
            {
                'name': 'address_details'
            },
            {
                'name': 'administrative_details'
            },
            {
                'name': 'bank_account_details'
            },
            {
                'name': 'billing_address_details'
            },
            {
                'name': 'company_id'
            },
            {
                'name': 'contract_details'
            },
            {
                'name': 'country'
            },
            {
                'name': 'emergency_contact_details'
            },
            {
                'name': 'manager_id'
            },
            {
                'name': 'personal_details'
            },
            {
                'name': 'pricing_plan_details'
            },
            {
                'name': 'provisional_start_date'
            },
            {
                'name': 'seniority_date'
            },
            {
                'name': 'basic_information'
            },
            {
                'name': 'department_id'
            },
        ]
    },
    '/v1/expenses-POST': {
        'parameters': [
            {
                'name': 'title'
            },
            {
                'name': 'amount'
            },
            {
                'name': 'currency'
            },
            {
                'name': 'employment_id'
            },
            {
                'name': 'expense_date'
            },
            {
                'name': 'category'
            },
            {
                'name': 'receipt'
            },
            {
                'name': 'receipts'
            },
            {
                'name': 'reviewed_at'
            },
            {
                'name': 'reviewer_id'
            },
            {
                'name': 'tax_amount'
            },
            {
                'name': 'timezone'
            },
        ]
    },
    '/v1/expenses/{expense_id}/receipt-GET': {
        'parameters': [
            {
                'name': 'expense_id'
            },
        ]
    },
    '/v1/expenses/{expense_id}/receipts/{receipt_id}-GET': {
        'parameters': [
            {
                'name': 'expense_id'
            },
            {
                'name': 'receipt_id'
            },
        ]
    },
    '/v1/expenses-GET': {
        'parameters': [
            {
                'name': 'page'
            },
            {
                'name': 'page_size'
            },
        ]
    },
    '/v1/expenses/{id}-GET': {
        'parameters': [
            {
                'name': 'id'
            },
        ]
    },
    '/v1/expenses/{id}-PUT': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'status'
            },
            {
                'name': 'reason'
            },
        ]
    },
    '/v1/expenses/{id}-PATCH': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'status'
            },
            {
                'name': 'reason'
            },
        ]
    },
    '/v1/files/{id}-GET': {
        'parameters': [
            {
                'name': 'id'
            },
        ]
    },
    '/v1/documents-POST': {
        'parameters': [
            {
                'name': 'employment_id'
            },
            {
                'name': 'file'
            },
            {
                'name': 'type'
            },
        ]
    },
    '/v1/identity/current-GET': {
        'parameters': [
        ]
    },
    '/v1/incentives-POST': {
        'parameters': [
            {
                'name': 'amount'
            },
            {
                'name': 'amount_tax_type'
            },
            {
                'name': 'effective_date'
            },
            {
                'name': 'employment_id'
            },
            {
                'name': 'type'
            },
            {
                'name': 'note'
            },
        ]
    },
    '/v1/incentives-GET': {
        'parameters': [
            {
                'name': 'employment_id'
            },
            {
                'name': 'status'
            },
            {
                'name': 'recurring_incentive_id'
            },
            {
                'name': 'page'
            },
            {
                'name': 'page_size'
            },
        ]
    },
    '/v1/incentives/{id}-DELETE': {
        'parameters': [
            {
                'name': 'id'
            },
        ]
    },
    '/v1/incentives/{id}-GET': {
        'parameters': [
            {
                'name': 'id'
            },
        ]
    },
    '/v1/incentives/{id}-PUT': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'amount'
            },
            {
                'name': 'amount_tax_type'
            },
            {
                'name': 'effective_date'
            },
            {
                'name': 'note'
            },
            {
                'name': 'type'
            },
        ]
    },
    '/v1/incentives/{id}-PATCH': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'amount'
            },
            {
                'name': 'amount_tax_type'
            },
            {
                'name': 'effective_date'
            },
            {
                'name': 'note'
            },
            {
                'name': 'type'
            },
        ]
    },
    '/auth/oauth2/token-POST': {
        'parameters': [
            {
                'name': 'code'
            },
            {
                'name': 'grant_type'
            },
            {
                'name': 'client_id'
            },
            {
                'name': 'refresh_token'
            },
        ]
    },
    '/v1/offboardings-POST': {
        'parameters': [
            {
                'name': 'employment_id'
            },
            {
                'name': 'termination_details'
            },
            {
                'name': 'type'
            },
        ]
    },
    '/v1/offboardings-GET': {
        'parameters': [
            {
                'name': 'employment_id'
            },
            {
                'name': 'type'
            },
            {
                'name': 'include_confidential'
            },
            {
                'name': 'page'
            },
            {
                'name': 'page_size'
            },
        ]
    },
    '/v1/offboardings/{id}-GET': {
        'parameters': [
            {
                'name': 'id'
            },
        ]
    },
    '/v1/payslips/{payslip_id}/pdf-GET': {
        'parameters': [
            {
                'name': 'payslip_id'
            },
        ]
    },
    '/v1/payslips-GET': {
        'parameters': [
            {
                'name': 'employment_id'
            },
            {
                'name': 'start_date'
            },
            {
                'name': 'end_date'
            },
            {
                'name': 'expected_payout_start_date'
            },
            {
                'name': 'expected_payout_end_date'
            },
            {
                'name': 'page'
            },
            {
                'name': 'page_size'
            },
        ]
    },
    '/v1/payslips/{id}-GET': {
        'parameters': [
            {
                'name': 'id'
            },
        ]
    },
    '/v1/incentives/recurring-POST': {
        'parameters': [
            {
                'name': 'amount'
            },
            {
                'name': 'amount_tax_type'
            },
            {
                'name': 'effective_date'
            },
            {
                'name': 'employment_id'
            },
            {
                'name': 'type'
            },
            {
                'name': 'note'
            },
            {
                'name': 'duration_in_months'
            },
        ]
    },
    '/v1/incentives/recurring/{id}-DELETE': {
        'parameters': [
            {
                'name': 'id'
            },
        ]
    },
    '/v1/incentives/recurring-GET': {
        'parameters': [
            {
                'name': 'status'
            },
            {
                'name': 'type'
            },
            {
                'name': 'note'
            },
            {
                'name': 'page'
            },
            {
                'name': 'page_size'
            },
        ]
    },
    '/v1/resignations/{employment_request_id}/resignation-letter-GET': {
        'parameters': [
            {
                'name': 'employment_request_id'
            },
        ]
    },
    '/v1/sandbox/employments-POST': {
        'parameters': [
            {
                'name': 'country_code'
            },
            {
                'name': 'full_name'
            },
            {
                'name': 'job_title'
            },
            {
                'name': 'personal_email'
            },
            {
                'name': 'basic_information'
            },
            {
                'name': 'company_id'
            },
            {
                'name': 'type'
            },
            {
                'name': 'provisional_start_date'
            },
            {
                'name': 'seniority_date'
            },
        ]
    },
    '/v1/sandbox/employments/{employment_id}-PUT': {
        'parameters': [
            {
                'name': 'employment_id'
            },
            {
                'name': 'status'
            },
        ]
    },
    '/v1/sandbox/webhook-callbacks/trigger-POST': {
        'parameters': [
            {
                'name': 'employment_id'
            },
            {
                'name': 'event_type'
            },
        ]
    },
    '/v1/sandbox/employments/{employment_id}-PATCH': {
        'parameters': [
            {
                'name': 'employment_id'
            },
            {
                'name': 'status'
            },
        ]
    },
    '/v1/timeoff/{id}-GET': {
        'parameters': [
            {
                'name': 'id'
            },
        ]
    },
    '/v1/timeoff-GET': {
        'parameters': [
            {
                'name': 'employment_id'
            },
            {
                'name': 'timeoff_type'
            },
            {
                'name': 'status'
            },
            {
                'name': 'order'
            },
            {
                'name': 'sort_by'
            },
            {
                'name': 'page'
            },
            {
                'name': 'page_size'
            },
        ]
    },
    '/v1/timeoff/types-GET': {
        'parameters': [
        ]
    },
    '/v1/timeoff-POST': {
        'parameters': [
            {
                'name': 'approved_at'
            },
            {
                'name': 'approver_id'
            },
            {
                'name': 'status'
            },
            {
                'name': 'document'
            },
            {
                'name': 'employment_id'
            },
            {
                'name': 'end_date'
            },
            {
                'name': 'notes'
            },
            {
                'name': 'start_date'
            },
            {
                'name': 'timeoff_days'
            },
            {
                'name': 'timeoff_type'
            },
            {
                'name': 'timezone'
            },
        ]
    },
    '/v1/timeoff/{id}-PUT': {
        'parameters': [
            {
                'name': 'cancel_reason'
            },
            {
                'name': 'edit_reason'
            },
            {
                'name': 'id'
            },
            {
                'name': 'approved_at'
            },
            {
                'name': 'approver_id'
            },
            {
                'name': 'document'
            },
            {
                'name': 'end_date'
            },
            {
                'name': 'notes'
            },
            {
                'name': 'start_date'
            },
            {
                'name': 'status'
            },
            {
                'name': 'timeoff_days'
            },
            {
                'name': 'timeoff_type'
            },
            {
                'name': 'timezone'
            },
        ]
    },
    '/v1/timeoff/{id}-PATCH': {
        'parameters': [
            {
                'name': 'cancel_reason'
            },
            {
                'name': 'edit_reason'
            },
            {
                'name': 'id'
            },
            {
                'name': 'approved_at'
            },
            {
                'name': 'approver_id'
            },
            {
                'name': 'document'
            },
            {
                'name': 'end_date'
            },
            {
                'name': 'notes'
            },
            {
                'name': 'start_date'
            },
            {
                'name': 'status'
            },
            {
                'name': 'timeoff_days'
            },
            {
                'name': 'timeoff_type'
            },
            {
                'name': 'timezone'
            },
        ]
    },
    '/v1/timeoff-balances/{employment_id}-GET': {
        'parameters': [
            {
                'name': 'employment_id'
            },
        ]
    },
    '/v1/webhook-callbacks/{id}-DELETE': {
        'parameters': [
            {
                'name': 'id'
            },
        ]
    },
    '/v1/webhook-callbacks-POST': {
        'parameters': [
            {
                'name': 'url'
            },
            {
                'name': 'subscribed_events'
            },
        ]
    },
};