# coding: utf-8

"""
    Remote API

    Talent is everywhere. Opportunity is not. Remote's mission is to create opportunity everywhere, empowering employers to find and hire the best talent, and enabling individuals to build financial and personal freedom.   Remote is a Global HR Platform that helps companies hire, manage, and pay their entire team — and more effectively compete in the modern global economy through our comprehensive set of core solutions including, HRIS, payroll, international employment, contractor management, and more.   Whether you're just starting your global journey, or looking to optimize your existing operations, sign up or book a demo - and see how Remote makes global HR simple.

    The version of the OpenAPI document: 0.1.0
    Generated by: https://konfigthis.com
"""

from remote_python_sdk.paths.v1_custom_fields.get import ListDefinitions
from remote_python_sdk.paths.v1_custom_fields_custom_field_id_values_employment_id.get import ShowValue
from remote_python_sdk.apis.tags.custom_fields_api_raw import CustomFieldsApiRaw


class CustomFieldsApi(
    ListDefinitions,
    ShowValue,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: CustomFieldsApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = CustomFieldsApiRaw(api_client)
