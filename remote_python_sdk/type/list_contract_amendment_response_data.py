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

from remote_python_sdk.type.minimal_contract_amendment import MinimalContractAmendment

class RequiredListContractAmendmentResponseData(TypedDict):
    pass

class OptionalListContractAmendmentResponseData(TypedDict, total=False):
    contract_amendments: typing.List[MinimalContractAmendment]

    # The current page among all of the total_pages
    current_page: int

    # The total number of records in the result
    total_count: int

    # The total number of pages the user can go through
    total_pages: int

class ListContractAmendmentResponseData(RequiredListContractAmendmentResponseData, OptionalListContractAmendmentResponseData):
    pass
