from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.models_ssl_scan_job_part import ModelsSSLScanJobPart
from ...types import Response, Unset


def _get_kwargs(
    id: str,
    *,
    client: Client,
    x_keyfactor_api_version: Union[Unset, str] = "1",
    x_keyfactor_requested_with: str = "APIClient",
) -> Dict[str, Any]:
    url = "{}/SSL/Parts/{id}".format(client.base_url, id=id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    if not isinstance(x_keyfactor_api_version, Unset):
        headers["x-keyfactor-api-version"] = x_keyfactor_api_version

    headers["x-keyfactor-requested-with"] = x_keyfactor_requested_with

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[ModelsSSLScanJobPart]:
    if response.status_code == 200:
        response_200 = ModelsSSLScanJobPart.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[ModelsSSLScanJobPart]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    id: str,
    *,
    client: Client,
    x_keyfactor_api_version: Union[Unset, str] = "1",
    x_keyfactor_requested_with: str = "APIClient",
) -> Response[ModelsSSLScanJobPart]:
    """Returns the execution details of the associated network scan job part

    Args:
        id (str):
        x_keyfactor_api_version (Union[Unset, str]):  Default: '1'.
        x_keyfactor_requested_with (str):  Default: 'APIClient'.

    Returns:
        Response[ModelsSSLScanJobPart]
    """

    kwargs = _get_kwargs(
        id=id,
        client=client,
        x_keyfactor_api_version=x_keyfactor_api_version,
        x_keyfactor_requested_with=x_keyfactor_requested_with,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    id: str,
    *,
    client: Client,
    x_keyfactor_api_version: Union[Unset, str] = "1",
    x_keyfactor_requested_with: str = "APIClient",
) -> Optional[ModelsSSLScanJobPart]:
    """Returns the execution details of the associated network scan job part

    Args:
        id (str):
        x_keyfactor_api_version (Union[Unset, str]):  Default: '1'.
        x_keyfactor_requested_with (str):  Default: 'APIClient'.

    Returns:
        Response[ModelsSSLScanJobPart]
    """

    return sync_detailed(
        id=id,
        client=client,
        x_keyfactor_api_version=x_keyfactor_api_version,
        x_keyfactor_requested_with=x_keyfactor_requested_with,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: Client,
    x_keyfactor_api_version: Union[Unset, str] = "1",
    x_keyfactor_requested_with: str = "APIClient",
) -> Response[ModelsSSLScanJobPart]:
    """Returns the execution details of the associated network scan job part

    Args:
        id (str):
        x_keyfactor_api_version (Union[Unset, str]):  Default: '1'.
        x_keyfactor_requested_with (str):  Default: 'APIClient'.

    Returns:
        Response[ModelsSSLScanJobPart]
    """

    kwargs = _get_kwargs(
        id=id,
        client=client,
        x_keyfactor_api_version=x_keyfactor_api_version,
        x_keyfactor_requested_with=x_keyfactor_requested_with,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    id: str,
    *,
    client: Client,
    x_keyfactor_api_version: Union[Unset, str] = "1",
    x_keyfactor_requested_with: str = "APIClient",
) -> Optional[ModelsSSLScanJobPart]:
    """Returns the execution details of the associated network scan job part

    Args:
        id (str):
        x_keyfactor_api_version (Union[Unset, str]):  Default: '1'.
        x_keyfactor_requested_with (str):  Default: 'APIClient'.

    Returns:
        Response[ModelsSSLScanJobPart]
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            x_keyfactor_api_version=x_keyfactor_api_version,
            x_keyfactor_requested_with=x_keyfactor_requested_with,
        )
    ).parsed
