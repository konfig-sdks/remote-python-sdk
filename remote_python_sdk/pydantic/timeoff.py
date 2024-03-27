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

from remote_python_sdk.pydantic.file import File
from remote_python_sdk.pydantic.nullable_approver_id import NullableApproverId
from remote_python_sdk.pydantic.nullable_date_time import NullableDateTime
from remote_python_sdk.pydantic.timeoff_day import TimeoffDay
from remote_python_sdk.pydantic.timeoff_type import TimeoffType

class Timeoff(BaseModel):
    employment_id: str = Field(alias='employment_id')

    end_date: date = Field(alias='end_date')

    id: str = Field(alias='id')

    start_date: date = Field(alias='start_date')

    status: str = Field(alias='status')

    timeoff_days: typing.List[TimeoffDay] = Field(alias='timeoff_days')

    timeoff_type: TimeoffType = Field(alias='timeoff_type')

    # [TZ identifier](https://www.iana.org/time-zones)
    timezone: str = Field(alias='timezone')

    approved_at: typing.Optional[typing.Optional[datetime]] = Field(None, alias='approved_at')

    approver_id: typing.Optional[NullableApproverId] = Field(None, alias='approver_id')

    cancel_reason: typing.Optional[typing.Optional[str]] = Field(None, alias='cancel_reason')

    cancelled_at: typing.Optional[NullableDateTime] = Field(None, alias='cancelled_at')

    document: typing.Optional[File] = Field(None, alias='document')

    notes: typing.Optional[typing.Optional[str]] = Field(None, alias='notes')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )