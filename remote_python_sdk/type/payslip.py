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


class RequiredPayslip(TypedDict):
    employment_id: str

    id: str

    issued_at: date

class OptionalPayslip(TypedDict, total=False):
    # UTC date in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format
    expected_payout_date: date

    # This field is only shown if available
    net_pay_converted_amount: int

    # This field is only shown if available
    net_pay_source_amount: int

class Payslip(RequiredPayslip, OptionalPayslip):
    pass
