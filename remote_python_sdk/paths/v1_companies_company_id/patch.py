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

from remote_python_sdk.model.update_company_params import UpdateCompanyParams as UpdateCompanyParamsSchema
from remote_python_sdk.model.not_found_response import NotFoundResponse as NotFoundResponseSchema
from remote_python_sdk.model.unprocessable_entity_response import UnprocessableEntityResponse as UnprocessableEntityResponseSchema
from remote_python_sdk.model.too_many_requests_response import TooManyRequestsResponse as TooManyRequestsResponseSchema
from remote_python_sdk.model.company_response import CompanyResponse as CompanyResponseSchema
from remote_python_sdk.model.bad_request_response import BadRequestResponse as BadRequestResponseSchema
from remote_python_sdk.model.unauthorized_response import UnauthorizedResponse as UnauthorizedResponseSchema

from remote_python_sdk.type.too_many_requests_response import TooManyRequestsResponse
from remote_python_sdk.type.not_found_response import NotFoundResponse
from remote_python_sdk.type.update_company_params import UpdateCompanyParams
from remote_python_sdk.type.bad_request_response import BadRequestResponse
from remote_python_sdk.type.company_response import CompanyResponse
from remote_python_sdk.type.unprocessable_entity_response import UnprocessableEntityResponse
from remote_python_sdk.type.unauthorized_response import UnauthorizedResponse

from ...api_client import Dictionary
from remote_python_sdk.pydantic.too_many_requests_response import TooManyRequestsResponse as TooManyRequestsResponsePydantic
from remote_python_sdk.pydantic.not_found_response import NotFoundResponse as NotFoundResponsePydantic
from remote_python_sdk.pydantic.update_company_params import UpdateCompanyParams as UpdateCompanyParamsPydantic
from remote_python_sdk.pydantic.unprocessable_entity_response import UnprocessableEntityResponse as UnprocessableEntityResponsePydantic
from remote_python_sdk.pydantic.unauthorized_response import UnauthorizedResponse as UnauthorizedResponsePydantic
from remote_python_sdk.pydantic.bad_request_response import BadRequestResponse as BadRequestResponsePydantic
from remote_python_sdk.pydantic.company_response import CompanyResponse as CompanyResponsePydantic

from . import path

# Path params
CompanyIdSchema = schemas.StrSchema
RequestRequiredPathParams = typing_extensions.TypedDict(
    'RequestRequiredPathParams',
    {
        'company_id': typing.Union[CompanyIdSchema, str, ],
    }
)
RequestOptionalPathParams = typing_extensions.TypedDict(
    'RequestOptionalPathParams',
    {
    },
    total=False
)


class RequestPathParams(RequestRequiredPathParams, RequestOptionalPathParams):
    pass


request_path_company_id = api_client.PathParameter(
    name="company_id",
    style=api_client.ParameterStyle.SIMPLE,
    schema=CompanyIdSchema,
    required=True,
)
# body param
SchemaForRequestBodyApplicationJson = UpdateCompanyParamsSchema


request_body_update_company_params = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
    },
)
_auth = [
    'OAuth2',
    'OAuth2',
]
SchemaFor200ResponseBodyApplicationJson = CompanyResponseSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: CompanyResponse


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: CompanyResponse


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson),
    },
)
SchemaFor400ResponseBodyApplicationJson = BadRequestResponseSchema


@dataclass
class ApiResponseFor400(api_client.ApiResponse):
    body: BadRequestResponse


@dataclass
class ApiResponseFor400Async(api_client.AsyncApiResponse):
    body: BadRequestResponse


_response_for_400 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor400,
    response_cls_async=ApiResponseFor400Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor400ResponseBodyApplicationJson),
    },
)
SchemaFor401ResponseBodyApplicationJson = UnauthorizedResponseSchema


@dataclass
class ApiResponseFor401(api_client.ApiResponse):
    body: UnauthorizedResponse


@dataclass
class ApiResponseFor401Async(api_client.AsyncApiResponse):
    body: UnauthorizedResponse


_response_for_401 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor401,
    response_cls_async=ApiResponseFor401Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor401ResponseBodyApplicationJson),
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
SchemaFor429ResponseBodyApplicationJson = TooManyRequestsResponseSchema


@dataclass
class ApiResponseFor429(api_client.ApiResponse):
    body: TooManyRequestsResponse


@dataclass
class ApiResponseFor429Async(api_client.AsyncApiResponse):
    body: TooManyRequestsResponse


