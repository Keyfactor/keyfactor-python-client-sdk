from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.models_security_identities_security_identity_lookup_response import (
    ModelsSecurityIdentitiesSecurityIdentityLookupResponse,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    account_name: str,
    x_keyfactor_api_version: Union[Unset, str] = "1",
    x_keyfactor_requested_with: str = "APIClient",
) -> Dict[str, Any]:
    url = "{}/Security/Identities/Lookup".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    if not isinstance(x_keyfactor_api_version, Unset):
        headers["x-keyfactor-api-version"] = x_keyfactor_api_version

    headers["x-keyfactor-requested-with"] = x_keyfactor_requested_with

    params: Dict[str, Any] = {}
    params["accountName"] = account_name

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[ModelsSecurityIdentitiesSecurityIdentityLookupResponse]:
    if response.status_code == 200:
        response_200 = ModelsSecurityIdentitiesSecurityIdentityLookupResponse.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[ModelsSecurityIdentitiesSecurityIdentityLookupResponse]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    account_name: str,
    x_keyfactor_api_version: Union[Unset, str] = "1",
    x_keyfactor_requested_with: str = "APIClient",
) -> Response[ModelsSecurityIdentitiesSecurityIdentityLookupResponse]:
    """Validates that the identity with the name given exists.

    Args:
        account_name (str):
        x_keyfactor_api_version (Union[Unset, str]):  Default: '1'.
        x_keyfactor_requested_with (str):  Default: 'APIClient'.

    Returns:
        Response[ModelsSecurityIdentitiesSecurityIdentityLookupResponse]
    """

    kwargs = _get_kwargs(
        client=client,
        account_name=account_name,
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
    account_name: str,
    x_keyfactor_api_version: Union[Unset, str] = "1",
    x_keyfactor_requested_with: str = "APIClient",
) -> Optional[ModelsSecurityIdentitiesSecurityIdentityLookupResponse]:
    """Validates that the identity with the name given exists.

    Args:
        account_name (str):
        x_keyfactor_api_version (Union[Unset, str]):  Default: '1'.
        x_keyfactor_requested_with (str):  Default: 'APIClient'.

    Returns:
        Response[ModelsSecurityIdentitiesSecurityIdentityLookupResponse]
    """

    return sync_detailed(
        client=client,
        account_name=account_name,
        x_keyfactor_api_version=x_keyfactor_api_version,
        x_keyfactor_requested_with=x_keyfactor_requested_with,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    account_name: str,
    x_keyfactor_api_version: Union[Unset, str] = "1",
    x_keyfactor_requested_with: str = "APIClient",
) -> Response[ModelsSecurityIdentitiesSecurityIdentityLookupResponse]:
    """Validates that the identity with the name given exists.

    Args:
        account_name (str):
        x_keyfactor_api_version (Union[Unset, str]):  Default: '1'.
        x_keyfactor_requested_with (str):  Default: 'APIClient'.

    Returns:
        Response[ModelsSecurityIdentitiesSecurityIdentityLookupResponse]
    """

    kwargs = _get_kwargs(
        client=client,
        account_name=account_name,
        x_keyfactor_api_version=x_keyfactor_api_version,
        x_keyfactor_requested_with=x_keyfactor_requested_with,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    account_name: str,
    x_keyfactor_api_version: Union[Unset, str] = "1",
    x_keyfactor_requested_with: str = "APIClient",
) -> Optional[ModelsSecurityIdentitiesSecurityIdentityLookupResponse]:
    """Validates that the identity with the name given exists.

    Args:
        account_name (str):
        x_keyfactor_api_version (Union[Unset, str]):  Default: '1'.
        x_keyfactor_requested_with (str):  Default: 'APIClient'.

    Returns:
        Response[ModelsSecurityIdentitiesSecurityIdentityLookupResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            account_name=account_name,
            x_keyfactor_api_version=x_keyfactor_api_version,
            x_keyfactor_requested_with=x_keyfactor_requested_with,
        )
    ).parsed