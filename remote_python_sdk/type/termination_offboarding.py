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

from remote_python_sdk.type.termination_offboarding_employee_awareness import TerminationOffboardingEmployeeAwareness
from remote_python_sdk.type.termination_offboarding_risk_assessment_reasons import TerminationOffboardingRiskAssessmentReasons

class RequiredTerminationOffboarding(TypedDict):
    additional_comments: str

    confidential: bool

    employment_id: str

    id: str

    proposed_termination_date: date

    reason_description: str

    requested_by: str

    risk_assessment_reasons: TerminationOffboardingRiskAssessmentReasons

    status: str

    submitted_at: str

    # Most updated termination date for the offboarding. This date is subject to change through the offboarding process even after it is finalized.
    termination_date: typing.Optional[date]

    termination_reason: str

    type: str

    will_challenge_termination: bool

class OptionalTerminationOffboarding(TypedDict, total=False):
    agrees_to_pto_amount: str

    employee_awareness: TerminationOffboardingEmployeeAwareness

    will_challenge_termination_description: str

class TerminationOffboarding(RequiredTerminationOffboarding, OptionalTerminationOffboarding):
    pass
