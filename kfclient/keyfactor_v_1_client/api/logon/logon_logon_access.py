from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.models_ssh_access_logon_user_access_response import ModelsSSHAccessLogonUserAccessResponse
from ...models.models_ssh_logons_logon_access_request import ModelsSSHLogonsLogonAccessRequest
from ...types import Response, Unset


def _get_kwargs(
    *,
    client: Client,
    json_body: ModelsSSHLogonsLogonAccessRequest,
    x_keyfactor_api_version: Union[Unset, str] = "1",
    x_keyfactor_requested_with: str = "APIClient",
) -> Dict[str, Any]:
    url = "{}/SSH/Logons/Access".format(client.base_url)

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


def _parse_response(*, response: httpx.Response) -> Optional[ModelsSSHAccessLogonUserAccessResponse]:
    if response.status_code == 200:
        response_200 = ModelsSSHAccessLogonUserAccessResponse.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[ModelsSSHAccessLogonUserAccessResponse]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    json_body: ModelsSSHLogonsLogonAccessRequest,
    x_keyfactor_api_version: Union[Unset, str] = "1",
    x_keyfactor_requested_with: str = "APIClient",
) -> Response[ModelsSSHAccessLogonUserAccessResponse]:
    """Updates the users with access to an existing logon

    Args:
        x_keyfactor_api_version (Union[Unset, str]):  Default: '1'.
        x_keyfactor_requested_with (str):  Default: 'APIClient'.
        json_body (ModelsSSHLogonsLogonAccessRequest):

    Returns:
        Response[ModelsSSHAccessLogonUserAccessResponse]
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
    json_body: ModelsSSHLogonsLogonAccessRequest,
    x_keyfactor_api_version: Union[Unset, str] = "1",
    x_keyfactor_requested_with: str = "APIClient",
) -> Optional[ModelsSSHAccessLogonUserAccessResponse]:
    """Updates the users with access to an existing logon

    Args:
        x_keyfactor_api_version (Union[Unset, str]):  Default: '1'.
        x_keyfactor_requested_with (str):  Default: 'APIClient'.
        json_body (ModelsSSHLogonsLogonAccessRequest):

    Returns:
        Response[ModelsSSHAccessLogonUserAccessResponse]
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
    json_body: ModelsSSHLogonsLogonAccessRequest,
    x_keyfactor_api_version: Union[Unset, str] = "1",
    x_keyfactor_requested_with: str = "APIClient",
) -> Response[ModelsSSHAccessLogonUserAccessResponse]:
    """Updates the users with access to an existing logon

    Args:
        x_keyfactor_api_version (Union[Unset, str]):  Default: '1'.
        x_keyfactor_requested_with (str):  Default: 'APIClient'.
        json_body (ModelsSSHLogonsLogonAccessRequest):

    Returns:
        Response[ModelsSSHAccessLogonUserAccessResponse]
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
    json_body: ModelsSSHLogonsLogonAccessRequest,
    x_keyfactor_api_version: Union[Unset, str] = "1",
    x_keyfactor_requested_with: str = "APIClient",
) -> Optional[ModelsSSHAccessLogonUserAccessResponse]:
    """Updates the users with access to an existing logon

    Args:
        x_keyfactor_api_version (Union[Unset, str]):  Default: '1'.
        x_keyfactor_requested_with (str):  Default: 'APIClient'.
        json_body (ModelsSSHLogonsLogonAccessRequest):

    Returns:
        Response[ModelsSSHAccessLogonUserAccessResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
            x_keyfactor_api_version=x_keyfactor_api_version,
            x_keyfactor_requested_with=x_keyfactor_requested_with,
        )
    ).parsed