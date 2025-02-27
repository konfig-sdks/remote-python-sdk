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


class UpdateApprovedTimeoffParams(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Update timeoff params
    """


    class MetaOapg:
        required = {
            "cancel_reason",
            "edit_reason",
        }
        
        class properties:
            cancel_reason = schemas.StrSchema
            edit_reason = schemas.StrSchema
            approved_at = schemas.DateTimeSchema
        
            @staticmethod
            def approver_id() -> typing.Type['NullableApproverId']:
                return NullableApproverId
        
            @staticmethod
            def document() -> typing.Type['TimeoffDocumentParams']:
                return TimeoffDocumentParams
            end_date = schemas.DateSchema
            notes = schemas.StrSchema
            start_date = schemas.DateSchema
            
            
            class status(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "approved": "APPROVED",
                        "cancelled": "CANCELLED",
                    }
                
                @schemas.classproperty
                def APPROVED(cls):
                    return cls("approved")
                
                @schemas.classproperty
                def CANCELLED(cls):
                    return cls("cancelled")
            
            
            class timeoff_days(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['TimeoffDaysParams']:
                        return TimeoffDaysParams
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['TimeoffDaysParams'], typing.List['TimeoffDaysParams']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'timeoff_days':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'TimeoffDaysParams':
                    return super().__getitem__(i)
        
            @staticmethod
            def timeoff_type() -> typing.Type['TimeoffType']:
                return TimeoffType
            timezone = schemas.StrSchema
            __annotations__ = {
                "cancel_reason": cancel_reason,
                "edit_reason": edit_reason,
                "approved_at": approved_at,
                "approver_id": approver_id,
                "document": document,
                "end_date": end_date,
                "notes": notes,
                "start_date": start_date,
                "status": status,
                "timeoff_days": timeoff_days,
                "timeoff_type": timeoff_type,
                "timezone": timezone,
            }
    
    cancel_reason: MetaOapg.properties.cancel_reason
    edit_reason: MetaOapg.properties.edit_reason
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["cancel_reason"]) -> MetaOapg.properties.cancel_reason: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["edit_reason"]) -> MetaOapg.properties.edit_reason: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["approved_at"]) -> MetaOapg.properties.approved_at: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["approver_id"]) -> 'NullableApproverId': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["document"]) -> 'TimeoffDocumentParams': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["end_date"]) -> MetaOapg.properties.end_date: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["notes"]) -> MetaOapg.properties.notes: ...
    
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
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["cancel_reason", "edit_reason", "approved_at", "approver_id", "document", "end_date", "notes", "start_date", "status", "timeoff_days", "timeoff_type", "timezone", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["cancel_reason"]) -> MetaOapg.properties.cancel_reason: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["edit_reason"]) -> MetaOapg.properties.edit_reason: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["approved_at"]) -> typing.Union[MetaOapg.properties.approved_at, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["approver_id"]) -> typing.Union['NullableApproverId', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["document"]) -> typing.Union['TimeoffDocumentParams', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["end_date"]) -> typing.Union[MetaOapg.properties.end_date, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["notes"]) -> typing.Union[MetaOapg.properties.notes, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["start_date"]) -> typing.Union[MetaOapg.properties.start_date, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["status"]) -> typing.Union[MetaOapg.properties.status, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["timeoff_days"]) -> typing.Union[MetaOapg.properties.timeoff_days, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["timeoff_type"]) -> typing.Union['TimeoffType', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["timezone"]) -> typing.Union[MetaOapg.properties.timezone, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["cancel_reason", "edit_reason", "approved_at", "approver_id", "document", "end_date", "notes", "start_date", "status", "timeoff_days", "timeoff_type", "timezone", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        cancel_reason: typing.Union[MetaOapg.properties.cancel_reason, str, ],
        edit_reason: typing.Union[MetaOapg.properties.edit_reason, str, ],
        approved_at: typing.Union[MetaOapg.properties.approved_at, str, datetime, schemas.Unset] = schemas.unset,
        approver_id: typing.Union['NullableApproverId', schemas.Unset] = schemas.unset,
        document: typing.Union['TimeoffDocumentParams', schemas.Unset] = schemas.unset,
        end_date: typing.Union[MetaOapg.properties.end_date, str, date, schemas.Unset] = schemas.unset,
        notes: typing.Union[MetaOapg.properties.notes, str, schemas.Unset] = schemas.unset,
        start_date: typing.Union[MetaOapg.properties.start_date, str, date, schemas.Unset] = schemas.unset,
        status: typing.Union[MetaOapg.properties.status, str, schemas.Unset] = schemas.unset,
        timeoff_days: typing.Union[MetaOapg.properties.timeoff_days, list, tuple, schemas.Unset] = schemas.unset,
        timeoff_type: typing.Union['TimeoffType', schemas.Unset] = schemas.unset,
        timezone: typing.Union[MetaOapg.properties.timezone, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'UpdateApprovedTimeoffParams':
        return super().__new__(
            cls,
            *args,
            cancel_reason=cancel_reason,
            edit_reason=edit_reason,
            approved_at=approved_at,
            approver_id=approver_id,
            document=document,
            end_date=end_date,
            notes=notes,
            start_date=start_date,
            status=status,
            timeoff_days=timeoff_days,
            timeoff_type=timeoff_type,
            timezone=timezone,
            _configuration=_configuration,
            **kwargs,
        )

from remote_python_sdk.model.nullable_approver_id import NullableApproverId
from remote_python_sdk.model.timeoff_days_params import TimeoffDaysParams
from remote_python_sdk.model.timeoff_document_params import TimeoffDocumentParams
from remote_python_sdk.model.timeoff_type import TimeoffType
