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

from remote_python_sdk.type.employment_lifecycle_stage import EmploymentLifecycleStage
from remote_python_sdk.type.slug import Slug

class RequiredEmploymentBasicResponse(TypedDict):
    pass

class OptionalEmploymentBasicResponse(TypedDict, total=False):
    # Employment basic information. As its properties may vary depending on the country,                you must query the [Show form schema](https://gateway.remote.com/v1/docs/openapi.html) endpoint             passing the country code and `basic_information` as path parameters.
    basic_information: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]

    company_id: str

    country_code: str

    created_at: datetime

    employment_lifecycle_stage: EmploymentLifecycleStage

    full_name: str

    id: Slug

    job_title: str

    personal_email: str

    # Required for employees, optional for contractors
    provisional_start_date: date

    type: str

    updated_at: datetime

class EmploymentBasicResponse(RequiredEmploymentBasicResponse, OptionalEmploymentBasicResponse):
    pass