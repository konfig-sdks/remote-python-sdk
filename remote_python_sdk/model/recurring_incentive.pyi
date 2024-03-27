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


class RecurringIncentive(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "employment_id",
            "amount",
            "amount_tax_type",
            "id",
            "type",
            "start_date",
            "status",
        }
        
        class properties:
            amount = schemas.IntSchema
        
            @staticmethod
            def amount_tax_type() -> typing.Type['AmountTaxType']:
                return AmountTaxType
            employment_id = schemas.StrSchema
            id = schemas.StrSchema
            start_date = schemas.DateSchema
            
            
            class status(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def ACTIVE(cls):
                    return cls("active")
                
                @schemas.classproperty
                def INACTIVE(cls):
                    return cls("inactive")
            
            
            class type(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def ACTING_UP_ALLOWANCE(cls):
                    return cls("acting_up_allowance")
                
                @schemas.classproperty
                def ALLOWANCE(cls):
                    return cls("allowance")
                
                @schemas.classproperty
                def CAR_ALLOWANCE(cls):
                    return cls("car_allowance")
                
                @schemas.classproperty
                def HEALTH_AND_WELLNESS_ALLOWANCE(cls):
                    return cls("health_and_wellness_allowance")
                
                @schemas.classproperty
                def INTERNET_ALLOWANCE(cls):
                    return cls("internet_allowance")
                
                @schemas.classproperty
                def MEAL_ALLOWANCE(cls):
                    return cls("meal_allowance")
                
                @schemas.classproperty
                def ON_CALL_ALLOWANCE(cls):
                    return cls("on_call_allowance")
                
                @schemas.classproperty
                def PARENTHOOD_ALLOWANCE(cls):
                    return cls("parenthood_allowance")
                
                @schemas.classproperty
                def PHONE_ALLOWANCE(cls):
                    return cls("phone_allowance")
                
                @schemas.classproperty
                def RELOCATION_ALLOWANCE(cls):
                    return cls("relocation_allowance")
                
                @schemas.classproperty
                def TRAVEL_ALLOWANCE(cls):
                    return cls("travel_allowance")
                
                @schemas.classproperty
                def WORK_FROM_HOME_ALLOWANCE(cls):
                    return cls("work_from_home_allowance")
                
                @schemas.classproperty
                def BONUS(cls):
                    return cls("bonus")
                
                @schemas.classproperty
                def HOLIDAY_BONUS(cls):
                    return cls("holiday_bonus")
                
                @schemas.classproperty
                def REFERRAL_BONUS(cls):
                    return cls("referral_bonus")
                
                @schemas.classproperty
                def RETENTION_BONUS(cls):
                    return cls("retention_bonus")
                
                @schemas.classproperty
                def COMMISSION(cls):
                    return cls("commission")
                
                @schemas.classproperty
                def OTHER(cls):
                    return cls("other")
                
                @schemas.classproperty
                def OVERTIME(cls):
                    return cls("overtime")
                
                @schemas.classproperty
                def STIPEND(cls):
                    return cls("stipend")
            
            
            class end_date(
                schemas.DateBase,
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                class MetaOapg:
                    format = 'date'
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, date, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'end_date':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class note(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'note':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            __annotations__ = {
                "amount": amount,
                "amount_tax_type": amount_tax_type,
                "employment_id": employment_id,
                "id": id,
                "start_date": start_date,
                "status": status,
                "type": type,
                "end_date": end_date,
                "note": note,
            }
    
    employment_id: MetaOapg.properties.employment_id
    amount: MetaOapg.properties.amount
    amount_tax_type: 'AmountTaxType'
    id: MetaOapg.properties.id
    type: MetaOapg.properties.type
    start_date: MetaOapg.properties.start_date
    status: MetaOapg.properties.status
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["amount"]) -> MetaOapg.properties.amount: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["amount_tax_type"]) -> 'AmountTaxType': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["employment_id"]) -> MetaOapg.properties.employment_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["start_date"]) -> MetaOapg.properties.start_date: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["end_date"]) -> MetaOapg.properties.end_date: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["note"]) -> MetaOapg.properties.note: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["amount", "amount_tax_type", "employment_id", "id", "start_date", "status", "type", "end_date", "note", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["amount"]) -> MetaOapg.properties.amount: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["amount_tax_type"]) -> 'AmountTaxType': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["employment_id"]) -> MetaOapg.properties.employment_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["start_date"]) -> MetaOapg.properties.start_date: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["end_date"]) -> typing.Union[MetaOapg.properties.end_date, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["note"]) -> typing.Union[MetaOapg.properties.note, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["amount", "amount_tax_type", "employment_id", "id", "start_date", "status", "type", "end_date", "note", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        employment_id: typing.Union[MetaOapg.properties.employment_id, str, ],
        amount: typing.Union[MetaOapg.properties.amount, decimal.Decimal, int, ],
        amount_tax_type: 'AmountTaxType',
        id: typing.Union[MetaOapg.properties.id, str, ],
        type: typing.Union[MetaOapg.properties.type, str, ],
        start_date: typing.Union[MetaOapg.properties.start_date, str, date, ],
        status: typing.Union[MetaOapg.properties.status, str, ],
        end_date: typing.Union[MetaOapg.properties.end_date, None, str, date, schemas.Unset] = schemas.unset,
        note: typing.Union[MetaOapg.properties.note, None, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'RecurringIncentive':
        return super().__new__(
            cls,
            *args,
            employment_id=employment_id,
            amount=amount,
            amount_tax_type=amount_tax_type,
            id=id,
            type=type,
            start_date=start_date,
            status=status,
            end_date=end_date,
            note=note,
            _configuration=_configuration,
            **kwargs,
        )

from remote_python_sdk.model.amount_tax_type import AmountTaxType