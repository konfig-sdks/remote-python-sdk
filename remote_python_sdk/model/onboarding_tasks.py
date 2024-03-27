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


class OnboardingTasks(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    All tasks that need to be completed before marking the employment as ready
    """


    class MetaOapg:
        required = {
            "bank_account_details",
            "emergency_contact_details",
            "employment_document_details",
            "pricing_plan_details",
            "address_details",
            "contract_details",
            "personal_details",
            "administrative_details",
            "billing_address_details",
        }
        
        class properties:
        
            @staticmethod
            def address_details() -> typing.Type['TaskDescription']:
                return TaskDescription
        
            @staticmethod
            def administrative_details() -> typing.Type['TaskDescription']:
                return TaskDescription
        
            @staticmethod
            def bank_account_details() -> typing.Type['TaskDescription']:
                return TaskDescription
        
            @staticmethod
            def billing_address_details() -> typing.Type['TaskDescription']:
                return TaskDescription
        
            @staticmethod
            def contract_details() -> typing.Type['TaskDescription']:
                return TaskDescription
        
            @staticmethod
            def emergency_contact_details() -> typing.Type['TaskDescription']:
                return TaskDescription
        
            @staticmethod
            def employment_document_details() -> typing.Type['TaskDescription']:
                return TaskDescription
        
            @staticmethod
            def personal_details() -> typing.Type['TaskDescription']:
                return TaskDescription
        
            @staticmethod
            def pricing_plan_details() -> typing.Type['TaskDescription']:
                return TaskDescription
            __annotations__ = {
                "address_details": address_details,
                "administrative_details": administrative_details,
                "bank_account_details": bank_account_details,
                "billing_address_details": billing_address_details,
                "contract_details": contract_details,
                "emergency_contact_details": emergency_contact_details,
                "employment_document_details": employment_document_details,
                "personal_details": personal_details,
                "pricing_plan_details": pricing_plan_details,
            }
    
    bank_account_details: 'TaskDescription'
    emergency_contact_details: 'TaskDescription'
    employment_document_details: 'TaskDescription'
    pricing_plan_details: 'TaskDescription'
    address_details: 'TaskDescription'
    contract_details: 'TaskDescription'
    personal_details: 'TaskDescription'
    administrative_details: 'TaskDescription'
    billing_address_details: 'TaskDescription'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["address_details"]) -> 'TaskDescription': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["administrative_details"]) -> 'TaskDescription': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["bank_account_details"]) -> 'TaskDescription': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["billing_address_details"]) -> 'TaskDescription': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["contract_details"]) -> 'TaskDescription': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["emergency_contact_details"]) -> 'TaskDescription': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["employment_document_details"]) -> 'TaskDescription': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["personal_details"]) -> 'TaskDescription': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["pricing_plan_details"]) -> 'TaskDescription': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["address_details", "administrative_details", "bank_account_details", "billing_address_details", "contract_details", "emergency_contact_details", "employment_document_details", "personal_details", "pricing_plan_details", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["address_details"]) -> 'TaskDescription': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["administrative_details"]) -> 'TaskDescription': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["bank_account_details"]) -> 'TaskDescription': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["billing_address_details"]) -> 'TaskDescription': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["contract_details"]) -> 'TaskDescription': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["emergency_contact_details"]) -> 'TaskDescription': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["employment_document_details"]) -> 'TaskDescription': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["personal_details"]) -> 'TaskDescription': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["pricing_plan_details"]) -> 'TaskDescription': ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["address_details", "administrative_details", "bank_account_details", "billing_address_details", "contract_details", "emergency_contact_details", "employment_document_details", "personal_details", "pricing_plan_details", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        bank_account_details: 'TaskDescription',
        emergency_contact_details: 'TaskDescription',
        employment_document_details: 'TaskDescription',
        pricing_plan_details: 'TaskDescription',
        address_details: 'TaskDescription',
        contract_details: 'TaskDescription',
        personal_details: 'TaskDescription',
        administrative_details: 'TaskDescription',
        billing_address_details: 'TaskDescription',
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'OnboardingTasks':
        return super().__new__(
            cls,
            *args,
            bank_account_details=bank_account_details,
            emergency_contact_details=emergency_contact_details,
            employment_document_details=employment_document_details,
            pricing_plan_details=pricing_plan_details,
            address_details=address_details,
            contract_details=contract_details,
            personal_details=personal_details,
            administrative_details=administrative_details,
            billing_address_details=billing_address_details,
            _configuration=_configuration,
            **kwargs,
        )

from remote_python_sdk.model.task_description import TaskDescription
