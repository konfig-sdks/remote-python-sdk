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


class CreateWebhookCallbackParamsSubscribedEvents(
    schemas.ListSchema
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        
        class items(
            schemas.EnumBase,
            schemas.StrSchema
        ):
        
        
            class MetaOapg:
                enum_value_to_name = {
                    "billing_document.issued": "BILLING_DOCUMENT_ISSUED",
                    "contract_amendment.canceled": "CONTRACT_AMENDMENT_CANCELED",
                    "contract_amendment.deleted": "CONTRACT_AMENDMENT_DELETED",
                    "contract_amendment.done": "CONTRACT_AMENDMENT_DONE",
                    "contract_amendment.review_started": "CONTRACT_AMENDMENT_REVIEW_STARTED",
                    "contract_amendment.submitted": "CONTRACT_AMENDMENT_SUBMITTED",
                    "employment_contract.active_contract_updated": "EMPLOYMENT_CONTRACT_ACTIVE_CONTRACT_UPDATED",
                    "employment.account.updated": "EMPLOYMENT_ACCOUNT_UPDATED",
                    "employment.details.updated": "EMPLOYMENT_DETAILS_UPDATED",
                    "employment.onboarding_task.completed": "EMPLOYMENT_ONBOARDING_TASK_COMPLETED",
                    "employment.onboarding.completed": "EMPLOYMENT_ONBOARDING_COMPLETED",
                    "employment.personal_information.updated": "EMPLOYMENT_PERSONAL_INFORMATION_UPDATED",
                    "employment.user_status.activated": "EMPLOYMENT_USER_STATUS_ACTIVATED",
                    "employment.user_status.deactivated": "EMPLOYMENT_USER_STATUS_DEACTIVATED",
                    "expense.approved": "EXPENSE_APPROVED",
                    "expense.declined": "EXPENSE_DECLINED",
                    "expense.deleted": "EXPENSE_DELETED",
                    "expense.reimbursed": "EXPENSE_REIMBURSED",
                    "expense.submitted": "EXPENSE_SUBMITTED",
                    "expense.updated": "EXPENSE_UPDATED",
                    "incentive.created": "INCENTIVE_CREATED",
                    "incentive.deleted": "INCENTIVE_DELETED",
                    "incentive.paid": "INCENTIVE_PAID",
                    "incentive.processing_started": "INCENTIVE_PROCESSING_STARTED",
                    "incentive.updated": "INCENTIVE_UPDATED",
                    "offboarding.deleted": "OFFBOARDING_DELETED",
                    "offboarding.done": "OFFBOARDING_DONE",
                    "offboarding.review_started": "OFFBOARDING_REVIEW_STARTED",
                    "offboarding.submitted": "OFFBOARDING_SUBMITTED",
                    "payslip.released": "PAYSLIP_RELEASED",
                    "timeoff.approved": "TIMEOFF_APPROVED",
                    "timeoff.canceled": "TIMEOFF_CANCELED",
                    "timeoff.date_changed": "TIMEOFF_DATE_CHANGED",
                    "timeoff.declined": "TIMEOFF_DECLINED",
                    "timeoff.requested": "TIMEOFF_REQUESTED",
                    "timeoff.taken": "TIMEOFF_TAKEN",
                    "timeoff.updated": "TIMEOFF_UPDATED",
                }
            
            @schemas.classproperty
            def BILLING_DOCUMENT_ISSUED(cls):
                return cls("billing_document.issued")
            
            @schemas.classproperty
            def CONTRACT_AMENDMENT_CANCELED(cls):
                return cls("contract_amendment.canceled")
            
            @schemas.classproperty
            def CONTRACT_AMENDMENT_DELETED(cls):
                return cls("contract_amendment.deleted")
            
            @schemas.classproperty
            def CONTRACT_AMENDMENT_DONE(cls):
                return cls("contract_amendment.done")
            
            @schemas.classproperty
            def CONTRACT_AMENDMENT_REVIEW_STARTED(cls):
                return cls("contract_amendment.review_started")
            
            @schemas.classproperty
            def CONTRACT_AMENDMENT_SUBMITTED(cls):
                return cls("contract_amendment.submitted")
            
            @schemas.classproperty
            def EMPLOYMENT_CONTRACT_ACTIVE_CONTRACT_UPDATED(cls):
                return cls("employment_contract.active_contract_updated")
            
            @schemas.classproperty
            def EMPLOYMENT_ACCOUNT_UPDATED(cls):
                return cls("employment.account.updated")
            
            @schemas.classproperty
            def EMPLOYMENT_DETAILS_UPDATED(cls):
                return cls("employment.details.updated")
            
            @schemas.classproperty
            def EMPLOYMENT_ONBOARDING_TASK_COMPLETED(cls):
                return cls("employment.onboarding_task.completed")
            
            @schemas.classproperty
            def EMPLOYMENT_ONBOARDING_COMPLETED(cls):
                return cls("employment.onboarding.completed")
            
            @schemas.classproperty
            def EMPLOYMENT_PERSONAL_INFORMATION_UPDATED(cls):
                return cls("employment.personal_information.updated")
            
            @schemas.classproperty
            def EMPLOYMENT_USER_STATUS_ACTIVATED(cls):
                return cls("employment.user_status.activated")
            
            @schemas.classproperty
            def EMPLOYMENT_USER_STATUS_DEACTIVATED(cls):
                return cls("employment.user_status.deactivated")
            
            @schemas.classproperty
            def EXPENSE_APPROVED(cls):
                return cls("expense.approved")
            
            @schemas.classproperty
            def EXPENSE_DECLINED(cls):
                return cls("expense.declined")
            
            @schemas.classproperty
            def EXPENSE_DELETED(cls):
                return cls("expense.deleted")
            
            @schemas.classproperty
            def EXPENSE_REIMBURSED(cls):
                return cls("expense.reimbursed")
            
            @schemas.classproperty
            def EXPENSE_SUBMITTED(cls):
                return cls("expense.submitted")
            
            @schemas.classproperty
            def EXPENSE_UPDATED(cls):
                return cls("expense.updated")
            
            @schemas.classproperty
            def INCENTIVE_CREATED(cls):
                return cls("incentive.created")
            
            @schemas.classproperty
            def INCENTIVE_DELETED(cls):
                return cls("incentive.deleted")
            
            @schemas.classproperty
            def INCENTIVE_PAID(cls):
                return cls("incentive.paid")
            
            @schemas.classproperty
            def INCENTIVE_PROCESSING_STARTED(cls):
                return cls("incentive.processing_started")
            
            @schemas.classproperty
            def INCENTIVE_UPDATED(cls):
                return cls("incentive.updated")
            
            @schemas.classproperty
            def OFFBOARDING_DELETED(cls):
                return cls("offboarding.deleted")
            
            @schemas.classproperty
            def OFFBOARDING_DONE(cls):
                return cls("offboarding.done")
            
            @schemas.classproperty
            def OFFBOARDING_REVIEW_STARTED(cls):
                return cls("offboarding.review_started")
            
            @schemas.classproperty
            def OFFBOARDING_SUBMITTED(cls):
                return cls("offboarding.submitted")
            
            @schemas.classproperty
            def PAYSLIP_RELEASED(cls):
                return cls("payslip.released")
            
            @schemas.classproperty
            def TIMEOFF_APPROVED(cls):
                return cls("timeoff.approved")
            
            @schemas.classproperty
            def TIMEOFF_CANCELED(cls):
                return cls("timeoff.canceled")
            
            @schemas.classproperty
            def TIMEOFF_DATE_CHANGED(cls):
                return cls("timeoff.date_changed")
            
            @schemas.classproperty
            def TIMEOFF_DECLINED(cls):
                return cls("timeoff.declined")
            
            @schemas.classproperty
            def TIMEOFF_REQUESTED(cls):
                return cls("timeoff.requested")
            
            @schemas.classproperty
            def TIMEOFF_TAKEN(cls):
                return cls("timeoff.taken")
            
            @schemas.classproperty
            def TIMEOFF_UPDATED(cls):
                return cls("timeoff.updated")

    def __new__(
        cls,
        arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'CreateWebhookCallbackParamsSubscribedEvents':
        return super().__new__(
            cls,
            arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> MetaOapg.items:
        return super().__getitem__(i)
