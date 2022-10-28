# Copyright 2022 Keyfactor                                                   
# Licensed under the Apache License, Version 2.0 (the "License"); you may    
# not use this file except in compliance with the License.  You may obtain a 
# copy of the License at http://www.apache.org/licenses/LICENSE-2.0.  Unless 
# required by applicable law or agreed to in writing, software distributed   
# under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES   
# OR CONDITIONS OF ANY KIND, either express or implied. See the License for  
# the specific language governing permissions and limitations under the       
# License. 
from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.models_enrollment_csr_enrollment_request import ModelsEnrollmentCSREnrollmentRequest
from ...models.models_enrollment_csr_enrollment_response import ModelsEnrollmentCSREnrollmentResponse
from ...types import Response, Unset


def _get_kwargs(
    *,
    client: Client,
    json_body: ModelsEnrollmentCSREnrollmentRequest,
    x_keyfactor_api_version: Union[Unset, str] = "1",
    x_keyfactor_requested_with: str = "APIClient",
    x_certificateformat: str = "PEM",
) -> Dict[str, Any]:
    url = "{}/Enrollment/CSR".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    if not isinstance(x_keyfactor_api_version, Unset):
        headers["x-keyfactor-api-version"] = x_keyfactor_api_version

    headers["x-keyfactor-requested-with"] = x_keyfactor_requested_with

    headers["x-certificateformat"] = x_certificateformat

    json_json_body = json_body.to_dict()

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
    }


