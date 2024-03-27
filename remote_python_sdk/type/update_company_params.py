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


class RequiredUpdateCompanyParams(TypedDict):
    pass

class OptionalUpdateCompanyParams(TypedDict, total=False):
    # Fields can vary depending on the country. Please, check the required fields structure using the [Show form schema endpoint](https://gateway.remote.com/v1/docs/openapi.html). Use the desired country and `address_details` as the form name for the placeholders. The response complies with the [JSON Schema](https://remote.com/resources/api/how-json-schemas-work) specification. 
    address_details: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]

    # Fields can vary depending on the country. Please, check the required fields structure using the [Show form schema endpoint](https://gateway.remote.com/v1/docs/openapi.html). Use the desired country and `bank_account_details` as the form name for the placeholders. The response complies with the [JSON Schema](https://remote.com/resources/api/how-json-schemas-work) specification. 
    bank_account_details: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]

    # Country of company address
    country_code: str

    # Desired currency for invoicing and displaying converted salaries in Remote UI regardless of the employee's country.  This field is only accepted if company is in status `pending`. Please contact Remote if you wish to update it. 
    desired_currency: str

    # This field is only accepted if company is in status `pending`. Please contact Remote if you wish to update it. 
    name: str

    # A phone number the company can be contacted with.
    phone_number: str

    # The company registration number. This field or tax_number (but not both) should be submitted.  This field is only accepted if company is in status `pending`. 
    registration_number: str

    #   The tax identifier of the company. This field or registration_number (but not both) should be submitted.    This field is only accepted if company is in status `pending`. 
    tax_number: str

class UpdateCompanyParams(RequiredUpdateCompanyParams, OptionalUpdateCompanyParams):
    pass