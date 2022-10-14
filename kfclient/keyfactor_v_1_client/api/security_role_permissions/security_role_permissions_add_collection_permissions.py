from typing import Any, Dict, List, Optional, Union

import httpx

from ...client import Client
from ...models.keyfactor_api_models_security_roles_identities_security_roles_collection_permission_request import (
    KeyfactorApiModelsSecurityRolesIdentitiesSecurityRolesCollectionPermissionRequest,
)
from ...models.keyfactor_api_models_security_roles_identities_security_roles_collection_permission_response import (
    KeyfactorApiModelsSecurityRolesIdentitiesSecurityRolesCollectionPermissionResponse,
)
from ...types import Response, Unset


def _get_kwargs(
    id: int,
    *,
    client: Client,
    json_body: List[KeyfactorApiModelsSecurityRolesIdentitiesSecurityRolesCollectionPermissionRequest],
    x_keyfactor_api_version: Union[Unset, str] = "1",
    x_keyfactor_requested_with: str = "APIClient",
) -> Dict[str, Any]:
    url = "{}/Security/Roles/{id}/Permissions/Collections".format(client.base_url, id=id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    if not isinstance(x_keyfactor_api_version, Unset):
        headers["x-keyfactor-api-version"] = x_keyfactor_api_version

    headers["x-keyfactor-requested-with"] = x_keyfactor_requested_with

    json_json_body = []
    for json_body_item_data in json_body:
        json_body_item = json_body_item_data.to_dict()

        json_json_body.append(json_body_item)

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
    }


def _parse_response(
    *, response: httpx.Response
) -> Optional[List[KeyfactorApiModelsSecurityRolesIdentitiesSecurityRolesCollectionPermissionResponse]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = (
                KeyfactorApiModelsSecurityRolesIdentitiesSecurityRolesCollectionPermissionResponse.from_dict(
                    response_200_item_data
                )
            )

            response_200.append(response_200_item)

        return response_200
    return None


def _build_response(
    *, response: httpx.Response
) -> Response[List[KeyfactorApiModelsSecurityRolesIdentitiesSecurityRolesCollectionPermissionResponse]]:
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
    json_body: List[KeyfactorApiModelsSecurityRolesIdentitiesSecurityRolesCollectionPermissionRequest],
    x_keyfactor_api_version: Union[Unset, str] = "1",
    x_keyfactor_requested_with: str = "APIClient",
) -> Response[List[KeyfactorApiModelsSecurityRolesIdentitiesSecurityRolesCollectionPermissionResponse]]:
    """Adds collection permissions to the security role that matches the id.

     ### Valid Permissions ###
    | Permission    | Permission Display Name   |
    |---------------|---------------------------|
    | Read          | Read                      |
    | EditMetadata  | Edit Metadata             |
    | Recover       | Download with Private Key |
    | Revoke        | Revoke                    |
    | Delete        | Delete                    |

    Args:
        id (int):
        x_keyfactor_api_version (Union[Unset, str]):  Default: '1'.
        x_keyfactor_requested_with (str):  Default: 'APIClient'.
        json_body
            (List[KeyfactorApiModelsSecurityRolesIdentitiesSecurityRolesCollectionPermissionRequest]):

    Returns:
        Response[List[KeyfactorApiModelsSecurityRolesIdentitiesSecurityRolesCollectionPermissionResponse]]
    """

    kwargs = _get_kwargs(
        id=id,
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
    id: int,
    *,
    client: Client,
    json_body: List[KeyfactorApiModelsSecurityRolesIdentitiesSecurityRolesCollectionPermissionRequest],
    x_keyfactor_api_version: Union[Unset, str] = "1",
    x_keyfactor_requested_with: str = "APIClient",
) -> Optional[List[KeyfactorApiModelsSecurityRolesIdentitiesSecurityRolesCollectionPermissionResponse]]:
    """Adds collection permissions to the security role that matches the id.

     ### Valid Permissions ###
    | Permission    | Permission Display Name   |
    |---------------|---------------------------|
    | Read          | Read                      |
    | EditMetadata  | Edit Metadata             |
    | Recover       | Download with Private Key |
    | Revoke        | Revoke                    |
    | Delete        | Delete                    |

    Args:
        id (int):
        x_keyfactor_api_version (Union[Unset, str]):  Default: '1'.
        x_keyfactor_requested_with (str):  Default: 'APIClient'.
        json_body
            (List[KeyfactorApiModelsSecurityRolesIdentitiesSecurityRolesCollectionPermissionRequest]):

    Returns:
        Response[List[KeyfactorApiModelsSecurityRolesIdentitiesSecurityRolesCollectionPermissionResponse]]
    """

    return sync_detailed(
        id=id,
        client=client,
        json_body=json_body,
        x_keyfactor_api_version=x_keyfactor_api_version,
        x_keyfactor_requested_with=x_keyfactor_requested_with,
    ).parsed


async def asyncio_detailed(
    id: int,
    *,
    client: Client,
    json_body: List[KeyfactorApiModelsSecurityRolesIdentitiesSecurityRolesCollectionPermissionRequest],
    x_keyfactor_api_version: Union[Unset, str] = "1",
    x_keyfactor_requested_with: str = "APIClient",
) -> Response[List[KeyfactorApiModelsSecurityRolesIdentitiesSecurityRolesCollectionPermissionResponse]]:
    """Adds collection permissions to the security role that matches the id.

     ### Valid Permissions ###
    | Permission    | Permission Display Name   |
    |---------------|---------------------------|
    | Read          | Read                      |
    | EditMetadata  | Edit Metadata             |
    | Recover       | Download with Private Key |
    | Revoke        | Revoke                    |
    | Delete        | Delete                    |

    Args:
        id (int):
        x_keyfactor_api_version (Union[Unset, str]):  Default: '1'.
        x_keyfactor_requested_with (str):  Default: 'APIClient'.
        json_body
            (List[KeyfactorApiModelsSecurityRolesIdentitiesSecurityRolesCollectionPermissionRequest]):

    Returns:
        Response[List[KeyfactorApiModelsSecurityRolesIdentitiesSecurityRolesCollectionPermissionResponse]]
    """

    kwargs = _get_kwargs(
        id=id,
        client=client,
        json_body=json_body,
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
    json_body: List[KeyfactorApiModelsSecurityRolesIdentitiesSecurityRolesCollectionPermissionRequest],
    x_keyfactor_api_version: Union[Unset, str] = "1",
    x_keyfactor_requested_with: str = "APIClient",
) -> Optional[List[KeyfactorApiModelsSecurityRolesIdentitiesSecurityRolesCollectionPermissionResponse]]:
    """Adds collection permissions to the security role that matches the id.

     ### Valid Permissions ###
    | Permission    | Permission Display Name   |
    |---------------|---------------------------|
    | Read          | Read                      |
    | EditMetadata  | Edit Metadata             |
    | Recover       | Download with Private Key |
    | Revoke        | Revoke                    |
    | Delete        | Delete                    |

    Args:
        id (int):
        x_keyfactor_api_version (Union[Unset, str]):  Default: '1'.
        x_keyfactor_requested_with (str):  Default: 'APIClient'.
        json_body
            (List[KeyfactorApiModelsSecurityRolesIdentitiesSecurityRolesCollectionPermissionRequest]):

    Returns:
        Response[List[KeyfactorApiModelsSecurityRolesIdentitiesSecurityRolesCollectionPermissionResponse]]
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            json_body=json_body,
            x_keyfactor_api_version=x_keyfactor_api_version,
            x_keyfactor_requested_with=x_keyfactor_requested_with,
        )
    ).parsed
