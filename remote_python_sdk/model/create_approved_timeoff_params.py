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


class CreateApprovedTimeoffParams(
    schemas.ComposedBase,
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Approved timeoff creation params
    """


    class MetaOapg:
        required = {
            "approved_at",
            "approver_id",
            "status",
        }
        
        
        class all_of_1(
            schemas.DictSchema
        ):
        
        
            class MetaOapg:
                
                class properties:
                    approved_at = schemas.DateTimeSchema
                
                    @staticmethod
                    def approver_id() -> typing.Type['NullableApproverId']:
                        return NullableApproverId
                    
                    
                    class status(
                        schemas.EnumBase,
                        schemas.StrSchema
                    ):
                    
                    
                        class MetaOapg:
                            enum_value_to_name = {
                                "approved": "APPROVED",
                            }
                        
                        @schemas.classproperty
                        def APPROVED(cls):
                            return cls("approved")
                    __annotations__ = {
                        "approved_at": approved_at,
                        "approver_id": approver_id,
                        "status": status,
                    }
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["approved_at"]) -> MetaOapg.properties.approved_at: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["approver_id"]) -> 'NullableApproverId': ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
            
            @typing.overload
            def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
            
            def __getitem__(self, name: typing.Union[typing_extensions.Literal["approved_at", "approver_id", "status", ], str]):
                # dict_instance[name] accessor
                return super().__getitem__(name)
            
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["approved_at"]) -> typing.Union[MetaOapg.properties.approved_at, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["approver_id"]) -> typing.Union['NullableApproverId', schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["status"]) -> typing.Union[MetaOapg.properties.status, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
            
            def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["approved_at", "approver_id", "status", ], str]):
                return super().get_item_oapg(name)
            
        
            def __new__(
                cls,
                *args: typing.Union[dict, frozendict.frozendict, ],
                approved_at: typing.Union[MetaOapg.properties.approved_at, str, datetime, schemas.Unset] = schemas.unset,
                approver_id: typing.Union['NullableApproverId', schemas.Unset] = schemas.unset,
                status: typing.Union[MetaOapg.properties.status, str, schemas.Unset] = schemas.unset,
                _configuration: typing.Optional[schemas.Configuration] = None,
                **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
            ) -> 'all_of_1':
                return super().__new__(
                    cls,
                    *args,
                    approved_at=approved_at,
                    approver_id=approver_id,
                    status=status,
                    _configuration=_configuration,
                    **kwargs,
                )
        
        @classmethod
        @functools.lru_cache()
        def all_of(cls):
            # we need this here to make our import statements work
            # we must store _composed_schemas in here so the code is only run
            # when we invoke this method. If we kept this at the class
            # level we would get an error because the class level
            # code would be run when this module is imported, and these composed
            # classes don't exist yet because their module has not finished
            # loading
            return [
                CreateTimeoffParams,
                cls.all_of_1,
            ]

    
    approved_at: schemas.AnyTypeSchema
    approver_id: schemas.AnyTypeSchema
    status: schemas.AnyTypeSchema

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'CreateApprovedTimeoffParams':
        return super().__new__(
            cls,
            *args,
            _configuration=_configuration,
            **kwargs,
        )

from remote_python_sdk.model.create_timeoff_params import CreateTimeoffParams
from remote_python_sdk.model.nullable_approver_id import NullableApproverId