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


class Employment(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Complete information of an employment
    """


    class MetaOapg:
        required = {
            "bank_account_details",
            "country",
            "company_id",
            "emergency_contact_details",
            "pricing_plan_details",
            "created_at",
            "personal_details",
            "type",
            "administrative_details",
            "billing_address_details",
            "full_name",
            "updated_at",
            "address_details",
            "contract_details",
            "files",
            "id",
            "onboarding_tasks",
            "job_title",
            "employment_lifecycle_stage",
            "personal_email",
            "status",
        }
        
        class properties:
            address_details = schemas.DictSchema
            administrative_details = schemas.DictSchema
        
            @staticmethod
            def bank_account_details() -> typing.Type['EmploymentBankAccountDetails']:
                return EmploymentBankAccountDetails
            billing_address_details = schemas.DictSchema
            company_id = schemas.StrSchema
            contract_details = schemas.DictSchema
        
            @staticmethod
            def country() -> typing.Type['Country']:
                return Country
            created_at = schemas.StrSchema
            emergency_contact_details = schemas.DictSchema
        
            @staticmethod
            def employment_lifecycle_stage() -> typing.Type['EmploymentLifecycleStage']:
                return EmploymentLifecycleStage
            
            
            class files(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['File']:
                        return File
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['File'], typing.List['File']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'files':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'File':
                    return super().__getitem__(i)
            full_name = schemas.StrSchema
            id = schemas.StrSchema
            job_title = schemas.StrSchema
        
            @staticmethod
            def onboarding_tasks() -> typing.Type['OnboardingTasks']:
                return OnboardingTasks
            personal_details = schemas.DictSchema
            personal_email = schemas.StrSchema
        
            @staticmethod
            def pricing_plan_details() -> typing.Type['PricingPlanDetails']:
                return PricingPlanDetails
        
            @staticmethod
            def status() -> typing.Type['EmploymentStatus']:
                return EmploymentStatus
            
            
            class type(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def EMPLOYEE(cls):
                    return cls("employee")
                
                @schemas.classproperty
                def CONTRACTOR(cls):
                    return cls("contractor")
                
                @schemas.classproperty
                def DIRECT_EMPLOYEE(cls):
                    return cls("direct_employee")
                
                @schemas.classproperty
                def GLOBAL_PAYROLL_EMPLOYEE(cls):
                    return cls("global_payroll_employee")
            updated_at = schemas.DateTimeSchema
            active_contract_id = schemas.StrSchema
            basic_information = schemas.DictSchema
            
            
            class department(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'department':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class department_id(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'department_id':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            manager = schemas.StrSchema
            probation_period_end_date = schemas.DateSchema
            provisional_start_date = schemas.DateSchema
            seniority_date = schemas.DateTimeSchema
        
            @staticmethod
            def user_status() -> typing.Type['UserStatus']:
                return UserStatus
            __annotations__ = {
                "address_details": address_details,
                "administrative_details": administrative_details,
                "bank_account_details": bank_account_details,
                "billing_address_details": billing_address_details,
                "company_id": company_id,
                "contract_details": contract_details,
                "country": country,
                "created_at": created_at,
                "emergency_contact_details": emergency_contact_details,
                "employment_lifecycle_stage": employment_lifecycle_stage,
                "files": files,
                "full_name": full_name,
                "id": id,
                "job_title": job_title,
                "onboarding_tasks": onboarding_tasks,
                "personal_details": personal_details,
                "personal_email": personal_email,
                "pricing_plan_details": pricing_plan_details,
                "status": status,
                "type": type,
                "updated_at": updated_at,
                "active_contract_id": active_contract_id,
                "basic_information": basic_information,
                "department": department,
                "department_id": department_id,
                "manager": manager,
                "probation_period_end_date": probation_period_end_date,
                "provisional_start_date": provisional_start_date,
                "seniority_date": seniority_date,
                "user_status": user_status,
            }
    
    bank_account_details: 'EmploymentBankAccountDetails'
    country: 'Country'
    company_id: MetaOapg.properties.company_id
    emergency_contact_details: MetaOapg.properties.emergency_contact_details
    pricing_plan_details: 'PricingPlanDetails'
    created_at: MetaOapg.properties.created_at
    personal_details: MetaOapg.properties.personal_details
    type: MetaOapg.properties.type
    administrative_details: MetaOapg.properties.administrative_details
    billing_address_details: MetaOapg.properties.billing_address_details
    full_name: MetaOapg.properties.full_name
    updated_at: MetaOapg.properties.updated_at
    address_details: MetaOapg.properties.address_details
    contract_details: MetaOapg.properties.contract_details
    files: MetaOapg.properties.files
    id: MetaOapg.properties.id
    onboarding_tasks: 'OnboardingTasks'
    job_title: MetaOapg.properties.job_title
    employment_lifecycle_stage: 'EmploymentLifecycleStage'
    personal_email: MetaOapg.properties.personal_email
    status: 'EmploymentStatus'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["address_details"]) -> MetaOapg.properties.address_details: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["administrative_details"]) -> MetaOapg.properties.administrative_details: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["bank_account_details"]) -> 'EmploymentBankAccountDetails': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["billing_address_details"]) -> MetaOapg.properties.billing_address_details: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["company_id"]) -> MetaOapg.properties.company_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["contract_details"]) -> MetaOapg.properties.contract_details: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["country"]) -> 'Country': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["created_at"]) -> MetaOapg.properties.created_at: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["emergency_contact_details"]) -> MetaOapg.properties.emergency_contact_details: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["employment_lifecycle_stage"]) -> 'EmploymentLifecycleStage': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["files"]) -> MetaOapg.properties.files: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["full_name"]) -> MetaOapg.properties.full_name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["job_title"]) -> MetaOapg.properties.job_title: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["onboarding_tasks"]) -> 'OnboardingTasks': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["personal_details"]) -> MetaOapg.properties.personal_details: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["personal_email"]) -> MetaOapg.properties.personal_email: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["pricing_plan_details"]) -> 'PricingPlanDetails': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["status"]) -> 'EmploymentStatus': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["updated_at"]) -> MetaOapg.properties.updated_at: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["active_contract_id"]) -> MetaOapg.properties.active_contract_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["basic_information"]) -> MetaOapg.properties.basic_information: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["department"]) -> MetaOapg.properties.department: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["department_id"]) -> MetaOapg.properties.department_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["manager"]) -> MetaOapg.properties.manager: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["probation_period_end_date"]) -> MetaOapg.properties.probation_period_end_date: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["provisional_start_date"]) -> MetaOapg.properties.provisional_start_date: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["seniority_date"]) -> MetaOapg.properties.seniority_date: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["user_status"]) -> 'UserStatus': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["address_details", "administrative_details", "bank_account_details", "billing_address_details", "company_id", "contract_details", "country", "created_at", "emergency_contact_details", "employment_lifecycle_stage", "files", "full_name", "id", "job_title", "onboarding_tasks", "personal_details", "personal_email", "pricing_plan_details", "status", "type", "updated_at", "active_contract_id", "basic_information", "department", "department_id", "manager", "probation_period_end_date", "provisional_start_date", "seniority_date", "user_status", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["address_details"]) -> MetaOapg.properties.address_details: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["administrative_details"]) -> MetaOapg.properties.administrative_details: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["bank_account_details"]) -> 'EmploymentBankAccountDetails': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["billing_address_details"]) -> MetaOapg.properties.billing_address_details: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["company_id"]) -> MetaOapg.properties.company_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["contract_details"]) -> MetaOapg.properties.contract_details: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["country"]) -> 'Country': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["created_at"]) -> MetaOapg.properties.created_at: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["emergency_contact_details"]) -> MetaOapg.properties.emergency_contact_details: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["employment_lifecycle_stage"]) -> 'EmploymentLifecycleStage': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["files"]) -> MetaOapg.properties.files: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["full_name"]) -> MetaOapg.properties.full_name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["job_title"]) -> MetaOapg.properties.job_title: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["onboarding_tasks"]) -> 'OnboardingTasks': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["personal_details"]) -> MetaOapg.properties.personal_details: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["personal_email"]) -> MetaOapg.properties.personal_email: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["pricing_plan_details"]) -> 'PricingPlanDetails': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["status"]) -> 'EmploymentStatus': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["updated_at"]) -> MetaOapg.properties.updated_at: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["active_contract_id"]) -> typing.Union[MetaOapg.properties.active_contract_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["basic_information"]) -> typing.Union[MetaOapg.properties.basic_information, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["department"]) -> typing.Union[MetaOapg.properties.department, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["department_id"]) -> typing.Union[MetaOapg.properties.department_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["manager"]) -> typing.Union[MetaOapg.properties.manager, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["probation_period_end_date"]) -> typing.Union[MetaOapg.properties.probation_period_end_date, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["provisional_start_date"]) -> typing.Union[MetaOapg.properties.provisional_start_date, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["seniority_date"]) -> typing.Union[MetaOapg.properties.seniority_date, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["user_status"]) -> typing.Union['UserStatus', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["address_details", "administrative_details", "bank_account_details", "billing_address_details", "company_id", "contract_details", "country", "created_at", "emergency_contact_details", "employment_lifecycle_stage", "files", "full_name", "id", "job_title", "onboarding_tasks", "personal_details", "personal_email", "pricing_plan_details", "status", "type", "updated_at", "active_contract_id", "basic_information", "department", "department_id", "manager", "probation_period_end_date", "provisional_start_date", "seniority_date", "user_status", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        bank_account_details: 'EmploymentBankAccountDetails',
        country: 'Country',
        company_id: typing.Union[MetaOapg.properties.company_id, str, ],
        emergency_contact_details: typing.Union[MetaOapg.properties.emergency_contact_details, dict, frozendict.frozendict, ],
        pricing_plan_details: 'PricingPlanDetails',
        created_at: typing.Union[MetaOapg.properties.created_at, str, ],
        personal_details: typing.Union[MetaOapg.properties.personal_details, dict, frozendict.frozendict, ],
        type: typing.Union[MetaOapg.properties.type, str, ],
        administrative_details: typing.Union[MetaOapg.properties.administrative_details, dict, frozendict.frozendict, ],
        billing_address_details: typing.Union[MetaOapg.properties.billing_address_details, dict, frozendict.frozendict, ],
        full_name: typing.Union[MetaOapg.properties.full_name, str, ],
        updated_at: typing.Union[MetaOapg.properties.updated_at, str, datetime, ],
        address_details: typing.Union[MetaOapg.properties.address_details, dict, frozendict.frozendict, ],
        contract_details: typing.Union[MetaOapg.properties.contract_details, dict, frozendict.frozendict, ],
        files: typing.Union[MetaOapg.properties.files, list, tuple, ],
        id: typing.Union[MetaOapg.properties.id, str, ],
        onboarding_tasks: 'OnboardingTasks',
        job_title: typing.Union[MetaOapg.properties.job_title, str, ],
        employment_lifecycle_stage: 'EmploymentLifecycleStage',
        personal_email: typing.Union[MetaOapg.properties.personal_email, str, ],
        status: 'EmploymentStatus',
        active_contract_id: typing.Union[MetaOapg.properties.active_contract_id, str, schemas.Unset] = schemas.unset,
        basic_information: typing.Union[MetaOapg.properties.basic_information, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        department: typing.Union[MetaOapg.properties.department, None, str, schemas.Unset] = schemas.unset,
        department_id: typing.Union[MetaOapg.properties.department_id, None, str, schemas.Unset] = schemas.unset,
        manager: typing.Union[MetaOapg.properties.manager, str, schemas.Unset] = schemas.unset,
        probation_period_end_date: typing.Union[MetaOapg.properties.probation_period_end_date, str, date, schemas.Unset] = schemas.unset,
        provisional_start_date: typing.Union[MetaOapg.properties.provisional_start_date, str, date, schemas.Unset] = schemas.unset,
        seniority_date: typing.Union[MetaOapg.properties.seniority_date, str, datetime, schemas.Unset] = schemas.unset,
        user_status: typing.Union['UserStatus', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Employment':
        return super().__new__(
            cls,
            *args,
            bank_account_details=bank_account_details,
            country=country,
            company_id=company_id,
            emergency_contact_details=emergency_contact_details,
            pricing_plan_details=pricing_plan_details,
            created_at=created_at,
            personal_details=personal_details,
            type=type,
            administrative_details=administrative_details,
            billing_address_details=billing_address_details,
            full_name=full_name,
            updated_at=updated_at,
            address_details=address_details,
            contract_details=contract_details,
            files=files,
            id=id,
            onboarding_tasks=onboarding_tasks,
            job_title=job_title,
            employment_lifecycle_stage=employment_lifecycle_stage,
            personal_email=personal_email,
            status=status,
            active_contract_id=active_contract_id,
            basic_information=basic_information,
            department=department,
            department_id=department_id,
            manager=manager,
            probation_period_end_date=probation_period_end_date,
            provisional_start_date=provisional_start_date,
            seniority_date=seniority_date,
            user_status=user_status,
            _configuration=_configuration,
            **kwargs,
        )

from remote_python_sdk.model.country import Country
from remote_python_sdk.model.employment_bank_account_details import EmploymentBankAccountDetails
from remote_python_sdk.model.employment_lifecycle_stage import EmploymentLifecycleStage
from remote_python_sdk.model.employment_status import EmploymentStatus
from remote_python_sdk.model.file import File
from remote_python_sdk.model.onboarding_tasks import OnboardingTasks
from remote_python_sdk.model.pricing_plan_details import PricingPlanDetails
from remote_python_sdk.model.user_status import UserStatus