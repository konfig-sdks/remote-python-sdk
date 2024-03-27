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


class Timeoff(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "employment_id",
            "end_date",
            "timeoff_days",
            "timezone",
            "timeoff_type",
            "id",
            "start_date",
            "status",
        }
        
        class properties:
            employment_id = schemas.StrSchema
            end_date = schemas.DateSchema
            id = schemas.StrSchema
            start_date = schemas.DateSchema
            status = schemas.StrSchema
            
            
            class timeoff_days(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['TimeoffDay']:
                        return TimeoffDay
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['TimeoffDay'], typing.List['TimeoffDay']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'timeoff_days':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'TimeoffDay':
                    return super().__getitem__(i)
        
            @staticmethod
            def timeoff_type() -> typing.Type['TimeoffType']:
                return TimeoffType
            timezone = schemas.StrSchema
            
            
            class approved_at(
                schemas.DateTimeBase,
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                class MetaOapg:
                    format = 'date-time'
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, datetime, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'approved_at':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
        
            @staticmethod
            def approver_id() -> typing.Type['NullableApproverId']:
                return NullableApproverId
            
            
            class cancel_reason(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'cancel_reason':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
        
            @staticmethod
            def cancelled_at() -> typing.Type['NullableDateTime']:
                return NullableDateTime
        
            @staticmethod
            def document() -> typing.Type['File']:
                return File
            
            
            class notes(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'notes':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            __annotations__ = {
                "employment_id": employment_id,
                "end_date": end_date,
                "id": id,
                "start_date": start_date,
                "status": status,
                "timeoff_days": timeoff_days,
                "timeoff_type": timeoff_type,
                "timezone": timezone,
                "approved_at": approved_at,
                "approver_id": approver_id,
                "cancel_reason": cancel_reason,
                "cancelled_at": cancelled_at,
                "document": document,
                "notes": notes,
            }
    
    employment_id: MetaOapg.properties.employment_id
    end_date: MetaOapg.properties.end_date
    timeoff_days: MetaOapg.properties.timeoff_days
    timezone: MetaOapg.properties.timezone
    timeoff_type: 'TimeoffType'
    id: MetaOapg.properties.id
    start_date: MetaOapg.properties.start_date
    status: MetaOapg.properties.status
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["employment_id"]) -> MetaOapg.properties.employment_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["end_date"]) -> MetaOapg.properties.end_date: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["start_date"]) -> MetaOapg.properties.start_date: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["timeoff_days"]) -> MetaOapg.properties.timeoff_days: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["timeoff_type"]) -> 'TimeoffType': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["timezone"]) -> MetaOapg.properties.timezone: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["approved_at"]) -> MetaOapg.properties.approved_at: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["approver_id"]) -> 'NullableApproverId': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["cancel_reason"]) -> MetaOapg.properties.cancel_reason: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["cancelled_at"]) -> 'NullableDateTime': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["document"]) -> 'File': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["notes"]) -> MetaOapg.properties.notes: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["employment_id", "end_date", "id", "start_date", "status", "timeoff_days", "timeoff_type", "timezone", "approved_at", "approver_id", "cancel_reason", "cancelled_at", "document", "notes", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["employment_id"]) -> MetaOapg.properties.employment_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["end_date"]) -> MetaOapg.properties.end_date: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["start_date"]) -> MetaOapg.properties.start_date: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["timeoff_days"]) -> MetaOapg.properties.timeoff_days: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["timeoff_type"]) -> 'TimeoffType': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["timezone"]) -> MetaOapg.properties.timezone: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["approved_at"]) -> typing.Union[MetaOapg.properties.approved_at, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["approver_id"]) -> typing.Union['NullableApproverId', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["cancel_reason"]) -> typing.Union[MetaOapg.properties.cancel_reason, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["cancelled_at"]) -> typing.Union['NullableDateTime', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["document"]) -> typing.Union['File', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["notes"]) -> typing.Union[MetaOapg.properties.notes, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["employment_id", "end_date", "id", "start_date", "status", "timeoff_days", "timeoff_type", "timezone", "approved_at", "approver_id", "cancel_reason", "cancelled_at", "document", "notes", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        employment_id: typing.Union[MetaOapg.properties.employment_id, str, ],
        end_date: typing.Union[MetaOapg.properties.end_date, str, date, ],
        timeoff_days: typing.Union[MetaOapg.properties.timeoff_days, list, tuple, ],
        timezone: typing.Union[MetaOapg.properties.timezone, str, ],
        timeoff_type: 'TimeoffType',
        id: typing.Union[MetaOapg.properties.id, str, ],
        start_date: typing.Union[MetaOapg.properties.start_date, str, date, ],
        status: typing.Union[MetaOapg.properties.status, str, ],
        approved_at: typing.Union[MetaOapg.properties.approved_at, None, str, datetime, schemas.Unset] = schemas.unset,
        approver_id: typing.Union['NullableApproverId', schemas.Unset] = schemas.unset,
        cancel_reason: typing.Union[MetaOapg.properties.cancel_reason, None, str, schemas.Unset] = schemas.unset,
        cancelled_at: typing.Union['NullableDateTime', schemas.Unset] = schemas.unset,
        document: typing.Union['File', schemas.Unset] = schemas.unset,
        notes: typing.Union[MetaOapg.properties.notes, None, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Timeoff':
        return super().__new__(
            cls,
            *args,
            employment_id=employment_id,
            end_date=end_date,
            timeoff_days=timeoff_days,
            timezone=timezone,
            timeoff_type=timeoff_type,
            id=id,
            start_date=start_date,
            status=status,
            approved_at=approved_at,
            approver_id=approver_id,
            cancel_reason=cancel_reason,
            cancelled_at=cancelled_at,
            document=document,
            notes=notes,
            _configuration=_configuration,
            **kwargs,
        )

from remote_python_sdk.model.file import File
from remote_python_sdk.model.nullable_approver_id import NullableApproverId
from remote_python_sdk.model.nullable_date_time import NullableDateTime
from remote_python_sdk.model.timeoff_day import TimeoffDay
from remote_python_sdk.model.timeoff_type import TimeoffType