_response_for_429 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor429,
    response_cls_async=ApiResponseFor429Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor429ResponseBodyApplicationJson),
    },
)
_status_code_to_response = {
    '200': _response_for_200,
    '400': _response_for_400,
    '401': _response_for_401,
    '404': _response_for_404,
    '422': _response_for_422,
    '429': _response_for_429,
}
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _update_company_0_mapped_args(
        self,
        company_id: str,
        address_details: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        bank_account_details: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        country_code: typing.Optional[str] = None,
        desired_currency: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        phone_number: typing.Optional[str] = None,
        registration_number: typing.Optional[str] = None,
        tax_number: typing.Optional[str] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _path_params = {}
        _body = {}
        if address_details is not None:
            _body["address_details"] = address_details
        if bank_account_details is not None:
            _body["bank_account_details"] = bank_account_details
        if country_code is not None:
            _body["country_code"] = country_code
        if desired_currency is not None:
            _body["desired_currency"] = desired_currency
        if name is not None:
            _body["name"] = name
        if phone_number is not None:
            _body["phone_number"] = phone_number
        if registration_number is not None:
            _body["registration_number"] = registration_number
        if tax_number is not None:
            _body["tax_number"] = tax_number
        args.body = _body
        if company_id is not None:
            _path_params["company_id"] = company_id
        args.path = _path_params
        return args

    async def _aupdate_company_0_oapg(
        self,
        body: typing.Any = None,
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        Update a company
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_company_id,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)
    
        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'patch'.upper()
        _headers.add('Content-Type', content_type)
    
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/v1/companies/{company_id}',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_update_company_params.serialize(body, content_type)
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


    def _update_company_0_oapg(
        self,
        body: typing.Any = None,
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Update a company
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_company_id,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)
    
        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'patch'.upper()
        _headers.add('Content-Type', content_type)
    
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/v1/companies/{company_id}',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_update_company_params.serialize(body, content_type)
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


class UpdateCompany0Raw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aupdate_company_0(
        self,
        company_id: str,
        address_details: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        bank_account_details: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        country_code: typing.Optional[str] = None,
        desired_currency: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        phone_number: typing.Optional[str] = None,
        registration_number: typing.Optional[str] = None,
        tax_number: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._update_company_0_mapped_args(
            company_id=company_id,
            address_details=address_details,
            bank_account_details=bank_account_details,
            country_code=country_code,
            desired_currency=desired_currency,
            name=name,
            phone_number=phone_number,
            registration_number=registration_number,
            tax_number=tax_number,
        )
        return await self._aupdate_company_0_oapg(
            body=args.body,
            path_params=args.path,
            **kwargs,
        )
    
    def update_company_0(
        self,
        company_id: str,
        address_details: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        bank_account_details: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        country_code: typing.Optional[str] = None,
        desired_currency: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        phone_number: typing.Optional[str] = None,
        registration_number: typing.Optional[str] = None,
        tax_number: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._update_company_0_mapped_args(
            company_id=company_id,
            address_details=address_details,
            bank_account_details=bank_account_details,
            country_code=country_code,
            desired_currency=desired_currency,
            name=name,
            phone_number=phone_number,
            registration_number=registration_number,
            tax_number=tax_number,
        )
        return self._update_company_0_oapg(
            body=args.body,
            path_params=args.path,
        )

class UpdateCompany0(BaseApi):

    async def aupdate_company_0(
        self,
        company_id: str,
        address_details: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        bank_account_details: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        country_code: typing.Optional[str] = None,
        desired_currency: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        phone_number: typing.Optional[str] = None,
        registration_number: typing.Optional[str] = None,
        tax_number: typing.Optional[str] = None,
        validate: bool = False,
        **kwargs,
    ) -> CompanyResponsePydantic:
        raw_response = await self.raw.aupdate_company_0(
            company_id=company_id,
            address_details=address_details,
            bank_account_details=bank_account_details,
            country_code=country_code,
            desired_currency=desired_currency,
            name=name,
            phone_number=phone_number,
            registration_number=registration_number,
            tax_number=tax_number,
            **kwargs,
        )
        if validate:
            return CompanyResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(CompanyResponsePydantic, raw_response.body)
    
    
    def update_company_0(
        self,
        company_id: str,
        address_details: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        bank_account_details: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        country_code: typing.Optional[str] = None,
        desired_currency: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        phone_number: typing.Optional[str] = None,
        registration_number: typing.Optional[str] = None,
        tax_number: typing.Optional[str] = None,
        validate: bool = False,
    ) -> CompanyResponsePydantic:
        raw_response = self.raw.update_company_0(
            company_id=company_id,
            address_details=address_details,
            bank_account_details=bank_account_details,
            country_code=country_code,
            desired_currency=desired_currency,
            name=name,
            phone_number=phone_number,
            registration_number=registration_number,
            tax_number=tax_number,
        )
        if validate:
            return CompanyResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(CompanyResponsePydantic, raw_response.body)


class ApiForpatch(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apatch(
        self,
        company_id: str,
        address_details: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        bank_account_details: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        country_code: typing.Optional[str] = None,
        desired_currency: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        phone_number: typing.Optional[str] = None,
        registration_number: typing.Optional[str] = None,
        tax_number: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._update_company_0_mapped_args(
            company_id=company_id,
            address_details=address_details,
            bank_account_details=bank_account_details,
            country_code=country_code,
            desired_currency=desired_currency,
            name=name,
            phone_number=phone_number,
            registration_number=registration_number,
            tax_number=tax_number,
        )
        return await self._aupdate_company_0_oapg(
            body=args.body,
            path_params=args.path,
            **kwargs,
        )
    
    def patch(
        self,
        company_id: str,
        address_details: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        bank_account_details: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        country_code: typing.Optional[str] = None,
        desired_currency: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        phone_number: typing.Optional[str] = None,
        registration_number: typing.Optional[str] = None,
        tax_number: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._update_company_0_mapped_args(
            company_id=company_id,
            address_details=address_details,
            bank_account_details=bank_account_details,
            country_code=country_code,
            desired_currency=desired_currency,
            name=name,
            phone_number=phone_number,
            registration_number=registration_number,
            tax_number=tax_number,
        )
        return self._update_company_0_oapg(
            body=args.body,
            path_params=args.path,
        )