def _parse_response(*, response: httpx.Response) -> Optional[ModelsEnrollmentCSREnrollmentResponse]:
    if response.status_code == 200:
        response_200 = ModelsEnrollmentCSREnrollmentResponse.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[ModelsEnrollmentCSREnrollmentResponse]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    json_body: ModelsEnrollmentCSREnrollmentRequest,
    x_keyfactor_api_version: Union[Unset, str] = "1",
    x_keyfactor_requested_with: str = "APIClient",
    x_certificateformat: str = "PEM",
) -> Response[ModelsEnrollmentCSREnrollmentResponse]:
    """Performs a CSR Enrollment based upon the provided request

     ### Subject Alternative Name Flags ###
    | Value              | Description               |
    |--------------------|---------------------------|
    | other              | OtherName                 |
    | rfc822             | RFC822Name                |
    | dns                | DNSName                   |
    | x400               | X400Address               |
    | directory          | DirectoryName             |
    | ediparty           | EdipartyName              |
    | uri                | UniformResourceIdentifier |
    | ip                 | IPAddress                 |
    | ip4                | IPv4Address               |
    | ip6                | IPv6Address               |
    | registeredid       | RegisteredId              |
    | ms_ntprincipalname | MS_NTPrincipalName        |
    | ms_ntdsreplication | MS_NTDSReplication        |

    Args:
        x_keyfactor_api_version (Union[Unset, str]):  Default: '1'.
        x_keyfactor_requested_with (str):  Default: 'APIClient'.
        x_certificateformat (str):  Default: 'PEM'.
        json_body (ModelsEnrollmentCSREnrollmentRequest):  Example: {'CSR': '<base64-encoded
            CSR>', 'CertificateAuthority': '<host\\logical>', 'IncludeChain': False, 'Timestamp':
            datetime.datetime(2022, 9, 22, 18, 9, 16, 719678, tzinfo=datetime.timezone.utc),
            'Template': 'WebServer', 'SANs': {'ip4': ['192.168.2.2']}}.

    Returns:
        Response[ModelsEnrollmentCSREnrollmentResponse]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
        x_keyfactor_api_version=x_keyfactor_api_version,
        x_keyfactor_requested_with=x_keyfactor_requested_with,
        x_certificateformat=x_certificateformat,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
    json_body: ModelsEnrollmentCSREnrollmentRequest,
    x_keyfactor_api_version: Union[Unset, str] = "1",
    x_keyfactor_requested_with: str = "APIClient",
    x_certificateformat: str = "PEM",
) -> Optional[ModelsEnrollmentCSREnrollmentResponse]:
    """Performs a CSR Enrollment based upon the provided request

     ### Subject Alternative Name Flags ###
    | Value              | Description               |
    |--------------------|---------------------------|
    | other              | OtherName                 |
    | rfc822             | RFC822Name                |
    | dns                | DNSName                   |
    | x400               | X400Address               |
    | directory          | DirectoryName             |
    | ediparty           | EdipartyName              |
    | uri                | UniformResourceIdentifier |
    | ip                 | IPAddress                 |
    | ip4                | IPv4Address               |
    | ip6                | IPv6Address               |
    | registeredid       | RegisteredId              |
    | ms_ntprincipalname | MS_NTPrincipalName        |
    | ms_ntdsreplication | MS_NTDSReplication        |

    Args:
        x_keyfactor_api_version (Union[Unset, str]):  Default: '1'.
        x_keyfactor_requested_with (str):  Default: 'APIClient'.
        x_certificateformat (str):  Default: 'PEM'.
        json_body (ModelsEnrollmentCSREnrollmentRequest):  Example: {'CSR': '<base64-encoded
            CSR>', 'CertificateAuthority': '<host\\logical>', 'IncludeChain': False, 'Timestamp':
            datetime.datetime(2022, 9, 22, 18, 9, 16, 719678, tzinfo=datetime.timezone.utc),
            'Template': 'WebServer', 'SANs': {'ip4': ['192.168.2.2']}}.

    Returns:
        Response[ModelsEnrollmentCSREnrollmentResponse]
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
        x_keyfactor_api_version=x_keyfactor_api_version,
        x_keyfactor_requested_with=x_keyfactor_requested_with,
        x_certificateformat=x_certificateformat,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    json_body: ModelsEnrollmentCSREnrollmentRequest,
    x_keyfactor_api_version: Union[Unset, str] = "1",
    x_keyfactor_requested_with: str = "APIClient",
    x_certificateformat: str = "PEM",
) -> Response[ModelsEnrollmentCSREnrollmentResponse]:
    """Performs a CSR Enrollment based upon the provided request

     ### Subject Alternative Name Flags ###
    | Value              | Description               |
    |--------------------|---------------------------|
    | other              | OtherName                 |
    | rfc822             | RFC822Name                |
    | dns                | DNSName                   |
    | x400               | X400Address               |
    | directory          | DirectoryName             |
    | ediparty           | EdipartyName              |
    | uri                | UniformResourceIdentifier |
    | ip                 | IPAddress                 |
    | ip4                | IPv4Address               |
    | ip6                | IPv6Address               |
    | registeredid       | RegisteredId              |
    | ms_ntprincipalname | MS_NTPrincipalName        |
    | ms_ntdsreplication | MS_NTDSReplication        |

    Args:
        x_keyfactor_api_version (Union[Unset, str]):  Default: '1'.
        x_keyfactor_requested_with (str):  Default: 'APIClient'.
        x_certificateformat (str):  Default: 'PEM'.
        json_body (ModelsEnrollmentCSREnrollmentRequest):  Example: {'CSR': '<base64-encoded
            CSR>', 'CertificateAuthority': '<host\\logical>', 'IncludeChain': False, 'Timestamp':
            datetime.datetime(2022, 9, 22, 18, 9, 16, 719678, tzinfo=datetime.timezone.utc),
            'Template': 'WebServer', 'SANs': {'ip4': ['192.168.2.2']}}.

    Returns:
        Response[ModelsEnrollmentCSREnrollmentResponse]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
        x_keyfactor_api_version=x_keyfactor_api_version,
        x_keyfactor_requested_with=x_keyfactor_requested_with,
        x_certificateformat=x_certificateformat,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    json_body: ModelsEnrollmentCSREnrollmentRequest,
    x_keyfactor_api_version: Union[Unset, str] = "1",
    x_keyfactor_requested_with: str = "APIClient",
    x_certificateformat: str = "PEM",
) -> Optional[ModelsEnrollmentCSREnrollmentResponse]:
    """Performs a CSR Enrollment based upon the provided request

     ### Subject Alternative Name Flags ###
    | Value              | Description               |
    |--------------------|---------------------------|
    | other              | OtherName                 |
    | rfc822             | RFC822Name                |
    | dns                | DNSName                   |
    | x400               | X400Address               |
    | directory          | DirectoryName             |
    | ediparty           | EdipartyName              |
    | uri                | UniformResourceIdentifier |
    | ip                 | IPAddress                 |
    | ip4                | IPv4Address               |
    | ip6                | IPv6Address               |
    | registeredid       | RegisteredId              |
    | ms_ntprincipalname | MS_NTPrincipalName        |
    | ms_ntdsreplication | MS_NTDSReplication        |

    Args:
        x_keyfactor_api_version (Union[Unset, str]):  Default: '1'.
        x_keyfactor_requested_with (str):  Default: 'APIClient'.
        x_certificateformat (str):  Default: 'PEM'.
        json_body (ModelsEnrollmentCSREnrollmentRequest):  Example: {'CSR': '<base64-encoded
            CSR>', 'CertificateAuthority': '<host\\logical>', 'IncludeChain': False, 'Timestamp':
            datetime.datetime(2022, 9, 22, 18, 9, 16, 719678, tzinfo=datetime.timezone.utc),
            'Template': 'WebServer', 'SANs': {'ip4': ['192.168.2.2']}}.

    Returns:
        Response[ModelsEnrollmentCSREnrollmentResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
            x_keyfactor_api_version=x_keyfactor_api_version,
            x_keyfactor_requested_with=x_keyfactor_requested_with,
            x_certificateformat=x_certificateformat,
        )
    ).parsed
