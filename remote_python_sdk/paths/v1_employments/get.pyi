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
from remote_python_sdk.model.unprocessable_entity_response import UnprocessableEntityResponse as UnprocessableEntityResponseSchema
from remote_python_sdk.model.list_employments_response import ListEmploymentsResponse as ListEmploymentsResponseSchema
from remote_python_sdk.model.too_many_requests_response import TooManyRequestsResponse as TooManyRequestsResponseSchema
from remote_python_sdk.model.bad_request_response import BadRequestResponse as BadRequestResponseSchema
from remote_python_sdk.model.unauthorized_response import UnauthorizedResponse as UnauthorizedResponseSchema

from remote_python_sdk.type.too_many_requests_response import TooManyRequestsResponse
from remote_python_sdk.type.not_found_response import NotFoundResponse
from remote_python_sdk.type.bad_request_response import BadRequestResponse
from remote_python_sdk.type.list_employments_response import ListEmploymentsResponse
from remote_python_sdk.type.unprocessable_entity_response import UnprocessableEntityResponse
from remote_python_sdk.type.unauthorized_response import UnauthorizedResponse

from ...api_client import Dictionary
from remote_python_sdk.pydantic.too_many_requests_response import TooManyRequestsResponse as TooManyRequestsResponsePydantic
from remote_python_sdk.pydantic.not_found_response import NotFoundResponse as NotFoundResponsePydantic
from remote_python_sdk.pydantic.list_employments_response import ListEmploymentsResponse as ListEmploymentsResponsePydantic
from remote_python_sdk.pydantic.unprocessable_entity_response import UnprocessableEntityResponse as UnprocessableEntityResponsePydantic
from remote_python_sdk.pydantic.unauthorized_response import UnauthorizedResponse as UnauthorizedResponsePydantic
from remote_python_sdk.pydantic.bad_request_response import BadRequestResponse as BadRequestResponsePydantic

