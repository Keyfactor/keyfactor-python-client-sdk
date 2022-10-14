from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.models_ssh_keys_key_response import ModelsSSHKeysKeyResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    include_private_key: Union[Unset, None, bool] = UNSET,
    x_keyfactor_api_version: Union[Unset, str] = "1",
    x_keyfactor_requested_with: str = "APIClient",
    x_keyfactor_key_passphrase: str,
) -> Dict[str, Any]:
    url = "{}/SSH/Keys/MyKey".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    if not isinstance(x_keyfactor_api_version, Unset):
        headers["x-keyfactor-api-version"] = x_keyfactor_api_version

    headers["x-keyfactor-requested-with"] = x_keyfactor_requested_with

    headers["x-keyfactor-key-passphrase"] = x_keyfactor_key_passphrase

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
    *,
    client: Client,
    include_private_key: Union[Unset, None, bool] = UNSET,
    x_keyfactor_api_version: Union[Unset, str] = "1",
    x_keyfactor_requested_with: str = "APIClient",
    x_keyfactor_key_passphrase: str,
) -> Response[ModelsSSHKeysKeyResponse]:
    """Returns the current key of the requesting user

    Args:
        include_private_key (Union[Unset, None, bool]):
        x_keyfactor_api_version (Union[Unset, str]):  Default: '1'.
        x_keyfactor_requested_with (str):  Default: 'APIClient'.
        x_keyfactor_key_passphrase (str):

    Returns:
        Response[ModelsSSHKeysKeyResponse]
    """

    kwargs = _get_kwargs(
        client=client,
        include_private_key=include_private_key,
        x_keyfactor_api_version=x_keyfactor_api_version,
        x_keyfactor_requested_with=x_keyfactor_requested_with,
        x_keyfactor_key_passphrase=x_keyfactor_key_passphrase,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
    include_private_key: Union[Unset, None, bool] = UNSET,
    x_keyfactor_api_version: Union[Unset, str] = "1",
    x_keyfactor_requested_with: str = "APIClient",
    x_keyfactor_key_passphrase: str,
) -> Optional[ModelsSSHKeysKeyResponse]:
    """Returns the current key of the requesting user

    Args:
        include_private_key (Union[Unset, None, bool]):
        x_keyfactor_api_version (Union[Unset, str]):  Default: '1'.
        x_keyfactor_requested_with (str):  Default: 'APIClient'.
        x_keyfactor_key_passphrase (str):

    Returns:
        Response[ModelsSSHKeysKeyResponse]
    """

    return sync_detailed(
        client=client,
        include_private_key=include_private_key,
        x_keyfactor_api_version=x_keyfactor_api_version,
        x_keyfactor_requested_with=x_keyfactor_requested_with,
        x_keyfactor_key_passphrase=x_keyfactor_key_passphrase,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    include_private_key: Union[Unset, None, bool] = UNSET,
    x_keyfactor_api_version: Union[Unset, str] = "1",
    x_keyfactor_requested_with: str = "APIClient",
    x_keyfactor_key_passphrase: str,
) -> Response[ModelsSSHKeysKeyResponse]:
    """Returns the current key of the requesting user

    Args:
        include_private_key (Union[Unset, None, bool]):
        x_keyfactor_api_version (Union[Unset, str]):  Default: '1'.
        x_keyfactor_requested_with (str):  Default: 'APIClient'.
        x_keyfactor_key_passphrase (str):

    Returns:
        Response[ModelsSSHKeysKeyResponse]
    """

    kwargs = _get_kwargs(
        client=client,
        include_private_key=include_private_key,
        x_keyfactor_api_version=x_keyfactor_api_version,
        x_keyfactor_requested_with=x_keyfactor_requested_with,
        x_keyfactor_key_passphrase=x_keyfactor_key_passphrase,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    include_private_key: Union[Unset, None, bool] = UNSET,
    x_keyfactor_api_version: Union[Unset, str] = "1",
    x_keyfactor_requested_with: str = "APIClient",
    x_keyfactor_key_passphrase: str,
) -> Optional[ModelsSSHKeysKeyResponse]:
    """Returns the current key of the requesting user

    Args:
        include_private_key (Union[Unset, None, bool]):
        x_keyfactor_api_version (Union[Unset, str]):  Default: '1'.
        x_keyfactor_requested_with (str):  Default: 'APIClient'.
        x_keyfactor_key_passphrase (str):

    Returns:
        Response[ModelsSSHKeysKeyResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            include_private_key=include_private_key,
            x_keyfactor_api_version=x_keyfactor_api_version,
            x_keyfactor_requested_with=x_keyfactor_requested_with,
            x_keyfactor_key_passphrase=x_keyfactor_key_passphrase,
        )
    ).parsed
