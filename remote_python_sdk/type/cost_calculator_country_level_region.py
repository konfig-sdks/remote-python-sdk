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

from remote_python_sdk.type.cost_calculator_country_availability import CostCalculatorCountryAvailability
from remote_python_sdk.type.currency import Currency
from remote_python_sdk.type.minimal_region import MinimalRegion

class RequiredCostCalculatorCountryLevelRegion(TypedDict):
    availability: CostCalculatorCountryAvailability

    child_regions: typing.List[MinimalRegion]

    code: str

    currency: Currency

    name: str

    original_country_slug: str

    region_slug: str

class OptionalCostCalculatorCountryLevelRegion(TypedDict, total=False):
    has_additional_fields: bool

class CostCalculatorCountryLevelRegion(RequiredCostCalculatorCountryLevelRegion, OptionalCostCalculatorCountryLevelRegion):
    pass
