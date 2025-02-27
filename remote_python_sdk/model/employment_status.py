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


class EmploymentStatus(
    schemas.EnumBase,
    schemas.StrSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    The status of employment
    """


    class MetaOapg:
        enum_value_to_name = {
            "active": "ACTIVE",
            "created": "CREATED",
            "created_awaiting_reserve": "CREATED_AWAITING_RESERVE",
            "created_reserve_paid": "CREATED_RESERVE_PAID",
            "initiated": "INITIATED",
            "invited": "INVITED",
            "pending": "PENDING",
            "review": "REVIEW",
            "archived": "ARCHIVED",
            "deleted": "DELETED",
        }
    
    @schemas.classproperty
    def ACTIVE(cls):
        return cls("active")
    
    @schemas.classproperty
    def CREATED(cls):
        return cls("created")
    
    @schemas.classproperty
    def CREATED_AWAITING_RESERVE(cls):
        return cls("created_awaiting_reserve")
    
    @schemas.classproperty
    def CREATED_RESERVE_PAID(cls):
        return cls("created_reserve_paid")
    
    @schemas.classproperty
    def INITIATED(cls):
        return cls("initiated")
    
    @schemas.classproperty
    def INVITED(cls):
        return cls("invited")
    
    @schemas.classproperty
    def PENDING(cls):
        return cls("pending")
    
    @schemas.classproperty
    def REVIEW(cls):
        return cls("review")
    
    @schemas.classproperty
    def ARCHIVED(cls):
        return cls("archived")
    
    @schemas.classproperty
    def DELETED(cls):
        return cls("deleted")
