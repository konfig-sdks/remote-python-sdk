# coding: utf-8

"""
    Remote API

    Talent is everywhere. Opportunity is not. Remote's mission is to create opportunity everywhere, empowering employers to find and hire the best talent, and enabling individuals to build financial and personal freedom.   Remote is a Global HR Platform that helps companies hire, manage, and pay their entire team — and more effectively compete in the modern global economy through our comprehensive set of core solutions including, HRIS, payroll, international employment, contractor management, and more.   Whether you're just starting your global journey, or looking to optimize your existing operations, sign up or book a demo - and see how Remote makes global HR simple.

    The version of the OpenAPI document: 0.1.0
    Generated by: https://konfigthis.com
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal, TYPE_CHECKING
from pydantic import BaseModel, Field, RootModel, ConfigDict

from remote_python_sdk.pydantic.country import Country
from remote_python_sdk.pydantic.employment_bank_account_details import EmploymentBankAccountDetails
from remote_python_sdk.pydantic.employment_lifecycle_stage import EmploymentLifecycleStage
from remote_python_sdk.pydantic.employment_status import EmploymentStatus
from remote_python_sdk.pydantic.file import File
from remote_python_sdk.pydantic.onboarding_tasks import OnboardingTasks
from remote_python_sdk.pydantic.pricing_plan_details import PricingPlanDetails
from remote_python_sdk.pydantic.user_status import UserStatus

class Employment(BaseModel):
    # Home address information. Its properties may vary depending on the country.
    address_details: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(alias='address_details')

    # Administrative information. Its properties may vary depending on the country.
    administrative_details: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(alias='administrative_details')

    bank_account_details: EmploymentBankAccountDetails = Field(alias='bank_account_details')

    # Billing address information. Its properties may vary depending on the country.
    billing_address_details: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(alias='billing_address_details')

    company_id: str = Field(alias='company_id')

    # Contract information. Its properties may vary depending on the country.
    contract_details: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(alias='contract_details')

    country: Country = Field(alias='country')

    created_at: str = Field(alias='created_at')

    # Emergency contact information. Its properties may vary depending on the country.
    emergency_contact_details: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(alias='emergency_contact_details')

    employment_lifecycle_stage: EmploymentLifecycleStage = Field(alias='employment_lifecycle_stage')

    files: typing.List[File] = Field(alias='files')

    full_name: str = Field(alias='full_name')

    id: str = Field(alias='id')

    job_title: str = Field(alias='job_title')

    onboarding_tasks: OnboardingTasks = Field(alias='onboarding_tasks')

    # Personal details information. Its properties may vary depending on the country.
    personal_details: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(alias='personal_details')

    personal_email: str = Field(alias='personal_email')

    pricing_plan_details: PricingPlanDetails = Field(alias='pricing_plan_details')

    status: EmploymentStatus = Field(alias='status')

    # For the employment types `contractor`, `global_payroll_employee` and `direct_employee`, only [List employments](https://gateway.remote.com/v1/docs/openapi.html) and [Show employment](https://gateway.remote.com/v1/docs/openapi.html) operations are available. 
    type: Literal["employee", "contractor", "direct_employee", "global_payroll_employee"] = Field(alias='type')

    updated_at: datetime = Field(alias='updated_at')

    active_contract_id: typing.Optional[str] = Field(None, alias='active_contract_id')

    # Employment basic information. Its properties may vary depending on the country. 
    basic_information: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = Field(None, alias='basic_information')

    # Name of related department, if any. Otherwise, null.
    department: typing.Optional[typing.Optional[str]] = Field(None, alias='department')

    # Unique ID of related department, if any. Otherwise, null.
    department_id: typing.Optional[typing.Optional[str]] = Field(None, alias='department_id')

    manager: typing.Optional[str] = Field(None, alias='manager')

    probation_period_end_date: typing.Optional[date] = Field(None, alias='probation_period_end_date')

    # Indicates the expected start date of the employee or contractor.  Required for employees, but optional for contractors. Date format is in ISO8601 without the time component.  See the **Date and Time Format** documentation for more details on how the Remote API works with dates. 
    provisional_start_date: typing.Optional[date] = Field(None, alias='provisional_start_date')

    # The date the employee first started working for your company. If you don’t include a seniority date, the employee’s start date with Remote will be deemed as the start of the employee’s seniority.  **Example**: Your employee started working for your company on Feb 1, 2022. On Aug 1, 2022, you transferred the employee to Remote and started managing them on the platform. Feb 1, 2022 would be their seniority date. Aug 1, 2022 would be their starting date. 
    seniority_date: typing.Optional[datetime] = Field(None, alias='seniority_date')

    user_status: typing.Optional[UserStatus] = Field(None, alias='user_status')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
