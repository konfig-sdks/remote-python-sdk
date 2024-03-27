# coding: utf-8

"""
    Remote API

    Talent is everywhere. Opportunity is not. Remote's mission is to create opportunity everywhere, empowering employers to find and hire the best talent, and enabling individuals to build financial and personal freedom.   Remote is a Global HR Platform that helps companies hire, manage, and pay their entire team — and more effectively compete in the modern global economy through our comprehensive set of core solutions including, HRIS, payroll, international employment, contractor management, and more.   Whether you're just starting your global journey, or looking to optimize your existing operations, sign up or book a demo - and see how Remote makes global HR simple.

    The version of the OpenAPI document: 0.1.0
    Generated by: https://konfigthis.com
"""

from dataclasses import dataclass
import typing_extensions
import urllib3
from pydantic import RootModel
from remote_python_sdk.request_before_hook import request_before_hook
import json
from urllib3._collections import HTTPHeaderDict

from remote_python_sdk.api_response import AsyncGeneratorResponse
from remote_python_sdk import api_client, exceptions
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

from remote_python_sdk.model.not_found_response import NotFoundResponse as NotFoundResponseSchema
from remote_python_sdk.model.create_company_department_params import CreateCompanyDepartmentParams as CreateCompanyDepartmentParamsSchema
from remote_python_sdk.model.unprocessable_entity_response import UnprocessableEntityResponse as UnprocessableEntityResponseSchema
from remote_python_sdk.model.company_department_created_response import CompanyDepartmentCreatedResponse as CompanyDepartmentCreatedResponseSchema

from remote_python_sdk.type.not_found_response import NotFoundResponse
from remote_python_sdk.type.create_company_department_params import CreateCompanyDepartmentParams
from remote_python_sdk.type.unprocessable_entity_response import UnprocessableEntityResponse
from remote_python_sdk.type.company_department_created_response import CompanyDepartmentCreatedResponse

from ...api_client import Dictionary
from remote_python_sdk.pydantic.create_company_department_params import CreateCompanyDepartmentParams as CreateCompanyDepartmentParamsPydantic
from remote_python_sdk.pydantic.not_found_response import NotFoundResponse as NotFoundResponsePydantic
from remote_python_sdk.pydantic.company_department_created_response import CompanyDepartmentCreatedResponse as CompanyDepartmentCreatedResponsePydantic
from remote_python_sdk.pydantic.unprocessable_entity_response import UnprocessableEntityResponse as UnprocessableEntityResponsePydantic

from . import path

# body param
SchemaForRequestBodyApplicationJson = CreateCompanyDepartmentParamsSchema


request_body_create_company_department_params = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
    },
    required=True,
)
_auth = [
    'OAuth2',
    'OAuth2',
]
SchemaFor201ResponseBodyApplicationJson = CompanyDepartmentCreatedResponseSchema


@dataclass
class ApiResponseFor201(api_client.ApiResponse):
    body: CompanyDepartmentCreatedResponse


@dataclass
class ApiResponseFor201Async(api_client.AsyncApiResponse):
    body: CompanyDepartmentCreatedResponse


_response_for_201 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor201,
    response_cls_async=ApiResponseFor201Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor201ResponseBodyApplicationJson),
    },
)
SchemaFor404ResponseBodyApplicationJson = NotFoundResponseSchema


@dataclass
class ApiResponseFor404(api_client.ApiResponse):
    body: NotFoundResponse


@dataclass
class ApiResponseFor404Async(api_client.AsyncApiResponse):
    body: NotFoundResponse


_response_for_404 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor404,
    response_cls_async=ApiResponseFor404Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor404ResponseBodyApplicationJson),
    },
)
SchemaFor422ResponseBodyApplicationJson = UnprocessableEntityResponseSchema


@dataclass
class ApiResponseFor422(api_client.ApiResponse):
    body: UnprocessableEntityResponse


@dataclass
class ApiResponseFor422Async(api_client.AsyncApiResponse):
    body: UnprocessableEntityResponse


