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


class NullableApproverId(
    schemas.StrBase,
    schemas.NoneBase,
    schemas.Schema,
    schemas.NoneStrMixin
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    The field matches the `id` of a user in the
Remote Platform that has permission to approve time off
requests. [Available users][] can be found fetching
the [List Company Manager][] endpoint.

[Available users]: https://support.remote.com/hc/en-us/articles/360054668651-Approving-Declining-time-off-requests#h_01G0014GZKZ3EMN6P7C99HAK55
[List Company Manager]: https://gateway.remote.com/v1/docs/openapi.html#tag/Company-Managers

    """


    def __new__(
        cls,
        *args: typing.Union[None, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'NullableApproverId':
        return super().__new__(
            cls,
            *args,
            _configuration=_configuration,
        )
