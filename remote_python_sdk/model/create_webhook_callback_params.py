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


class CreateWebhookCallbackParams(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Webhook callback creation params
    """


    class MetaOapg:
        required = {
            "url",
        }
        
        class properties:
            url = schemas.StrSchema
        
            @staticmethod
            def subscribed_events() -> typing.Type['CreateWebhookCallbackParamsSubscribedEvents']:
                return CreateWebhookCallbackParamsSubscribedEvents
            __annotations__ = {
                "url": url,
                "subscribed_events": subscribed_events,
            }
    
    url: MetaOapg.properties.url
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["url"]) -> MetaOapg.properties.url: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["subscribed_events"]) -> 'CreateWebhookCallbackParamsSubscribedEvents': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["url", "subscribed_events", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["url"]) -> MetaOapg.properties.url: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["subscribed_events"]) -> typing.Union['CreateWebhookCallbackParamsSubscribedEvents', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["url", "subscribed_events", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        url: typing.Union[MetaOapg.properties.url, str, ],
        subscribed_events: typing.Union['CreateWebhookCallbackParamsSubscribedEvents', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'CreateWebhookCallbackParams':
        return super().__new__(
            cls,
            *args,
            url=url,
            subscribed_events=subscribed_events,
            _configuration=_configuration,
            **kwargs,
        )

from remote_python_sdk.model.create_webhook_callback_params_subscribed_events import CreateWebhookCallbackParamsSubscribedEvents
