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

from remote_python_sdk.type.base64_file import Base64File

class RequiredParamsToCreateExpense(TypedDict):
    title: str

    amount: int

    #   The three-letter code for the expense currency.<br/>   Examples: `\"USD\"`, `\"EUR\"`, `\"CAD\"` 
    currency: str

    # The ID for the employment to which this expense relates.
    employment_id: str

    # Date of the purchase, which must be in the past
    expense_date: str

class OptionalParamsToCreateExpense(TypedDict, total=False):
    # Categories allowed for an expense
    category: str

    receipt: Base64File

    receipts: typing.List[Base64File]

    # The date and time that the expense was reviewed in ISO8601 format. If not provided, it defaults to the current datetime.
    reviewed_at: date

    # If the person reviewing the expense is a user in Remote, you can provide its user id for this field. If a value is not provided, defaults to the user that generated the API token.
    reviewer_id: str

    tax_amount: int

    # [TZ identifier](https://www.iana.org/time-zones)
    timezone: str

class ParamsToCreateExpense(RequiredParamsToCreateExpense, OptionalParamsToCreateExpense):
    pass
