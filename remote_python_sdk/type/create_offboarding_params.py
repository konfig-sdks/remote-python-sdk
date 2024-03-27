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

from remote_python_sdk.type.termination_details_params import TerminationDetailsParams

class RequiredCreateOffboardingParams(TypedDict):
    employment_id: str

    termination_details: TerminationDetailsParams

    # The type of the offboarding request. For now, only `termination` is allowed.
    type: str

class OptionalCreateOffboardingParams(TypedDict, total=False):
    pass

class CreateOffboardingParams(RequiredCreateOffboardingParams, OptionalCreateOffboardingParams):
    pass
