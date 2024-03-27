# coding: utf-8

"""
    Remote API

    Talent is everywhere. Opportunity is not. Remote's mission is to create opportunity everywhere, empowering employers to find and hire the best talent, and enabling individuals to build financial and personal freedom.   Remote is a Global HR Platform that helps companies hire, manage, and pay their entire team — and more effectively compete in the modern global economy through our comprehensive set of core solutions including, HRIS, payroll, international employment, contractor management, and more.   Whether you're just starting your global journey, or looking to optimize your existing operations, sign up or book a demo - and see how Remote makes global HR simple.

    The version of the OpenAPI document: 0.1.0
    Generated by: https://konfigthis.com
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from remote_python_sdk import schemas  # noqa: F401


class TimeoffType(
    schemas.EnumBase,
    schemas.StrSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    
    @schemas.classproperty
    def PAID_TIME_OFF(cls):
        return cls("paid_time_off")
    
    @schemas.classproperty
    def SICK_LEAVE(cls):
        return cls("sick_leave")
    
    @schemas.classproperty
    def PUBLIC_HOLIDAY(cls):
        return cls("public_holiday")
    
    @schemas.classproperty
    def UNPAID_LEAVE(cls):
        return cls("unpaid_leave")
    
    @schemas.classproperty
    def EXTENDED_LEAVE(cls):
        return cls("extended_leave")
    
    @schemas.classproperty
    def IN_LIEU_TIME(cls):
        return cls("in_lieu_time")
    
    @schemas.classproperty
    def MATERNITY_LEAVE(cls):
        return cls("maternity_leave")
    
    @schemas.classproperty
    def PATERNITY_LEAVE(cls):
        return cls("paternity_leave")
    
    @schemas.classproperty
    def PARENTAL_LEAVE(cls):
        return cls("parental_leave")
    
    @schemas.classproperty
    def BEREAVEMENT(cls):
        return cls("bereavement")
    
    @schemas.classproperty
    def MILITARY_LEAVE(cls):
        return cls("military_leave")
    
    @schemas.classproperty
    def OTHER(cls):
        return cls("other")