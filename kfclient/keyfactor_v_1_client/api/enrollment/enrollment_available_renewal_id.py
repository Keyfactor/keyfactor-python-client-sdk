from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.models_enrollment_available_renewal import ModelsEnrollmentAvailableRenewal
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: int,
    *,
    client: Client,
    collection_id: Union[Unset, None, int] = UNSET,
    x_keyfactor_api_version: Union[Unset, str] = "1",
    x_keyfactor_requested_with: str = "APIClient",
) -> Dict[str, Any]:
    url = "{}/Enrollment/AvailableRenewal/Id/{id}".format(client.base_url, id=id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    if not isinstance(x_keyfactor_api_version, Unset):
        headers["x-keyfactor-api-version"] = x_keyfactor_api_version

    headers["x-keyfactor-requested-with"] = x_keyfactor_requested_with

    params: Dict[str, Any] = {}
    params["collectionId"] = collection_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[ModelsEnrollmentAvailableRenewal]:
    if response.status_code == 200:
        response_200 = ModelsEnrollmentAvailableRenewal.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[ModelsEnrollmentAvailableRenewal]:
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
    collection_id: Union[Unset, None, int] = UNSET,
    x_keyfactor_api_version: Union[Unset, str] = "1",
    x_keyfactor_requested_with: str = "APIClient",
) -> Response[ModelsEnrollmentAvailableRenewal]:
    """Returns the type of renewal available for a given certificate.

     ### Available Renewal Types ###
    | Value              | Description               |
    |--------------------|---------------------------|
    | 0              | None                 |
    | 1             | Seeded PFX                |
    | 2                | One-click                   |

    Args:
        id (int):
        collection_id (Union[Unset, None, int]):
        x_keyfactor_api_version (Union[Unset, str]):  Default: '1'.
        x_keyfactor_requested_with (str):  Default: 'APIClient'.

    Returns:
        Response[ModelsEnrollmentAvailableRenewal]
    """

    kwargs = _get_kwargs(
        id=id,
        client=client,
        collection_id=collection_id,
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
    collection_id: Union[Unset, None, int] = UNSET,
    x_keyfactor_api_version: Union[Unset, str] = "1",
    x_keyfactor_requested_with: str = "APIClient",
) -> Optional[ModelsEnrollmentAvailableRenewal]:
    """Returns the type of renewal available for a given certificate.

     ### Available Renewal Types ###
    | Value              | Description               |
    |--------------------|---------------------------|
    | 0              | None                 |
    | 1             | Seeded PFX                |
    | 2                | One-click                   |

    Args:
        id (int):
        collection_id (Union[Unset, None, int]):
        x_keyfactor_api_version (Union[Unset, str]):  Default: '1'.
        x_keyfactor_requested_with (str):  Default: 'APIClient'.

    Returns:
        Response[ModelsEnrollmentAvailableRenewal]
    """

    return sync_detailed(
        id=id,
        client=client,
        collection_id=collection_id,
        x_keyfactor_api_version=x_keyfactor_api_version,
        x_keyfactor_requested_with=x_keyfactor_requested_with,
    ).parsed


async def asyncio_detailed(
    id: int,
    *,
    client: Client,
    collection_id: Union[Unset, None, int] = UNSET,
    x_keyfactor_api_version: Union[Unset, str] = "1",
    x_keyfactor_requested_with: str = "APIClient",
) -> Response[ModelsEnrollmentAvailableRenewal]:
    """Returns the type of renewal available for a given certificate.

     ### Available Renewal Types ###
    | Value              | Description               |
    |--------------------|---------------------------|
    | 0              | None                 |
    | 1             | Seeded PFX                |
    | 2                | One-click                   |

    Args:
        id (int):
        collection_id (Union[Unset, None, int]):
        x_keyfactor_api_version (Union[Unset, str]):  Default: '1'.
        x_keyfactor_requested_with (str):  Default: 'APIClient'.

    Returns:
        Response[ModelsEnrollmentAvailableRenewal]
    """

    kwargs = _get_kwargs(
        id=id,
        client=client,
        collection_id=collection_id,
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
    collection_id: Union[Unset, None, int] = UNSET,
    x_keyfactor_api_version: Union[Unset, str] = "1",
    x_keyfactor_requested_with: str = "APIClient",
) -> Optional[ModelsEnrollmentAvailableRenewal]:
    """Returns the type of renewal available for a given certificate.

     ### Available Renewal Types ###
    | Value              | Description               |
    |--------------------|---------------------------|
    | 0              | None                 |
    | 1             | Seeded PFX                |
    | 2                | One-click                   |

    Args:
        id (int):
        collection_id (Union[Unset, None, int]):
        x_keyfactor_api_version (Union[Unset, str]):  Default: '1'.
        x_keyfactor_requested_with (str):  Default: 'APIClient'.

    Returns:
        Response[ModelsEnrollmentAvailableRenewal]
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            collection_id=collection_id,
            x_keyfactor_api_version=x_keyfactor_api_version,
            x_keyfactor_requested_with=x_keyfactor_requested_with,
        )
    ).parsed
