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


class CompanyManagersResponseData(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            
            
            class company_managers(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['CompanyManager']:
                        return CompanyManager
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['CompanyManager'], typing.List['CompanyManager']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'company_managers':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'CompanyManager':
                    return super().__getitem__(i)
            current_page = schemas.IntSchema
            total_count = schemas.IntSchema
            total_pages = schemas.IntSchema
            __annotations__ = {
                "company_managers": company_managers,
                "current_page": current_page,
                "total_count": total_count,
                "total_pages": total_pages,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["company_managers"]) -> MetaOapg.properties.company_managers: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["current_page"]) -> MetaOapg.properties.current_page: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["total_count"]) -> MetaOapg.properties.total_count: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["total_pages"]) -> MetaOapg.properties.total_pages: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["company_managers", "current_page", "total_count", "total_pages", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["company_managers"]) -> typing.Union[MetaOapg.properties.company_managers, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["current_page"]) -> typing.Union[MetaOapg.properties.current_page, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["total_count"]) -> typing.Union[MetaOapg.properties.total_count, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["total_pages"]) -> typing.Union[MetaOapg.properties.total_pages, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["company_managers", "current_page", "total_count", "total_pages", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        company_managers: typing.Union[MetaOapg.properties.company_managers, list, tuple, schemas.Unset] = schemas.unset,
        current_page: typing.Union[MetaOapg.properties.current_page, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        total_count: typing.Union[MetaOapg.properties.total_count, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        total_pages: typing.Union[MetaOapg.properties.total_pages, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'CompanyManagersResponseData':
        return super().__new__(
            cls,
            *args,
            company_managers=company_managers,
            current_page=current_page,
            total_count=total_count,
            total_pages=total_pages,
            _configuration=_configuration,
            **kwargs,
        )

from remote_python_sdk.model.company_manager import CompanyManager