# Query params
CompanyIdSchema = schemas.StrSchema
EmailSchema = schemas.StrSchema
StatusSchema = schemas.StrSchema
PageSchema = schemas.IntSchema
PageSizeSchema = schemas.IntSchema
RequestRequiredQueryParams = typing_extensions.TypedDict(
    'RequestRequiredQueryParams',
    {
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
        'company_id': typing.Union[CompanyIdSchema, str, ],
        'email': typing.Union[EmailSchema, str, ],
        'status': typing.Union[StatusSchema, str, ],
        'page': typing.Union[PageSchema, decimal.Decimal, int, ],
        'page_size': typing.Union[PageSizeSchema, decimal.Decimal, int, ],
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


request_query_company_id = api_client.QueryParameter(
    name="company_id",
    style=api_client.ParameterStyle.FORM,
    schema=CompanyIdSchema,
    explode=True,
)
request_query_email = api_client.QueryParameter(
    name="email",
    style=api_client.ParameterStyle.FORM,
    schema=EmailSchema,
    explode=True,
)
request_query_status = api_client.QueryParameter(
    name="status",
    style=api_client.ParameterStyle.FORM,
    schema=StatusSchema,
    explode=True,
)
request_query_page = api_client.QueryParameter(
    name="page",
    style=api_client.ParameterStyle.FORM,
    schema=PageSchema,
    explode=True,
)
request_query_page_size = api_client.QueryParameter(
    name="page_size",
    style=api_client.ParameterStyle.FORM,
    schema=PageSizeSchema,
    explode=True,
)
SchemaFor200ResponseBodyApplicationJson = ListEmploymentsResponseSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: ListEmploymentsResponse


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: ListEmploymentsResponse


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
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _list_all_mapped_args(
        self,
        company_id: typing.Optional[str] = None,
        email: typing.Optional[str] = None,
        status: typing.Optional[str] = None,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _query_params = {}
        if company_id is not None:
            _query_params["company_id"] = company_id
        if email is not None:
            _query_params["email"] = email
        if status is not None:
            _query_params["status"] = status
        if page is not None:
            _query_params["page"] = page
        if page_size is not None:
            _query_params["page_size"] = page_size
        args.query = _query_params
        return args

    async def _alist_all_oapg(
        self,
            query_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        List employments
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_company_id,
            request_query_email,
            request_query_status,
            request_query_page,
            request_query_page_size,
        ):
            parameter_data = query_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            if prefix_separator_iterator is None:
                prefix_separator_iterator = parameter.get_prefix_separator_iterator()
            serialized_data = parameter.serialize(parameter_data, prefix_separator_iterator)
            for serialized_value in serialized_data.values():
                used_path += serialized_value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'get'.upper()
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/v1/employments',
            auth_settings=_auth,
            headers=_headers,
        )
    
        response = await self.api_client.async_call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            auth_settings=_auth,
            prefix_separator_iterator=prefix_separator_iterator,
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


    def _list_all_oapg(
        self,
            query_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        List employments
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_company_id,
            request_query_email,
            request_query_status,
            request_query_page,
            request_query_page_size,
        ):
            parameter_data = query_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            if prefix_separator_iterator is None:
                prefix_separator_iterator = parameter.get_prefix_separator_iterator()
            serialized_data = parameter.serialize(parameter_data, prefix_separator_iterator)
            for serialized_value in serialized_data.values():
                used_path += serialized_value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'get'.upper()
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/v1/employments',
            auth_settings=_auth,
            headers=_headers,
        )
    
        response = self.api_client.call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            auth_settings=_auth,
            prefix_separator_iterator=prefix_separator_iterator,
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


class ListAllRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def alist_all(
        self,
        company_id: typing.Optional[str] = None,
        email: typing.Optional[str] = None,
        status: typing.Optional[str] = None,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._list_all_mapped_args(
            company_id=company_id,
            email=email,
            status=status,
            page=page,
            page_size=page_size,
        )
        return await self._alist_all_oapg(
            query_params=args.query,
            **kwargs,
        )
    
    def list_all(
        self,
        company_id: typing.Optional[str] = None,
        email: typing.Optional[str] = None,
        status: typing.Optional[str] = None,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._list_all_mapped_args(
            company_id=company_id,
            email=email,
            status=status,
            page=page,
            page_size=page_size,
        )
        return self._list_all_oapg(
            query_params=args.query,
        )

class ListAll(BaseApi):

    async def alist_all(
        self,
        company_id: typing.Optional[str] = None,
        email: typing.Optional[str] = None,
        status: typing.Optional[str] = None,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        validate: bool = False,
        **kwargs,
    ) -> ListEmploymentsResponsePydantic:
        raw_response = await self.raw.alist_all(
            company_id=company_id,
            email=email,
            status=status,
            page=page,
            page_size=page_size,
            **kwargs,
        )
        if validate:
            return ListEmploymentsResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(ListEmploymentsResponsePydantic, raw_response.body)
    
    
    def list_all(
        self,
        company_id: typing.Optional[str] = None,
        email: typing.Optional[str] = None,
        status: typing.Optional[str] = None,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        validate: bool = False,
    ) -> ListEmploymentsResponsePydantic:
        raw_response = self.raw.list_all(
            company_id=company_id,
            email=email,
            status=status,
            page=page,
            page_size=page_size,
        )
        if validate:
            return ListEmploymentsResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(ListEmploymentsResponsePydantic, raw_response.body)


class ApiForget(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aget(
        self,
        company_id: typing.Optional[str] = None,
        email: typing.Optional[str] = None,
        status: typing.Optional[str] = None,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._list_all_mapped_args(
            company_id=company_id,
            email=email,
            status=status,
            page=page,
            page_size=page_size,
        )
        return await self._alist_all_oapg(
            query_params=args.query,
            **kwargs,
        )
    
    def get(
        self,
        company_id: typing.Optional[str] = None,
        email: typing.Optional[str] = None,
        status: typing.Optional[str] = None,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._list_all_mapped_args(
            company_id=company_id,
            email=email,
            status=status,
            page=page,
            page_size=page_size,
        )
        return self._list_all_oapg(
            query_params=args.query,
        )

