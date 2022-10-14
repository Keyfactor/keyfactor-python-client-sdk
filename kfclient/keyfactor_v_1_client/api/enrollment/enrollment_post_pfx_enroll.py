from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.models_enrollment_pfx_enrollment_request import ModelsEnrollmentPFXEnrollmentRequest
from ...models.models_enrollment_pfx_enrollment_response import ModelsEnrollmentPFXEnrollmentResponse
from ...types import Response, Unset


def _get_kwargs(
    *,
    client: Client,
    json_body: ModelsEnrollmentPFXEnrollmentRequest,
    x_keyfactor_api_version: Union[Unset, str] = "1",
    x_keyfactor_requested_with: str = "APIClient",
    x_certificateformat: str = "PFX",
) -> Dict[str, Any]:
    url = "{}/Enrollment/PFX".format(client.base_url)

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


def _parse_response(*, response: httpx.Response) -> Optional[ModelsEnrollmentPFXEnrollmentResponse]:
    if response.status_code == 200:
        response_200 = ModelsEnrollmentPFXEnrollmentResponse.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[ModelsEnrollmentPFXEnrollmentResponse]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    json_body: ModelsEnrollmentPFXEnrollmentRequest,
    x_keyfactor_api_version: Union[Unset, str] = "1",
    x_keyfactor_requested_with: str = "APIClient",
    x_certificateformat: str = "PFX",
) -> Response[ModelsEnrollmentPFXEnrollmentResponse]:
    """Performs a PFX Enrollment based upon the provided request

     ### IMPORTANT:
    - The <b>'RenewalCertificateId'</b> field in the request should be set to <b>null</b> if the
    certificate is not being renewed as part of the enrollment. A value of <b>0</b> will produce an
    error.

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
        x_certificateformat (str):  Default: 'PFX'.
        json_body (ModelsEnrollmentPFXEnrollmentRequest):  Example: {'CustomFriendlyName':
            '<custom name>', 'Password': '<pfx password>', 'PopulateMissingValuesFromAD': False,
            'Subject': '<certificate subject>', 'IncludeChain': True, 'RenewalCertificateId': 0,
            'CertificateAuthority': '<host>\\<logical>', 'Timestamp': datetime.datetime(2022, 9, 22,
            18, 9, 16, 719678, tzinfo=datetime.timezone.utc), 'Template': '<template short name>',
            'SANs': {'ip4': ['192.168.2.2']}}.

    Returns:
        Response[ModelsEnrollmentPFXEnrollmentResponse]
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
    json_body: ModelsEnrollmentPFXEnrollmentRequest,
    x_keyfactor_api_version: Union[Unset, str] = "1",
    x_keyfactor_requested_with: str = "APIClient",
    x_certificateformat: str = "PFX",
) -> Optional[ModelsEnrollmentPFXEnrollmentResponse]:
    """Performs a PFX Enrollment based upon the provided request

     ### IMPORTANT:
    - The <b>'RenewalCertificateId'</b> field in the request should be set to <b>null</b> if the
    certificate is not being renewed as part of the enrollment. A value of <b>0</b> will produce an
    error.

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
        x_certificateformat (str):  Default: 'PFX'.
        json_body (ModelsEnrollmentPFXEnrollmentRequest):  Example: {'CustomFriendlyName':
            '<custom name>', 'Password': '<pfx password>', 'PopulateMissingValuesFromAD': False,
            'Subject': '<certificate subject>', 'IncludeChain': True, 'RenewalCertificateId': 0,
            'CertificateAuthority': '<host>\\<logical>', 'Timestamp': datetime.datetime(2022, 9, 22,
            18, 9, 16, 719678, tzinfo=datetime.timezone.utc), 'Template': '<template short name>',
            'SANs': {'ip4': ['192.168.2.2']}}.

    Returns:
        Response[ModelsEnrollmentPFXEnrollmentResponse]
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
    json_body: ModelsEnrollmentPFXEnrollmentRequest,
    x_keyfactor_api_version: Union[Unset, str] = "1",
    x_keyfactor_requested_with: str = "APIClient",
    x_certificateformat: str = "PFX",
) -> Response[ModelsEnrollmentPFXEnrollmentResponse]:
    """Performs a PFX Enrollment based upon the provided request

     ### IMPORTANT:
    - The <b>'RenewalCertificateId'</b> field in the request should be set to <b>null</b> if the
    certificate is not being renewed as part of the enrollment. A value of <b>0</b> will produce an
    error.

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
        x_certificateformat (str):  Default: 'PFX'.
        json_body (ModelsEnrollmentPFXEnrollmentRequest):  Example: {'CustomFriendlyName':
            '<custom name>', 'Password': '<pfx password>', 'PopulateMissingValuesFromAD': False,
            'Subject': '<certificate subject>', 'IncludeChain': True, 'RenewalCertificateId': 0,
            'CertificateAuthority': '<host>\\<logical>', 'Timestamp': datetime.datetime(2022, 9, 22,
            18, 9, 16, 719678, tzinfo=datetime.timezone.utc), 'Template': '<template short name>',
            'SANs': {'ip4': ['192.168.2.2']}}.

    Returns:
        Response[ModelsEnrollmentPFXEnrollmentResponse]
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
    json_body: ModelsEnrollmentPFXEnrollmentRequest,
    x_keyfactor_api_version: Union[Unset, str] = "1",
    x_keyfactor_requested_with: str = "APIClient",
    x_certificateformat: str = "PFX",
) -> Optional[ModelsEnrollmentPFXEnrollmentResponse]:
    """Performs a PFX Enrollment based upon the provided request

     ### IMPORTANT:
    - The <b>'RenewalCertificateId'</b> field in the request should be set to <b>null</b> if the
    certificate is not being renewed as part of the enrollment. A value of <b>0</b> will produce an
    error.

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
        x_certificateformat (str):  Default: 'PFX'.
        json_body (ModelsEnrollmentPFXEnrollmentRequest):  Example: {'CustomFriendlyName':
            '<custom name>', 'Password': '<pfx password>', 'PopulateMissingValuesFromAD': False,
            'Subject': '<certificate subject>', 'IncludeChain': True, 'RenewalCertificateId': 0,
            'CertificateAuthority': '<host>\\<logical>', 'Timestamp': datetime.datetime(2022, 9, 22,
            18, 9, 16, 719678, tzinfo=datetime.timezone.utc), 'Template': '<template short name>',
            'SANs': {'ip4': ['192.168.2.2']}}.

    Returns:
        Response[ModelsEnrollmentPFXEnrollmentResponse]
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
