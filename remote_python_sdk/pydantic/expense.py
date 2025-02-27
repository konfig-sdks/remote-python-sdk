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

from remote_python_sdk.pydantic.currency_definition import CurrencyDefinition
from remote_python_sdk.pydantic.expense_reviewer import ExpenseReviewer
from remote_python_sdk.pydantic.file import File

class Expense(BaseModel):
    title: str = Field(alias='title')

    amount: int = Field(alias='amount')

    converted_amount: int = Field(alias='converted_amount')

    converted_currency: CurrencyDefinition = Field(alias='converted_currency')

    converted_tax_amount: int = Field(alias='converted_tax_amount')

    currency: CurrencyDefinition = Field(alias='currency')

    employment_id: str = Field(alias='employment_id')

    expense_date: date = Field(alias='expense_date')

    id: str = Field(alias='id')

    tax_amount: int = Field(alias='tax_amount')

    # Categories allowed for an expense
    category: typing.Optional[Literal["education_training", "home_office", "meals", "other", "phone_utilities", "tech_equipment", "travel", "coworking"]] = Field(None, alias='category')

    invoice_period: typing.Optional[typing.Optional[str]] = Field(None, alias='invoice_period')

    notes: typing.Optional[typing.Optional[str]] = Field(None, alias='notes')

    reason: typing.Optional[typing.Optional[str]] = Field(None, alias='reason')

    receipts: typing.Optional[typing.List[File]] = Field(None, alias='receipts')

    reviewed_at: typing.Optional[typing.Optional[date]] = Field(None, alias='reviewed_at')

    reviewer: typing.Optional[ExpenseReviewer] = Field(None, alias='reviewer')

    # Expense status
    status: typing.Optional[Literal["canceled", "pending", "declined", "approved", "processing", "reimbursed"]] = Field(None, alias='status')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
