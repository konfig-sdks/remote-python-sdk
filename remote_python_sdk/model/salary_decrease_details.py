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


class SalaryDecreaseDetails(
    schemas.DictBase,
    schemas.NoneBase,
    schemas.Schema,
    schemas.NoneFrozenDictMixin
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    The details of the salary decrease request if there is one
    """


    class MetaOapg:
        
        class properties:
            
            
            class salary_decrease_reason(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "change_in_working_hours": "CHANGE_IN_WORKING_HOURS",
                        "trade_salary_for_equity": "TRADE_SALARY_FOR_EQUITY",
                        "error_in_initial_salary": "ERROR_IN_INITIAL_SALARY",
                        "role_change_or_demotion": "ROLE_CHANGE_OR_DEMOTION",
                        "compensation_restructure": "COMPENSATION_RESTRUCTURE",
                        "other": "OTHER",
                    }
                
                @schemas.classproperty
                def CHANGE_IN_WORKING_HOURS(cls):
                    return cls("change_in_working_hours")
                
                @schemas.classproperty
                def TRADE_SALARY_FOR_EQUITY(cls):
                    return cls("trade_salary_for_equity")
                
                @schemas.classproperty
                def ERROR_IN_INITIAL_SALARY(cls):
                    return cls("error_in_initial_salary")
                
                @schemas.classproperty
                def ROLE_CHANGE_OR_DEMOTION(cls):
                    return cls("role_change_or_demotion")
                
                @schemas.classproperty
                def COMPENSATION_RESTRUCTURE(cls):
                    return cls("compensation_restructure")
                
                @schemas.classproperty
                def OTHER(cls):
                    return cls("other")
            
            
            class salary_decrease_reason_description(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'salary_decrease_reason_description':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            was_employee_informed = schemas.StrSchema
            __annotations__ = {
                "salary_decrease_reason": salary_decrease_reason,
                "salary_decrease_reason_description": salary_decrease_reason_description,
                "was_employee_informed": was_employee_informed,
            }

    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["salary_decrease_reason"]) -> MetaOapg.properties.salary_decrease_reason: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["salary_decrease_reason_description"]) -> MetaOapg.properties.salary_decrease_reason_description: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["was_employee_informed"]) -> MetaOapg.properties.was_employee_informed: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["salary_decrease_reason", "salary_decrease_reason_description", "was_employee_informed", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["salary_decrease_reason"]) -> typing.Union[MetaOapg.properties.salary_decrease_reason, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["salary_decrease_reason_description"]) -> typing.Union[MetaOapg.properties.salary_decrease_reason_description, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["was_employee_informed"]) -> typing.Union[MetaOapg.properties.was_employee_informed, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["salary_decrease_reason", "salary_decrease_reason_description", "was_employee_informed", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, None, ],
        salary_decrease_reason: typing.Union[MetaOapg.properties.salary_decrease_reason, str, schemas.Unset] = schemas.unset,
        salary_decrease_reason_description: typing.Union[MetaOapg.properties.salary_decrease_reason_description, None, str, schemas.Unset] = schemas.unset,
        was_employee_informed: typing.Union[MetaOapg.properties.was_employee_informed, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'SalaryDecreaseDetails':
        return super().__new__(
            cls,
            *args,
            salary_decrease_reason=salary_decrease_reason,
            salary_decrease_reason_description=salary_decrease_reason_description,
            was_employee_informed=was_employee_informed,
            _configuration=_configuration,
            **kwargs,
        )
