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

from remote_python_sdk.type.resignation_after_start_date_request_params_owed_outstanding_reimbursements import ResignationAfterStartDateRequestParamsOwedOutstandingReimbursements
from remote_python_sdk.type.resignation_after_start_date_request_params_proposed_last_date import ResignationAfterStartDateRequestParamsProposedLastDate

class RequiredResignationAfterStartDateRequestParams(TypedDict):
    accepts_proposed_notice: bool

    agrees_to_pto_amount: bool

    agrees_to_resignation_reason: bool

    has_additional_information: bool

    has_more_salary_info: bool

    is_owed_outstanding_reimbursements: bool

    will_take_more_pto: bool

class OptionalResignationAfterStartDateRequestParams(TypedDict, total=False):
    # Required if `agrees_to_pto_amount` is set to false.
    agrees_to_pto_amount_notes: str

    # required if `agrees_to_resignation_reason` is set to false.
    agrees_to_resignation_reason_notes: str

    # required if `has_additional_information` is set to true.
    has_additional_information_notes: str

    # required if `has_more_salary_info` is set to true.
    has_more_salary_info_notes: str

    owed_outstanding_reimbursements: ResignationAfterStartDateRequestParamsOwedOutstandingReimbursements

    proposed_last_date: ResignationAfterStartDateRequestParamsProposedLastDate

    # required if `will_take_more_pto` is set to true.
    will_take_more_pto_notes: str

class ResignationAfterStartDateRequestParams(RequiredResignationAfterStartDateRequestParams, OptionalResignationAfterStartDateRequestParams):
    pass
