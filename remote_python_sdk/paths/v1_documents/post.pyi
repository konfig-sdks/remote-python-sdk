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
from remote_python_sdk.model.too_many_requests_response import TooManyRequestsResponse as TooManyRequestsResponseSchema
from remote_python_sdk.model.file_response import FileResponse as FileResponseSchema
from remote_python_sdk.model.bad_request_response import BadRequestResponse as BadRequestResponseSchema
from remote_python_sdk.model.file_params import FileParams as FileParamsSchema
from remote_python_sdk.model.unauthorized_response import UnauthorizedResponse as UnauthorizedResponseSchema

from remote_python_sdk.type.too_many_requests_response import TooManyRequestsResponse
from remote_python_sdk.type.not_found_response import NotFoundResponse
from remote_python_sdk.type.bad_request_response import BadRequestResponse
from remote_python_sdk.type.file_response import FileResponse
from remote_python_sdk.type.unprocessable_entity_response import UnprocessableEntityResponse
from remote_python_sdk.type.file_params import FileParams
from remote_python_sdk.type.unauthorized_response import UnauthorizedResponse

from ...api_client import Dictionary
from remote_python_sdk.pydantic.too_many_requests_response import TooManyRequestsResponse as TooManyRequestsResponsePydantic
from remote_python_sdk.pydantic.file_params import FileParams as FileParamsPydantic
from remote_python_sdk.pydantic.not_found_response import NotFoundResponse as NotFoundResponsePydantic
from remote_python_sdk.pydantic.file_response import FileResponse as FileResponsePydantic
from remote_python_sdk.pydantic.unprocessable_entity_response import UnprocessableEntityResponse as UnprocessableEntityResponsePydantic
from remote_python_sdk.pydantic.unauthorized_response import UnauthorizedResponse as UnauthorizedResponsePydantic
from remote_python_sdk.pydantic.bad_request_response import BadRequestResponse as BadRequestResponsePydantic

# body param
SchemaForRequestBodyMultipartFormData = FileParamsSchema


request_body_file_params = api_client.RequestBody(
    content={
        'multipart/form-data': api_client.MediaType(
            schema=SchemaForRequestBodyMultipartFormData),
    },
    required=True,
)
SchemaFor201ResponseBodyApplicationJson = FileResponseSchema


@dataclass
class ApiResponseFor201(api_client.ApiResponse):
    body: FileResponse


@dataclass
class ApiResponseFor201Async(api_client.AsyncApiResponse):
    body: FileResponse


_response_for_201 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor201,
    response_cls_async=ApiResponseFor201Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor201ResponseBodyApplicationJson),
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

    def _upload_employment_file_mapped_args(
        self,
        employment_id: str,
        file: typing.IO,
        type: str,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _body = {}
        if employment_id is not None:
            _body["employment_id"] = employment_id
        if file is not None:
            _body["file"] = file
        if type is not None:
            _body["type"] = type
        args.body = _body
        return args

    async def _aupload_employment_file_oapg(
        self,
        body: typing.Any = None,
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'multipart/form-data',
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor201Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        Upload file
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
            path_template='/v1/documents',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_file_params.serialize(body, content_type)
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


    def _upload_employment_file_oapg(
        self,
        body: typing.Any = None,
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'multipart/form-data',
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor201,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Upload file
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
            path_template='/v1/documents',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_file_params.serialize(body, content_type)
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


class UploadEmploymentFileRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aupload_employment_file(
        self,
        employment_id: str,
        file: typing.IO,
        type: str,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor201Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._upload_employment_file_mapped_args(
            employment_id=employment_id,
            file=file,
            type=type,
        )
        return await self._aupload_employment_file_oapg(
            body=args.body,
            **kwargs,
        )
    
    def upload_employment_file(
        self,
        employment_id: str,
        file: typing.IO,
        type: str,
    ) -> typing.Union[
        ApiResponseFor201,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._upload_employment_file_mapped_args(
            employment_id=employment_id,
            file=file,
            type=type,
        )
        return self._upload_employment_file_oapg(
            body=args.body,
        )

class UploadEmploymentFile(BaseApi):

    async def aupload_employment_file(
        self,
        employment_id: str,
        file: typing.IO,
        type: str,
        validate: bool = False,
        **kwargs,
    ) -> FileResponsePydantic:
        raw_response = await self.raw.aupload_employment_file(
            employment_id=employment_id,
            file=file,
            type=type,
            **kwargs,
        )
        if validate:
            return FileResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(FileResponsePydantic, raw_response.body)
    
    
    def upload_employment_file(
        self,
        employment_id: str,
        file: typing.IO,
        type: str,
        validate: bool = False,
    ) -> FileResponsePydantic:
        raw_response = self.raw.upload_employment_file(
            employment_id=employment_id,
            file=file,
            type=type,
        )
        if validate:
            return FileResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(FileResponsePydantic, raw_response.body)


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apost(
        self,
        employment_id: str,
        file: typing.IO,
        type: str,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor201Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._upload_employment_file_mapped_args(
            employment_id=employment_id,
            file=file,
            type=type,
        )
        return await self._aupload_employment_file_oapg(
            body=args.body,
            **kwargs,
        )
    
    def post(
        self,
        employment_id: str,
        file: typing.IO,
        type: str,
    ) -> typing.Union[
        ApiResponseFor201,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._upload_employment_file_mapped_args(
            employment_id=employment_id,
            file=file,
            type=type,
        )
        return self._upload_employment_file_oapg(
            body=args.body,
        )

