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

from remote_python_sdk.type.salary_decrease_details import SalaryDecreaseDetails

class RequiredRequestDetails(TypedDict):
    pass

class OptionalRequestDetails(TypedDict, total=False):
    additional_comments: typing.Optional[str]

    effective_date: date

    reason_for_change: str

    # This is filled when the reason_for_change is 'other'.
    reason_for_change_description: typing.Optional[str]

    salary_decrease_details: typing.Optional[SalaryDecreaseDetails]

class RequestDetails(RequiredRequestDetails, OptionalRequestDetails):
    pass
