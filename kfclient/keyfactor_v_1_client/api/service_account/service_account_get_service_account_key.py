from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.models_ssh_keys_key_response import ModelsSSHKeysKeyResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: int,
    *,
    client: Client,
    include_private_key: Union[Unset, None, bool] = UNSET,
    x_keyfactor_api_version: Union[Unset, str] = "1",
    x_keyfactor_requested_with: str = "APIClient",
) -> Dict[str, Any]:
    url = "{}/SSH/ServiceAccounts/Key/{id}".format(client.base_url, id=id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    if not isinstance(x_keyfactor_api_version, Unset):
        headers["x-keyfactor-api-version"] = x_keyfactor_api_version

    headers["x-keyfactor-requested-with"] = x_keyfactor_requested_with

    params: Dict[str, Any] = {}
    params["includePrivateKey"] = include_private_key

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[ModelsSSHKeysKeyResponse]:
    if response.status_code == 200:
        response_200 = ModelsSSHKeysKeyResponse.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[ModelsSSHKeysKeyResponse]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    id: int,
    *,
    client: Client,
    include_private_key: Union[Unset, None, bool] = UNSET,
    x_keyfactor_api_version: Union[Unset, str] = "1",
    x_keyfactor_requested_with: str = "APIClient",
) -> Response[ModelsSSHKeysKeyResponse]:
    """Returns an SSH key with or without private key based on the provided parameters.

    Args:
        id (int):
        include_private_key (Union[Unset, None, bool]):
        x_keyfactor_api_version (Union[Unset, str]):  Default: '1'.
        x_keyfactor_requested_with (str):  Default: 'APIClient'.

    Returns:
        Response[ModelsSSHKeysKeyResponse]
    """

    kwargs = _get_kwargs(
        id=id,
        client=client,
        include_private_key=include_private_key,
        x_keyfactor_api_version=x_keyfactor_api_version,
        x_keyfactor_requested_with=x_keyfactor_requested_with,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    id: int,
    *,
    client: Client,
    include_private_key: Union[Unset, None, bool] = UNSET,
    x_keyfactor_api_version: Union[Unset, str] = "1",
    x_keyfactor_requested_with: str = "APIClient",
) -> Optional[ModelsSSHKeysKeyResponse]:
    """Returns an SSH key with or without private key based on the provided parameters.

    Args:
        id (int):
        include_private_key (Union[Unset, None, bool]):
        x_keyfactor_api_version (Union[Unset, str]):  Default: '1'.
        x_keyfactor_requested_with (str):  Default: 'APIClient'.

    Returns:
        Response[ModelsSSHKeysKeyResponse]
    """

    return sync_detailed(
        id=id,
        client=client,
        include_private_key=include_private_key,
        x_keyfactor_api_version=x_keyfactor_api_version,
        x_keyfactor_requested_with=x_keyfactor_requested_with,
    ).parsed


async def asyncio_detailed(
    id: int,
    *,
    client: Client,
    include_private_key: Union[Unset, None, bool] = UNSET,
    x_keyfactor_api_version: Union[Unset, str] = "1",
    x_keyfactor_requested_with: str = "APIClient",
) -> Response[ModelsSSHKeysKeyResponse]:
    """Returns an SSH key with or without private key based on the provided parameters.

    Args:
        id (int):
        include_private_key (Union[Unset, None, bool]):
        x_keyfactor_api_version (Union[Unset, str]):  Default: '1'.
        x_keyfactor_requested_with (str):  Default: 'APIClient'.

    Returns:
        Response[ModelsSSHKeysKeyResponse]
    """

    kwargs = _get_kwargs(
        id=id,
        client=client,
        include_private_key=include_private_key,
        x_keyfactor_api_version=x_keyfactor_api_version,
        x_keyfactor_requested_with=x_keyfactor_requested_with,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    id: int,
    *,
    client: Client,
    include_private_key: Union[Unset, None, bool] = UNSET,
    x_keyfactor_api_version: Union[Unset, str] = "1",
    x_keyfactor_requested_with: str = "APIClient",
) -> Optional[ModelsSSHKeysKeyResponse]:
    """Returns an SSH key with or without private key based on the provided parameters.

    Args:
        id (int):
        include_private_key (Union[Unset, None, bool]):
        x_keyfactor_api_version (Union[Unset, str]):  Default: '1'.
        x_keyfactor_requested_with (str):  Default: 'APIClient'.

    Returns:
        Response[ModelsSSHKeysKeyResponse]
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            include_private_key=include_private_key,
            x_keyfactor_api_version=x_keyfactor_api_version,
            x_keyfactor_requested_with=x_keyfactor_requested_with,
        )
    ).parsed
