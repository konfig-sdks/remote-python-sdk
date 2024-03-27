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


class Company(BaseModel):
    # Fields can vary depending on the country. Please, check the required fields structure using the [Show form schema endpoint](https://gateway.remote.com/v1/docs/openapi.html). Use the desired country and `address_details` as the form name for the placeholders. The response complies with the [JSON Schema](https://remote.com/resources/api/how-json-schemas-work) specification. 
    address_details: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(alias='address_details')

    company_owner_email: str = Field(alias='company_owner_email')

    country_code: str = Field(alias='country_code')

    created_at: datetime = Field(alias='created_at')

    desired_currency: str = Field(alias='desired_currency')

    id: str = Field(alias='id')

    name: str = Field(alias='name')

    # The company status determines what a company is allowed to do: - `pending`: The company has been created and the company owner invited. Remote is waiting for the company owner to complete onboarding. - `review`: The company is under review. In rare occasions, a company may not automatically get created in `active` status because Remote needs to   manually review the company that was created. The company will become `active` once the review is completed and no further action is necessary   through the Remote API. - `active`: The company owner has completed onboarding and the company is ready to employ. - `archived`: The company is no longer active on the Remote platform and no changes can be made to the company. 
    status: Literal["pending", "review", "active", "archived"] = Field(alias='status')

    terms_of_service_accepted_at: datetime = Field(alias='terms_of_service_accepted_at')

    updated_at: datetime = Field(alias='updated_at')

    # Fields can vary depending on the country. Please, check the required fields structure using the [Show form schema endpoint](https://gateway.remote.com/v1/docs/openapi.html). Use the desired country and `bank_account_details` as the form name for the placeholders. The response complies with the [JSON Schema](https://remote.com/resources/api/how-json-schemas-work) specification. 
    bank_account_details: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = Field(None, alias='bank_account_details')

    company_owner_name: typing.Optional[str] = Field(None, alias='company_owner_name')

    external_id: typing.Optional[typing.Optional[str]] = Field(None, alias='external_id')

    phone_number: typing.Optional[str] = Field(None, alias='phone_number')

    registration_number: typing.Optional[typing.Optional[str]] = Field(None, alias='registration_number')

    tax_number: typing.Optional[typing.Optional[str]] = Field(None, alias='tax_number')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
