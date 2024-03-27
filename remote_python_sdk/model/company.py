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


class Company(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "country_code",
            "terms_of_service_accepted_at",
            "desired_currency",
            "updated_at",
            "address_details",
            "name",
            "created_at",
            "company_owner_email",
            "id",
            "status",
        }
        
        class properties:
            address_details = schemas.DictSchema
            company_owner_email = schemas.StrSchema
            country_code = schemas.StrSchema
            created_at = schemas.DateTimeSchema
            desired_currency = schemas.StrSchema
            id = schemas.StrSchema
            name = schemas.StrSchema
            
            
            class status(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "pending": "PENDING",
                        "review": "REVIEW",
                        "active": "ACTIVE",
                        "archived": "ARCHIVED",
                    }
                
                @schemas.classproperty
                def PENDING(cls):
                    return cls("pending")
                
                @schemas.classproperty
                def REVIEW(cls):
                    return cls("review")
                
                @schemas.classproperty
                def ACTIVE(cls):
                    return cls("active")
                
                @schemas.classproperty
                def ARCHIVED(cls):
                    return cls("archived")
            terms_of_service_accepted_at = schemas.DateTimeSchema
            updated_at = schemas.DateTimeSchema
            bank_account_details = schemas.DictSchema
            company_owner_name = schemas.StrSchema
            
            
            class external_id(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'external_id':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            phone_number = schemas.StrSchema
            
            
            class registration_number(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'registration_number':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class tax_number(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'tax_number':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            __annotations__ = {
                "address_details": address_details,
                "company_owner_email": company_owner_email,
                "country_code": country_code,
                "created_at": created_at,
                "desired_currency": desired_currency,
                "id": id,
                "name": name,
                "status": status,
                "terms_of_service_accepted_at": terms_of_service_accepted_at,
                "updated_at": updated_at,
                "bank_account_details": bank_account_details,
                "company_owner_name": company_owner_name,
                "external_id": external_id,
                "phone_number": phone_number,
                "registration_number": registration_number,
                "tax_number": tax_number,
            }
    
    country_code: MetaOapg.properties.country_code
    terms_of_service_accepted_at: MetaOapg.properties.terms_of_service_accepted_at
    desired_currency: MetaOapg.properties.desired_currency
    updated_at: MetaOapg.properties.updated_at
    address_details: MetaOapg.properties.address_details
    name: MetaOapg.properties.name
    created_at: MetaOapg.properties.created_at
    company_owner_email: MetaOapg.properties.company_owner_email
    id: MetaOapg.properties.id
    status: MetaOapg.properties.status
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["address_details"]) -> MetaOapg.properties.address_details: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["company_owner_email"]) -> MetaOapg.properties.company_owner_email: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["country_code"]) -> MetaOapg.properties.country_code: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["created_at"]) -> MetaOapg.properties.created_at: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["desired_currency"]) -> MetaOapg.properties.desired_currency: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["terms_of_service_accepted_at"]) -> MetaOapg.properties.terms_of_service_accepted_at: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["updated_at"]) -> MetaOapg.properties.updated_at: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["bank_account_details"]) -> MetaOapg.properties.bank_account_details: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["company_owner_name"]) -> MetaOapg.properties.company_owner_name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["external_id"]) -> MetaOapg.properties.external_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["phone_number"]) -> MetaOapg.properties.phone_number: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["registration_number"]) -> MetaOapg.properties.registration_number: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["tax_number"]) -> MetaOapg.properties.tax_number: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["address_details", "company_owner_email", "country_code", "created_at", "desired_currency", "id", "name", "status", "terms_of_service_accepted_at", "updated_at", "bank_account_details", "company_owner_name", "external_id", "phone_number", "registration_number", "tax_number", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["address_details"]) -> MetaOapg.properties.address_details: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["company_owner_email"]) -> MetaOapg.properties.company_owner_email: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["country_code"]) -> MetaOapg.properties.country_code: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["created_at"]) -> MetaOapg.properties.created_at: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["desired_currency"]) -> MetaOapg.properties.desired_currency: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["terms_of_service_accepted_at"]) -> MetaOapg.properties.terms_of_service_accepted_at: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["updated_at"]) -> MetaOapg.properties.updated_at: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["bank_account_details"]) -> typing.Union[MetaOapg.properties.bank_account_details, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["company_owner_name"]) -> typing.Union[MetaOapg.properties.company_owner_name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["external_id"]) -> typing.Union[MetaOapg.properties.external_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["phone_number"]) -> typing.Union[MetaOapg.properties.phone_number, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["registration_number"]) -> typing.Union[MetaOapg.properties.registration_number, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["tax_number"]) -> typing.Union[MetaOapg.properties.tax_number, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["address_details", "company_owner_email", "country_code", "created_at", "desired_currency", "id", "name", "status", "terms_of_service_accepted_at", "updated_at", "bank_account_details", "company_owner_name", "external_id", "phone_number", "registration_number", "tax_number", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        country_code: typing.Union[MetaOapg.properties.country_code, str, ],
        terms_of_service_accepted_at: typing.Union[MetaOapg.properties.terms_of_service_accepted_at, str, datetime, ],
        desired_currency: typing.Union[MetaOapg.properties.desired_currency, str, ],
        updated_at: typing.Union[MetaOapg.properties.updated_at, str, datetime, ],
        address_details: typing.Union[MetaOapg.properties.address_details, dict, frozendict.frozendict, ],
        name: typing.Union[MetaOapg.properties.name, str, ],
        created_at: typing.Union[MetaOapg.properties.created_at, str, datetime, ],
        company_owner_email: typing.Union[MetaOapg.properties.company_owner_email, str, ],
        id: typing.Union[MetaOapg.properties.id, str, ],
        status: typing.Union[MetaOapg.properties.status, str, ],
        bank_account_details: typing.Union[MetaOapg.properties.bank_account_details, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        company_owner_name: typing.Union[MetaOapg.properties.company_owner_name, str, schemas.Unset] = schemas.unset,
        external_id: typing.Union[MetaOapg.properties.external_id, None, str, schemas.Unset] = schemas.unset,
        phone_number: typing.Union[MetaOapg.properties.phone_number, str, schemas.Unset] = schemas.unset,
        registration_number: typing.Union[MetaOapg.properties.registration_number, None, str, schemas.Unset] = schemas.unset,
        tax_number: typing.Union[MetaOapg.properties.tax_number, None, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Company':
        return super().__new__(
            cls,
            *args,
            country_code=country_code,
            terms_of_service_accepted_at=terms_of_service_accepted_at,
            desired_currency=desired_currency,
            updated_at=updated_at,
            address_details=address_details,
            name=name,
            created_at=created_at,
            company_owner_email=company_owner_email,
            id=id,
            status=status,
            bank_account_details=bank_account_details,
            company_owner_name=company_owner_name,
            external_id=external_id,
            phone_number=phone_number,
            registration_number=registration_number,
            tax_number=tax_number,
            _configuration=_configuration,
            **kwargs,
        )