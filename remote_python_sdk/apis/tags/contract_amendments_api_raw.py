# coding: utf-8

"""
    Remote API

    Talent is everywhere. Opportunity is not. Remote's mission is to create opportunity everywhere, empowering employers to find and hire the best talent, and enabling individuals to build financial and personal freedom.   Remote is a Global HR Platform that helps companies hire, manage, and pay their entire team — and more effectively compete in the modern global economy through our comprehensive set of core solutions including, HRIS, payroll, international employment, contractor management, and more.   Whether you're just starting your global journey, or looking to optimize your existing operations, sign up or book a demo - and see how Remote makes global HR simple.

    The version of the OpenAPI document: 0.1.0
    Generated by: https://konfigthis.com
"""

from remote_python_sdk.paths.v1_sandbox_contract_amendments_contract_amendment_request_id_approve.put import ApproveAmendmentRaw
from remote_python_sdk.paths.v1_contract_amendments_automatable.post import CheckAutomatabilityRaw
from remote_python_sdk.paths.v1_contract_amendments.post import CreateRequestRaw
from remote_python_sdk.paths.v1_contract_amendments_schema.post import GetFormSchemaRaw
from remote_python_sdk.paths.v1_contract_amendments.get import ListRequestsRaw
from remote_python_sdk.paths.v1_contract_amendments_id.get import ShowSingleRequestRaw


class ContractAmendmentsApiRaw(
    ApproveAmendmentRaw,
    CheckAutomatabilityRaw,
    CreateRequestRaw,
    GetFormSchemaRaw,
    ListRequestsRaw,
    ShowSingleRequestRaw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass
