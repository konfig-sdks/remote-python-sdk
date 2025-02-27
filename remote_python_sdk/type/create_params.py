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


class RequiredCreateParams(TypedDict):
    pass

class OptionalCreateParams(TypedDict, total=False):
    # Employment basic information. When using this field, the same other root level fields (name, personal_email, job_title, provisional_start_date, and seniority_date) will be ignored. Its properties may vary depending on the country, you must query the [Show form schema](https://gateway.remote.com/v1/docs/openapi.html) endpoint passing the country code and `employment_basic_information` as path parameters. 
    basic_information: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]

    # This optional field is deprecated.
    company_id: str

    country_code: str

    # If not provided, it will default to `employee`.
    type: str

class CreateParams(RequiredCreateParams, OptionalCreateParams):
    pass
