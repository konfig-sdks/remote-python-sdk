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

from remote_python_sdk.pydantic.resignation_after_start_date_request_params_owed_outstanding_reimbursements import ResignationAfterStartDateRequestParamsOwedOutstandingReimbursements
from remote_python_sdk.pydantic.resignation_after_start_date_request_params_proposed_last_date import ResignationAfterStartDateRequestParamsProposedLastDate

class ResignationAfterStartDateRequestParams(BaseModel):
    accepts_proposed_notice: bool = Field(alias='accepts_proposed_notice')

    agrees_to_pto_amount: bool = Field(alias='agrees_to_pto_amount')

    agrees_to_resignation_reason: bool = Field(alias='agrees_to_resignation_reason')

    has_additional_information: bool = Field(alias='has_additional_information')

    has_more_salary_info: bool = Field(alias='has_more_salary_info')

    is_owed_outstanding_reimbursements: bool = Field(alias='is_owed_outstanding_reimbursements')

    will_take_more_pto: bool = Field(alias='will_take_more_pto')

    # Required if `agrees_to_pto_amount` is set to false.
    agrees_to_pto_amount_notes: typing.Optional[str] = Field(None, alias='agrees_to_pto_amount_notes')

    # required if `agrees_to_resignation_reason` is set to false.
    agrees_to_resignation_reason_notes: typing.Optional[str] = Field(None, alias='agrees_to_resignation_reason_notes')

    # required if `has_additional_information` is set to true.
    has_additional_information_notes: typing.Optional[str] = Field(None, alias='has_additional_information_notes')

    # required if `has_more_salary_info` is set to true.
    has_more_salary_info_notes: typing.Optional[str] = Field(None, alias='has_more_salary_info_notes')

    owed_outstanding_reimbursements: typing.Optional[ResignationAfterStartDateRequestParamsOwedOutstandingReimbursements] = Field(None, alias='owed_outstanding_reimbursements')

    proposed_last_date: typing.Optional[ResignationAfterStartDateRequestParamsProposedLastDate] = Field(None, alias='proposed_last_date')

    # required if `will_take_more_pto` is set to true.
    will_take_more_pto_notes: typing.Optional[str] = Field(None, alias='will_take_more_pto_notes')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
