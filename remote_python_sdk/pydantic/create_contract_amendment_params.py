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


class CreateContractAmendmentParams(BaseModel):
    # The contract ID of the contract that needs to be amended.
    amendment_contract_id: str = Field(alias='amendment_contract_id')

    # Contract amendment informations. As its properties may vary depending on the country,                 you must query the [Show form schema](https://gateway.remote.com/v1/docs/openapi.html) endpoint             passing the country code, `contract_amendment` and the employment ID as request body.
    contract_amendment: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(alias='contract_amendment')

    # The employment ID that is related to the contract amendment request.
    employment_id: str = Field(alias='employment_id')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
