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


class TerminationOffboarding(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "submitted_at",
            "termination_reason",
            "reason_description",
            "type",
            "additional_comments",
            "employment_id",
            "requested_by",
            "proposed_termination_date",
            "termination_date",
            "risk_assessment_reasons",
            "id",
            "will_challenge_termination",
            "confidential",
            "status",
        }
        
        class properties:
            additional_comments = schemas.StrSchema
            confidential = schemas.BoolSchema
            employment_id = schemas.StrSchema
            id = schemas.StrSchema
            proposed_termination_date = schemas.DateSchema
            reason_description = schemas.StrSchema
            requested_by = schemas.StrSchema
        
            @staticmethod
            def risk_assessment_reasons() -> typing.Type['TerminationOffboardingRiskAssessmentReasons']:
                return TerminationOffboardingRiskAssessmentReasons
            
            
            class status(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def SUBMITTED(cls):
                    return cls("submitted")
                
                @schemas.classproperty
                def IN_REVIEW(cls):
                    return cls("in_review")
                
                @schemas.classproperty
                def DONE(cls):
                    return cls("done")
                
                @schemas.classproperty
                def CANCELED(cls):
                    return cls("canceled")
            submitted_at = schemas.StrSchema
            
            
            class termination_date(
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
                ) -> 'termination_date':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class termination_reason(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def CANCELLATION_BEFORE_START_DATE(cls):
                    return cls("cancellation_before_start_date")
                
                @schemas.classproperty
                def COMPLIANCE_ISSUE(cls):
                    return cls("compliance_issue")
                
                @schemas.classproperty
                def CONVERSION_TO_CONTRACTOR(cls):
                    return cls("conversion_to_contractor")
                
                @schemas.classproperty
                def DISSATISFACTION_WITH_REMOTE_SERVICE(cls):
                    return cls("dissatisfaction_with_remote_service")
                
                @schemas.classproperty
                def END_OF_FIXED_TERM_CONTRACT_COMPLIANCE_ISSUE(cls):
                    return cls("end_of_fixed_term_contract_compliance_issue")
                
                @schemas.classproperty
                def END_OF_FIXED_TERM_CONTRACT_INCAPACITY_TO_PERFORM_INHERENT_DUTIES(cls):
                    return cls("end_of_fixed_term_contract_incapacity_to_perform_inherent_duties")
                
                @schemas.classproperty
                def END_OF_FIXED_TERM_CONTRACT_LOCAL_REGULATIONS_MAX_TERM_REACHED(cls):
                    return cls("end_of_fixed_term_contract_local_regulations_max_term_reached")
                
                @schemas.classproperty
                def END_OF_FIXED_TERM_CONTRACT_MISCONDUCT(cls):
                    return cls("end_of_fixed_term_contract_misconduct")
                
                @schemas.classproperty
                def END_OF_FIXED_TERM_CONTRACT_OPERATIONAL_REASONS(cls):
                    return cls("end_of_fixed_term_contract_operational_reasons")
                
                @schemas.classproperty
                def END_OF_FIXED_TERM_CONTRACT_OTHER(cls):
                    return cls("end_of_fixed_term_contract_other")
                
                @schemas.classproperty
                def END_OF_FIXED_TERM_CONTRACT_PERFORMANCE(cls):
                    return cls("end_of_fixed_term_contract_performance")
                
                @schemas.classproperty
                def END_OF_FIXED_TERM_CONTRACT_REDUNDANCY(cls):
                    return cls("end_of_fixed_term_contract_redundancy")
                
                @schemas.classproperty
                def END_OF_FIXED_TERM_CONTRACT_VALUES(cls):
                    return cls("end_of_fixed_term_contract_values")
                
                @schemas.classproperty
                def GROSS_MISCONDUCT(cls):
                    return cls("gross_misconduct")
                
                @schemas.classproperty
                def INCAPACITY_TO_PERFORM_INHERENT_DUTIES(cls):
                    return cls("incapacity_to_perform_inherent_duties")
                
                @schemas.classproperty
                def JOB_ABANDONMENT(cls):
                    return cls("job_abandonment")
                
                @schemas.classproperty
                def MUTUAL_AGREEMENT(cls):
                    return cls("mutual_agreement")
                
                @schemas.classproperty
                def OTHER(cls):
                    return cls("other")
                
                @schemas.classproperty
                def PERFORMANCE(cls):
                    return cls("performance")
                
                @schemas.classproperty
                def VALUES(cls):
                    return cls("values")
                
                @schemas.classproperty
                def WORKFORCE_REDUCTION(cls):
                    return cls("workforce_reduction")
            
            
            class type(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def TERMINATION(cls):
                    return cls("termination")
            will_challenge_termination = schemas.BoolSchema
            agrees_to_pto_amount = schemas.StrSchema
        
            @staticmethod
            def employee_awareness() -> typing.Type['TerminationOffboardingEmployeeAwareness']:
                return TerminationOffboardingEmployeeAwareness
            will_challenge_termination_description = schemas.StrSchema
            __annotations__ = {
                "additional_comments": additional_comments,
                "confidential": confidential,
                "employment_id": employment_id,
                "id": id,
                "proposed_termination_date": proposed_termination_date,
                "reason_description": reason_description,
                "requested_by": requested_by,
                "risk_assessment_reasons": risk_assessment_reasons,
                "status": status,
                "submitted_at": submitted_at,
                "termination_date": termination_date,
                "termination_reason": termination_reason,
                "type": type,
                "will_challenge_termination": will_challenge_termination,
                "agrees_to_pto_amount": agrees_to_pto_amount,
                "employee_awareness": employee_awareness,
                "will_challenge_termination_description": will_challenge_termination_description,
            }
    
    submitted_at: MetaOapg.properties.submitted_at
    termination_reason: MetaOapg.properties.termination_reason
    reason_description: MetaOapg.properties.reason_description
    type: MetaOapg.properties.type
    additional_comments: MetaOapg.properties.additional_comments
    employment_id: MetaOapg.properties.employment_id
    requested_by: MetaOapg.properties.requested_by
    proposed_termination_date: MetaOapg.properties.proposed_termination_date
    termination_date: MetaOapg.properties.termination_date
    risk_assessment_reasons: 'TerminationOffboardingRiskAssessmentReasons'
    id: MetaOapg.properties.id
    will_challenge_termination: MetaOapg.properties.will_challenge_termination
    confidential: MetaOapg.properties.confidential
    status: MetaOapg.properties.status
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["additional_comments"]) -> MetaOapg.properties.additional_comments: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["confidential"]) -> MetaOapg.properties.confidential: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["employment_id"]) -> MetaOapg.properties.employment_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["proposed_termination_date"]) -> MetaOapg.properties.proposed_termination_date: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["reason_description"]) -> MetaOapg.properties.reason_description: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["requested_by"]) -> MetaOapg.properties.requested_by: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["risk_assessment_reasons"]) -> 'TerminationOffboardingRiskAssessmentReasons': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["submitted_at"]) -> MetaOapg.properties.submitted_at: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["termination_date"]) -> MetaOapg.properties.termination_date: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["termination_reason"]) -> MetaOapg.properties.termination_reason: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["will_challenge_termination"]) -> MetaOapg.properties.will_challenge_termination: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["agrees_to_pto_amount"]) -> MetaOapg.properties.agrees_to_pto_amount: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["employee_awareness"]) -> 'TerminationOffboardingEmployeeAwareness': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["will_challenge_termination_description"]) -> MetaOapg.properties.will_challenge_termination_description: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["additional_comments", "confidential", "employment_id", "id", "proposed_termination_date", "reason_description", "requested_by", "risk_assessment_reasons", "status", "submitted_at", "termination_date", "termination_reason", "type", "will_challenge_termination", "agrees_to_pto_amount", "employee_awareness", "will_challenge_termination_description", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["additional_comments"]) -> MetaOapg.properties.additional_comments: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["confidential"]) -> MetaOapg.properties.confidential: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["employment_id"]) -> MetaOapg.properties.employment_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["proposed_termination_date"]) -> MetaOapg.properties.proposed_termination_date: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["reason_description"]) -> MetaOapg.properties.reason_description: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["requested_by"]) -> MetaOapg.properties.requested_by: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["risk_assessment_reasons"]) -> 'TerminationOffboardingRiskAssessmentReasons': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["submitted_at"]) -> MetaOapg.properties.submitted_at: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["termination_date"]) -> MetaOapg.properties.termination_date: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["termination_reason"]) -> MetaOapg.properties.termination_reason: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["will_challenge_termination"]) -> MetaOapg.properties.will_challenge_termination: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["agrees_to_pto_amount"]) -> typing.Union[MetaOapg.properties.agrees_to_pto_amount, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["employee_awareness"]) -> typing.Union['TerminationOffboardingEmployeeAwareness', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["will_challenge_termination_description"]) -> typing.Union[MetaOapg.properties.will_challenge_termination_description, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["additional_comments", "confidential", "employment_id", "id", "proposed_termination_date", "reason_description", "requested_by", "risk_assessment_reasons", "status", "submitted_at", "termination_date", "termination_reason", "type", "will_challenge_termination", "agrees_to_pto_amount", "employee_awareness", "will_challenge_termination_description", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        submitted_at: typing.Union[MetaOapg.properties.submitted_at, str, ],
        termination_reason: typing.Union[MetaOapg.properties.termination_reason, str, ],
        reason_description: typing.Union[MetaOapg.properties.reason_description, str, ],
        type: typing.Union[MetaOapg.properties.type, str, ],
        additional_comments: typing.Union[MetaOapg.properties.additional_comments, str, ],
        employment_id: typing.Union[MetaOapg.properties.employment_id, str, ],
        requested_by: typing.Union[MetaOapg.properties.requested_by, str, ],
        proposed_termination_date: typing.Union[MetaOapg.properties.proposed_termination_date, str, date, ],
        termination_date: typing.Union[MetaOapg.properties.termination_date, None, str, date, ],
        risk_assessment_reasons: 'TerminationOffboardingRiskAssessmentReasons',
        id: typing.Union[MetaOapg.properties.id, str, ],
        will_challenge_termination: typing.Union[MetaOapg.properties.will_challenge_termination, bool, ],
        confidential: typing.Union[MetaOapg.properties.confidential, bool, ],
        status: typing.Union[MetaOapg.properties.status, str, ],
        agrees_to_pto_amount: typing.Union[MetaOapg.properties.agrees_to_pto_amount, str, schemas.Unset] = schemas.unset,
        employee_awareness: typing.Union['TerminationOffboardingEmployeeAwareness', schemas.Unset] = schemas.unset,
        will_challenge_termination_description: typing.Union[MetaOapg.properties.will_challenge_termination_description, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'TerminationOffboarding':
        return super().__new__(
            cls,
            *args,
            submitted_at=submitted_at,
            termination_reason=termination_reason,
            reason_description=reason_description,
            type=type,
            additional_comments=additional_comments,
            employment_id=employment_id,
            requested_by=requested_by,
            proposed_termination_date=proposed_termination_date,
            termination_date=termination_date,
            risk_assessment_reasons=risk_assessment_reasons,
            id=id,
            will_challenge_termination=will_challenge_termination,
            confidential=confidential,
            status=status,
            agrees_to_pto_amount=agrees_to_pto_amount,
            employee_awareness=employee_awareness,
            will_challenge_termination_description=will_challenge_termination_description,
            _configuration=_configuration,
            **kwargs,
        )

from remote_python_sdk.model.termination_offboarding_employee_awareness import TerminationOffboardingEmployeeAwareness
from remote_python_sdk.model.termination_offboarding_risk_assessment_reasons import TerminationOffboardingRiskAssessmentReasons
