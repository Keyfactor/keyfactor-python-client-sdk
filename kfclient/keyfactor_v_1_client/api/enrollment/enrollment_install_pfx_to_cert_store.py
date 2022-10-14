from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.keyfactor_api_models_enrollment_enrollment_management_request import (
    KeyfactorApiModelsEnrollmentEnrollmentManagementRequest,
)
from ...models.keyfactor_api_models_enrollment_enrollment_management_response import (
    KeyfactorAPIModelsEnrollmentEnrollmentManagementResponse,
)
from ...types import Response, Unset


def _get_kwargs(
    *,
    client: Client,
    json_body: KeyfactorApiModelsEnrollmentEnrollmentManagementRequest,
    x_keyfactor_api_version: Union[Unset, str] = "1",
    x_keyfactor_requested_with: str = "APIClient",
) -> Dict[str, Any]:
    url = "{}/Enrollment/PFX/Deploy".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    if not isinstance(x_keyfactor_api_version, Unset):
        headers["x-keyfactor-api-version"] = x_keyfactor_api_version

    headers["x-keyfactor-requested-with"] = x_keyfactor_requested_with

    json_json_body = json_body.to_dict()

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
    }


def _parse_response(*, response: httpx.Response) -> Optional[KeyfactorAPIModelsEnrollmentEnrollmentManagementResponse]:
    if response.status_code == 200:
        response_200 = KeyfactorAPIModelsEnrollmentEnrollmentManagementResponse.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[KeyfactorAPIModelsEnrollmentEnrollmentManagementResponse]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    json_body: KeyfactorApiModelsEnrollmentEnrollmentManagementRequest,
    x_keyfactor_api_version: Union[Unset, str] = "1",
    x_keyfactor_requested_with: str = "APIClient",
) -> Response[KeyfactorAPIModelsEnrollmentEnrollmentManagementResponse]:
    """Creates management jobs to install a newly enrolled pfx in to one or more certificate stores

    Args:
        x_keyfactor_api_version (Union[Unset, str]):  Default: '1'.
        x_keyfactor_requested_with (str):  Default: 'APIClient'.
        json_body (KeyfactorApiModelsEnrollmentEnrollmentManagementRequest):  Example: {'Stores':
            [{'StoreId': '00000000-0000-0000-0000-000000000000', 'Alias': '<store alias>',
            'Overwrite': True, 'Properties': {'Netscalervserver': 'thevalue'}}], 'CertificateId': 0,
            'RequestId': 0, 'Password': '<pfx password>', 'JobTime': datetime.datetime(2022, 9, 23,
            18, 9, 16, 719678, tzinfo=datetime.timezone.utc)}.

    Returns:
        Response[KeyfactorAPIModelsEnrollmentEnrollmentManagementResponse]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
        x_keyfactor_api_version=x_keyfactor_api_version,
        x_keyfactor_requested_with=x_keyfactor_requested_with,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
    json_body: KeyfactorApiModelsEnrollmentEnrollmentManagementRequest,
    x_keyfactor_api_version: Union[Unset, str] = "1",
    x_keyfactor_requested_with: str = "APIClient",
) -> Optional[KeyfactorAPIModelsEnrollmentEnrollmentManagementResponse]:
    """Creates management jobs to install a newly enrolled pfx in to one or more certificate stores

    Args:
        x_keyfactor_api_version (Union[Unset, str]):  Default: '1'.
        x_keyfactor_requested_with (str):  Default: 'APIClient'.
        json_body (KeyfactorApiModelsEnrollmentEnrollmentManagementRequest):  Example: {'Stores':
            [{'StoreId': '00000000-0000-0000-0000-000000000000', 'Alias': '<store alias>',
            'Overwrite': True, 'Properties': {'Netscalervserver': 'thevalue'}}], 'CertificateId': 0,
            'RequestId': 0, 'Password': '<pfx password>', 'JobTime': datetime.datetime(2022, 9, 23,
            18, 9, 16, 719678, tzinfo=datetime.timezone.utc)}.

    Returns:
        Response[KeyfactorAPIModelsEnrollmentEnrollmentManagementResponse]
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
        x_keyfactor_api_version=x_keyfactor_api_version,
        x_keyfactor_requested_with=x_keyfactor_requested_with,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    json_body: KeyfactorApiModelsEnrollmentEnrollmentManagementRequest,
    x_keyfactor_api_version: Union[Unset, str] = "1",
    x_keyfactor_requested_with: str = "APIClient",
) -> Response[KeyfactorAPIModelsEnrollmentEnrollmentManagementResponse]:
    """Creates management jobs to install a newly enrolled pfx in to one or more certificate stores

    Args:
        x_keyfactor_api_version (Union[Unset, str]):  Default: '1'.
        x_keyfactor_requested_with (str):  Default: 'APIClient'.
        json_body (KeyfactorApiModelsEnrollmentEnrollmentManagementRequest):  Example: {'Stores':
            [{'StoreId': '00000000-0000-0000-0000-000000000000', 'Alias': '<store alias>',
            'Overwrite': True, 'Properties': {'Netscalervserver': 'thevalue'}}], 'CertificateId': 0,
            'RequestId': 0, 'Password': '<pfx password>', 'JobTime': datetime.datetime(2022, 9, 23,
            18, 9, 16, 719678, tzinfo=datetime.timezone.utc)}.

    Returns:
        Response[KeyfactorAPIModelsEnrollmentEnrollmentManagementResponse]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
        x_keyfactor_api_version=x_keyfactor_api_version,
        x_keyfactor_requested_with=x_keyfactor_requested_with,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    json_body: KeyfactorApiModelsEnrollmentEnrollmentManagementRequest,
    x_keyfactor_api_version: Union[Unset, str] = "1",
    x_keyfactor_requested_with: str = "APIClient",
) -> Optional[KeyfactorAPIModelsEnrollmentEnrollmentManagementResponse]:
    """Creates management jobs to install a newly enrolled pfx in to one or more certificate stores

    Args:
        x_keyfactor_api_version (Union[Unset, str]):  Default: '1'.
        x_keyfactor_requested_with (str):  Default: 'APIClient'.
        json_body (KeyfactorApiModelsEnrollmentEnrollmentManagementRequest):  Example: {'Stores':
            [{'StoreId': '00000000-0000-0000-0000-000000000000', 'Alias': '<store alias>',
            'Overwrite': True, 'Properties': {'Netscalervserver': 'thevalue'}}], 'CertificateId': 0,
            'RequestId': 0, 'Password': '<pfx password>', 'JobTime': datetime.datetime(2022, 9, 23,
            18, 9, 16, 719678, tzinfo=datetime.timezone.utc)}.

    Returns:
        Response[KeyfactorAPIModelsEnrollmentEnrollmentManagementResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
            x_keyfactor_api_version=x_keyfactor_api_version,
            x_keyfactor_requested_with=x_keyfactor_requested_with,
        )
    ).parsed