_response_for_422 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor422,
    response_cls_async=ApiResponseFor422Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor422ResponseBodyApplicationJson),
    },
)
_status_code_to_response = {
    '201': _response_for_201,
    '404': _response_for_404,
    '422': _response_for_422,
}
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _create_new_department_mapped_args(
        self,
        company_id: str,
        name: str,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _body = {}
        if company_id is not None:
            _body["company_id"] = company_id
        if name is not None:
            _body["name"] = name
        args.body = _body
        return args

    async def _acreate_new_department_oapg(
        self,
        body: typing.Any = None,
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor201Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        Create New Department
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        used_path = path.value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'post'.upper()
        _headers.add('Content-Type', content_type)
    
        if body is schemas.unset:
            raise exceptions.ApiValueError(
                'The required body parameter has an invalid value of: unset. Set a valid value instead')
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/v1/company-departments',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_create_company_department_params.serialize(body, content_type)
        if 'fields' in serialized_data:
            _fields = serialized_data['fields']
        elif 'body' in serialized_data:
            _body = serialized_data['body']
    
        response = await self.api_client.async_call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            fields=_fields,
            serialized_body=_body,
            body=body,
            auth_settings=_auth,
            timeout=timeout,
            **kwargs
        )
    
        if stream:
            if not 200 <= response.http_response.status <= 299:
                body = (await response.http_response.content.read()).decode("utf-8")
                raise exceptions.ApiStreamingException(
                    status=response.http_response.status,
                    reason=response.http_response.reason,
                    body=body,
                )
    
            async def stream_iterator():
                """
                iterates over response.http_response.content and closes connection once iteration has finished
                """
                async for line in response.http_response.content:
                    if line == b'\r\n':
                        continue
                    yield line
                response.http_response.close()
                await response.session.close()
            return AsyncGeneratorResponse(
                content=stream_iterator(),
                headers=response.http_response.headers,
                status=response.http_response.status,
                response=response.http_response
            )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = await response_for_status.deserialize_async(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            # If response data is JSON then deserialize for SDK consumer convenience
            is_json = api_client.JSONDetector._content_type_is_json(response.http_response.headers.get('Content-Type', ''))
            api_response = api_client.ApiResponseWithoutDeserializationAsync(
                body=await response.http_response.json() if is_json else await response.http_response.text(),
                response=response.http_response,
                round_trip_time=response.round_trip_time,
                status=response.http_response.status,
                headers=response.http_response.headers,
            )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        # cleanup session / response
        response.http_response.close()
        await response.session.close()
    
        return api_response


    def _create_new_department_oapg(
        self,
        body: typing.Any = None,
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor201,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Create New Department
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        used_path = path.value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'post'.upper()
        _headers.add('Content-Type', content_type)
    
        if body is schemas.unset:
            raise exceptions.ApiValueError(
                'The required body parameter has an invalid value of: unset. Set a valid value instead')
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/v1/company-departments',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_create_company_department_params.serialize(body, content_type)
        if 'fields' in serialized_data:
            _fields = serialized_data['fields']
        elif 'body' in serialized_data:
            _body = serialized_data['body']
    
        response = self.api_client.call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            fields=_fields,
            serialized_body=_body,
            body=body,
            auth_settings=_auth,
            timeout=timeout,
        )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = response_for_status.deserialize(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            # If response data is JSON then deserialize for SDK consumer convenience
            is_json = api_client.JSONDetector._content_type_is_json(response.http_response.headers.get('Content-Type', ''))
            api_response = api_client.ApiResponseWithoutDeserialization(
                body=json.loads(response.http_response.data) if is_json else response.http_response.data,
                response=response.http_response,
                round_trip_time=response.round_trip_time,
                status=response.http_response.status,
                headers=response.http_response.headers,
            )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        return api_response


class CreateNewDepartmentRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def acreate_new_department(
        self,
        company_id: str,
        name: str,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor201Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._create_new_department_mapped_args(
            company_id=company_id,
            name=name,
        )
        return await self._acreate_new_department_oapg(
            body=args.body,
            **kwargs,
        )
    
    def create_new_department(
        self,
        company_id: str,
        name: str,
    ) -> typing.Union[
        ApiResponseFor201,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._create_new_department_mapped_args(
            company_id=company_id,
            name=name,
        )
        return self._create_new_department_oapg(
            body=args.body,
        )

class CreateNewDepartment(BaseApi):

    async def acreate_new_department(
        self,
        company_id: str,
        name: str,
        validate: bool = False,
        **kwargs,
    ) -> CompanyDepartmentCreatedResponsePydantic:
        raw_response = await self.raw.acreate_new_department(
            company_id=company_id,
            name=name,
            **kwargs,
        )
        if validate:
            return CompanyDepartmentCreatedResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(CompanyDepartmentCreatedResponsePydantic, raw_response.body)
    
    
    def create_new_department(
        self,
        company_id: str,
        name: str,
        validate: bool = False,
    ) -> CompanyDepartmentCreatedResponsePydantic:
        raw_response = self.raw.create_new_department(
            company_id=company_id,
            name=name,
        )
        if validate:
            return CompanyDepartmentCreatedResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(CompanyDepartmentCreatedResponsePydantic, raw_response.body)


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apost(
        self,
        company_id: str,
        name: str,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor201Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._create_new_department_mapped_args(
            company_id=company_id,
            name=name,
        )
        return await self._acreate_new_department_oapg(
            body=args.body,
            **kwargs,
        )
    
    def post(
        self,
        company_id: str,
        name: str,
    ) -> typing.Union[
        ApiResponseFor201,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._create_new_department_mapped_args(
            company_id=company_id,
            name=name,
        )
        return self._create_new_department_oapg(
            body=args.body,
        )

