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


class ResourceErrorResponseMessage(BaseModel):
    code: typing.Optional[Literal["parameter_invalid_date", "resource_not_supported_for_country", "parameter_value_invalid", "request_internal_server_error", "resource_invalid_state", "resource_already_exists", "resource_not_eligible", "action_invalid", "action_unrecognized", "parameter_map_empty", "parameter_one_of_required_missing", "parameter_required_missing", "parameter_too_many", "parameter_unknown", "parameter_value_unknown", "request_body_empty"]] = Field(None, alias='code')

    message: typing.Optional[str] = Field(None, alias='message')

    resource_id: typing.Optional[typing.Optional[str]] = Field(None, alias='resource_id')

    resource_type: typing.Optional[str] = Field(None, alias='resource_type')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
