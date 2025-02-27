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

from remote_python_sdk.type.offboarding_file import OffboardingFile
from remote_python_sdk.type.termination_details_params_employee_awareness import TerminationDetailsParamsEmployeeAwareness
from remote_python_sdk.type.termination_details_params_risk_assessment_reasons import TerminationDetailsParamsRiskAssessmentReasons

class RequiredTerminationDetailsParams(TypedDict):
    # Confidential requests are visible for who authorized the token or integration. Non-confidential requests are visible to all admins in the company.
    confidential: bool

    # In most cases, employee needs to be notified before termination. The required notice period depends on local labor laws, the employment agreement, and other factors. Remote will use those factors to determine the required notice period. Please note that we cannot commit to a termination date until we conduct a full review of the information you submit.
    proposed_termination_date: date

    # Description of the reason for termination
    reason_description: str

    risk_assessment_reasons: TerminationDetailsParamsRiskAssessmentReasons

    # Choose an accurate termination reason to avoid unfair or unlawful dismissal claims.  If the termination is created before the employee's start date, this field will be set to `cancellation_before_start_date`. 
    termination_reason: str

    # Whether is it likely or not that the employee will challenge their termination
    will_challenge_termination: bool

class OptionalTerminationDetailsParams(TypedDict, total=False):
    # Additional details regarding the termination process.
    additional_comments: str

    employee_awareness: TerminationDetailsParamsEmployeeAwareness

    # Remote will use this email address for post-termination communication. If it is not provided, this field will be derived from the employment record. Therefore, it is important to ensure that it is not a company email. 
    personal_email: str

    # Any supporting documents regarding the termination reason
    termination_reason_files: typing.List[OffboardingFile]

    # Paid time off accuracy  Typically, any vacation pay accrued and unpaid at the time of termination must be paid out to the employee. To avoid overpaying or underpaying, please make sure we have an accurate account of their paid time off by querying the [Show Time Off Balance](https://gateway.remote.com/v1/docs/openapi.html) endpoint, filtering by the `employment_id`. This optional document should be sent in case of any discrepancies. 
    timesheet_file: OffboardingFile

    # If it is likely that the employee will challenge their termination, please provide additional details explaining the risk
    will_challenge_termination_description: str

class TerminationDetailsParams(RequiredTerminationDetailsParams, OptionalTerminationDetailsParams):
    pass
