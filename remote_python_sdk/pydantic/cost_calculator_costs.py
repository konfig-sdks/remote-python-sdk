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

from remote_python_sdk.pydantic.cost_calculator_cost import CostCalculatorCost
from remote_python_sdk.pydantic.currency import Currency

class CostCalculatorCosts(BaseModel):
    # The annual contributions that a company must pay for this employment
    annual_contributions_total: int = Field(alias='annual_contributions_total')

    # The annual gross salary that the employee is going to earn
    annual_gross_salary: int = Field(alias='annual_gross_salary')

    # The annual gross salary + annual contributions + annual fee (monthly fee * 12) + extra statutory payments if applicable
    annual_total: int = Field(alias='annual_total')

    currency: Currency = Field(alias='currency')

    # 13th month salary, this happens for countries such as Philippines
    extra_statutory_payments_total: int = Field(alias='extra_statutory_payments_total')

    # The contributions that the company pays monthly
    monthly_contributions_total: int = Field(alias='monthly_contributions_total')

    # The gross monthly salary for the Employee
    monthly_gross_salary: int = Field(alias='monthly_gross_salary')

    # Monthly gross salary + monthly contributions  (doesn't include fee)
    monthly_tce: int = Field(alias='monthly_tce')

    # Monthly gross salary + monthly contributions + monthly fee
    monthly_total: int = Field(alias='monthly_total')

    # The list of all annual benefit costs
    annual_benefits_breakdown: typing.Optional[typing.List[CostCalculatorCost]] = Field(None, alias='annual_benefits_breakdown')

    # The annual benefits total that a company must pay for this employment
    annual_benefits_total: typing.Optional[int] = Field(None, alias='annual_benefits_total')

    # The list of all annual employer contribution costs
    annual_contributions_breakdown: typing.Optional[typing.List[CostCalculatorCost]] = Field(None, alias='annual_contributions_breakdown')

    # The list of all annual extra statutory payment costs
    extra_statutory_payments_breakdown: typing.Optional[typing.List[CostCalculatorCost]] = Field(None, alias='extra_statutory_payments_breakdown')

    # The list of all monthly benefit costs
    monthly_benefits_breakdown: typing.Optional[typing.List[CostCalculatorCost]] = Field(None, alias='monthly_benefits_breakdown')

    # The benefits total that the company pays monthly
    monthly_benefits_total: typing.Optional[int] = Field(None, alias='monthly_benefits_total')

    # The list of all monthly employer contribution costs
    monthly_contributions_breakdown: typing.Optional[typing.List[CostCalculatorCost]] = Field(None, alias='monthly_contributions_breakdown')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
