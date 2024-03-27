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

from remote_python_sdk.type.country import Country
from remote_python_sdk.type.pricing_plan_details import PricingPlanDetails

class RequiredFullParams(TypedDict):
    pass

class OptionalFullParams(TypedDict, total=False):
    # Home address information. As its properties may vary depending on the country,                you must query the [Show form schema](https://gateway.remote.com/v1/docs/openapi.html) endpoint             passing the country code and `address_details` as path parameters.
    address_details: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]

    # Administrative information. As its properties may vary depending on the country,                you must query the [Show form schema](https://gateway.remote.com/v1/docs/openapi.html) endpoint             passing the country code and `administrative_details` as path parameters.
    administrative_details: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]

    # Bank account information. As its properties may vary depending on the country,                you must query the [Show form schema](https://gateway.remote.com/v1/docs/openapi.html) endpoint             passing the country code and `bank_account_details` as path parameters.
    bank_account_details: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]

    # Employment basic information. As its properties may vary depending on the country,                you must query the [Show form schema](https://gateway.remote.com/v1/docs/openapi.html) endpoint             passing the country code and `employment_basic_information` as path parameters.
    basic_information: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]

    # Billing address information. As its properties may vary depending on the country,                you must query the [Show form schema](https://gateway.remote.com/v1/docs/openapi.html) endpoint             passing the country code and `billing_address_details` as path parameters.
    billing_address_details: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]

    company_id: str

    # Contract information. As its properties may vary depending on the country,                you must query the [Show form schema](https://gateway.remote.com/v1/docs/openapi.html) endpoint             passing the country code and `contract_details` as path parameters.
    contract_details: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]

    country: Country

    # The department of the employment. The department must belong to the same company as the employment. 
    department_id: str

    # Emergency contact information. As its properties may vary depending on the country,                you must query the [Show form schema](https://gateway.remote.com/v1/docs/openapi.html) endpoint             passing the country code and `emergency_contact_details` as path parameters.
    emergency_contact_details: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]

    full_name: str

    job_title: str

    # The user id of the manager, who should have an `admin`, `owner` or `people_manager` role. You can find these users by querying the [Company Managers endpoint](https://gateway.remote.com/v1/docs/openapi.html). **Update of this field is only available for active employments.** 
    manager_id: str

    # Personal details information. As its properties may vary depending on the country,                you must query the [Show form schema](https://gateway.remote.com/v1/docs/openapi.html) endpoint             passing the country code and `personal_details` as path parameters.
    personal_details: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]

    pricing_plan_details: PricingPlanDetails

class FullParams(RequiredFullParams, OptionalFullParams):
    pass