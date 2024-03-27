# coding: utf-8

"""
    Remote API

    Talent is everywhere. Opportunity is not. Remote's mission is to create opportunity everywhere, empowering employers to find and hire the best talent, and enabling individuals to build financial and personal freedom.   Remote is a Global HR Platform that helps companies hire, manage, and pay their entire team — and more effectively compete in the modern global economy through our comprehensive set of core solutions including, HRIS, payroll, international employment, contractor management, and more.   Whether you're just starting your global journey, or looking to optimize your existing operations, sign up or book a demo - and see how Remote makes global HR simple.

    The version of the OpenAPI document: 0.1.0
    Generated by: https://konfigthis.com
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal, TYPE_CHECKING
from pydantic import BaseModel, Field, RootModel, ConfigDict


class ResignationOffboarding(BaseModel):
    employment_id: str = Field(alias='employment_id')

    id: str = Field(alias='id')

    proposed_last_working_day: date = Field(alias='proposed_last_working_day')

    requested_by: str = Field(alias='requested_by')

    resignation_reason: Literal["cancellation_before_start_date", "company_culture_or_values", "conversion_to_contractor", "dissatisfaction_with_remote_service", "incapacity_to_perform_inherent_duties", "infrastructure_challenges", "lack_of_recognition", "leadership", "mutual_agreement", "other", "other_job_opportunity", "personal_reasons", "position_does_not_meet_expectations", "relationship_with_coworkers", "relocation_from_entity_to_entity_by_employee", "relocation_leaving_remote", "remuneration_and_benefits", "retirement", "transfer_and_relocation_new_customer_and_new_country", "transfer_between_remote_customer", "transfer_from_remote_to_customer", "transfer_from_remote_to_other_eor"] = Field(alias='resignation_reason')

    status: Literal["submitted", "in_review", "done", "canceled"] = Field(alias='status')

    submitted_at: str = Field(alias='submitted_at')

    # Most updated termination date for the offboarding. This date is subject to change through the offboarding process even after it is finalized.
    termination_date: typing.Optional[date] = Field(alias='termination_date')

    type: Literal["resignation"] = Field(alias='type')

    additional_comments: typing.Optional[str] = Field(None, alias='additional_comments')

    employer_awareness: typing.Optional[str] = Field(None, alias='employer_awareness')

    reason_description: typing.Optional[str] = Field(None, alias='reason_description')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )