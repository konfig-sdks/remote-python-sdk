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

from remote_python_sdk.type.cost_calculator_cost import CostCalculatorCost
from remote_python_sdk.type.currency import Currency

class RequiredCostCalculatorCosts(TypedDict):
    # The annual contributions that a company must pay for this employment
    annual_contributions_total: int

    # The annual gross salary that the employee is going to earn
    annual_gross_salary: int

    # The annual gross salary + annual contributions + annual fee (monthly fee * 12) + extra statutory payments if applicable
    annual_total: int

    currency: Currency

    # 13th month salary, this happens for countries such as Philippines
    extra_statutory_payments_total: int

    # The contributions that the company pays monthly
    monthly_contributions_total: int

    # The gross monthly salary for the Employee
    monthly_gross_salary: int

    # Monthly gross salary + monthly contributions  (doesn't include fee)
    monthly_tce: int

    # Monthly gross salary + monthly contributions + monthly fee
    monthly_total: int

class OptionalCostCalculatorCosts(TypedDict, total=False):
    # The list of all annual benefit costs
    annual_benefits_breakdown: typing.List[CostCalculatorCost]

    # The annual benefits total that a company must pay for this employment
    annual_benefits_total: int

    # The list of all annual employer contribution costs
    annual_contributions_breakdown: typing.List[CostCalculatorCost]

    # The list of all annual extra statutory payment costs
    extra_statutory_payments_breakdown: typing.List[CostCalculatorCost]

    # The list of all monthly benefit costs
    monthly_benefits_breakdown: typing.List[CostCalculatorCost]

    # The benefits total that the company pays monthly
    monthly_benefits_total: int

    # The list of all monthly employer contribution costs
    monthly_contributions_breakdown: typing.List[CostCalculatorCost]

class CostCalculatorCosts(RequiredCostCalculatorCosts, OptionalCostCalculatorCosts):
    pass