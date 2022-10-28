# Copyright 2022 Keyfactor                                                   
# Licensed under the Apache License, Version 2.0 (the "License"); you may    
# not use this file except in compliance with the License.  You may obtain a 
# copy of the License at http://www.apache.org/licenses/LICENSE-2.0.  Unless 
# required by applicable law or agreed to in writing, software distributed   
# under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES   
# OR CONDITIONS OF ANY KIND, either express or implied. See the License for  
# the specific language governing permissions and limitations under the       
# License. 
from typing import Any, Dict, List, Optional, Union

import httpx

from ...client import Client
from ...models.keyfactor_api_models_security_roles_identities_security_roles_global_permission_request import (
    KeyfactorApiModelsSecurityRolesIdentitiesSecurityRolesGlobalPermissionRequest,
)
from ...models.keyfactor_api_models_security_roles_identities_security_roles_global_permission_response import (
    KeyfactorApiModelsSecurityRolesIdentitiesSecurityRolesGlobalPermissionResponse,
)
from ...types import Response, Unset


def _get_kwargs(
    id: int,
    *,
    client: Client,
    json_body: List[KeyfactorApiModelsSecurityRolesIdentitiesSecurityRolesGlobalPermissionRequest],
    x_keyfactor_api_version: Union[Unset, str] = "1",
    x_keyfactor_requested_with: str = "APIClient",
) -> Dict[str, Any]:
    url = "{}/Security/Roles/{id}/Permissions/Global".format(client.base_url, id=id)

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
) -> Optional[List[KeyfactorApiModelsSecurityRolesIdentitiesSecurityRolesGlobalPermissionResponse]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = (
                KeyfactorApiModelsSecurityRolesIdentitiesSecurityRolesGlobalPermissionResponse.from_dict(
                    response_200_item_data
                )
            )

            response_200.append(response_200_item)

        return response_200
    return None


def _build_response(
    *, response: httpx.Response
) -> Response[List[KeyfactorApiModelsSecurityRolesIdentitiesSecurityRolesGlobalPermissionResponse]]:
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
    json_body: List[KeyfactorApiModelsSecurityRolesIdentitiesSecurityRolesGlobalPermissionRequest],
    x_keyfactor_api_version: Union[Unset, str] = "1",
    x_keyfactor_requested_with: str = "APIClient",
) -> Response[List[KeyfactorApiModelsSecurityRolesIdentitiesSecurityRolesGlobalPermissionResponse]]:
    """Adds global permissions to the security role that matches the id.

     ### Valid Global Permissions ###
    | Area                          | Permission        |
    |-------------------------------|-------------------|
    | AdminPortal                   | Read              |
    | AgentAutoRegistration         | Read              |
    | AgentAutoRegistration         | Modify            |
    | AgentManagement               | Read              |
    | AgentManagement               | Modify            |
    | API                           | Read              |
    | ApplicationSettings           | Read              |
    | ApplicationSettings           | Modify            |
    | Auditing                      | Read              |
    | CertificateCollections        | Modify            |
    | CertificateEnrollment         | EnrollPFX         |
    | CertificateEnrollment         | EnrollCSR         |
    | CertificateEnrollment         | CsrGeneration     |
    | CertificateEnrollment         | PendingCsr        |
    | CertificateMetadataTypes      | Read              |
    | CertificateMetadataTypes      | Modify            |
    | Certificates                  | Read              |
    | Certificates                  | EditMetadata      |
    | Certificates                  | Import            |
    | Certificates                  | Recover           |
    | Certificates                  | Revoke            |
    | Certificates                  | Delete            |
    | Certificates                  | ImportPrivateKey  |
    | CertificateStoreManagement    | Read              |
    | CertificateStoreManagement    | Schedule          |
    | CertificateStoreManagement    | Modify            |
    | Dashboard                     | Read              |
    | Dashboard                     | RiskHeader        |
    | EventHandlerRegistration      | Read              |
    | EventHandlerRegistration      | Modify            |
    | MacAutoEnrollManagement       | Read              |
    | MacAutoEnrollManagement       | Modify            |
    | Monitoring                    | Read              |
    | Monitoring                    | Modify            |
    | Monitoring                    | Test              |
    | PkiManagement                 | Read              |
    | PkiManagement                 | Modify            |
    | PrivilegedAccessManagement    | Read              |
    | PrivilegedAccessManagement    | Modify            |
    | Reports                       | Read              |
    | Reports                       | Modify            |
    | SecuritySettings              | Read              |
    | SecuritySettings              | Modify            |
    | SSH                           | User              |
    | SSH                           | ServerAdmin       |
    | SSH                           | EnterpriseAdmin   |
    | SslManagement                 | Read              |
    | SslManagement                 | Modify            |
    | SystemSettings                | Read              |
    | SystemSettings                | Modify            |
    | WorkflowDefinitions           | Read              |
    | WorkflowDefinitions           | Modify            |
    | WorkflowInstances             | ReadAll           |
    | WorkflowInstances             | ReadAssignedToMe  |
    | WorkflowInstances             | ReadMy            |
    | WorkflowInstances             | Manage            |
    | WorkflowManagement            | Read              |
    | WorkflowManagement            | Modify            |
    | WorkflowManagement            | Test              |
    | WorkflowManagement            | Participate       |
    | WorkflowManagement            | Manage            |

    Args:
        id (int):
        x_keyfactor_api_version (Union[Unset, str]):  Default: '1'.
        x_keyfactor_requested_with (str):  Default: 'APIClient'.
        json_body
            (List[KeyfactorApiModelsSecurityRolesIdentitiesSecurityRolesGlobalPermissionRequest]):

    Returns:
        Response[List[KeyfactorApiModelsSecurityRolesIdentitiesSecurityRolesGlobalPermissionResponse]]
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
    json_body: List[KeyfactorApiModelsSecurityRolesIdentitiesSecurityRolesGlobalPermissionRequest],
    x_keyfactor_api_version: Union[Unset, str] = "1",
    x_keyfactor_requested_with: str = "APIClient",
) -> Optional[List[KeyfactorApiModelsSecurityRolesIdentitiesSecurityRolesGlobalPermissionResponse]]:
    """Adds global permissions to the security role that matches the id.

     ### Valid Global Permissions ###
    | Area                          | Permission        |
    |-------------------------------|-------------------|
    | AdminPortal                   | Read              |
    | AgentAutoRegistration         | Read              |
    | AgentAutoRegistration         | Modify            |
    | AgentManagement               | Read              |
    | AgentManagement               | Modify            |
    | API                           | Read              |
    | ApplicationSettings           | Read              |
    | ApplicationSettings           | Modify            |
    | Auditing                      | Read              |
    | CertificateCollections        | Modify            |
    | CertificateEnrollment         | EnrollPFX         |
    | CertificateEnrollment         | EnrollCSR         |
    | CertificateEnrollment         | CsrGeneration     |
    | CertificateEnrollment         | PendingCsr        |
    | CertificateMetadataTypes      | Read              |
    | CertificateMetadataTypes      | Modify            |
    | Certificates                  | Read              |
    | Certificates                  | EditMetadata      |
    | Certificates                  | Import            |
    | Certificates                  | Recover           |
    | Certificates                  | Revoke            |
    | Certificates                  | Delete            |
    | Certificates                  | ImportPrivateKey  |
    | CertificateStoreManagement    | Read              |
    | CertificateStoreManagement    | Schedule          |
    | CertificateStoreManagement    | Modify            |
    | Dashboard                     | Read              |
    | Dashboard                     | RiskHeader        |
    | EventHandlerRegistration      | Read              |
    | EventHandlerRegistration      | Modify            |
    | MacAutoEnrollManagement       | Read              |
    | MacAutoEnrollManagement       | Modify            |
    | Monitoring                    | Read              |
    | Monitoring                    | Modify            |
    | Monitoring                    | Test              |
    | PkiManagement                 | Read              |
    | PkiManagement                 | Modify            |
    | PrivilegedAccessManagement    | Read              |
    | PrivilegedAccessManagement    | Modify            |
    | Reports                       | Read              |
    | Reports                       | Modify            |
    | SecuritySettings              | Read              |
    | SecuritySettings              | Modify            |
    | SSH                           | User              |
    | SSH                           | ServerAdmin       |
    | SSH                           | EnterpriseAdmin   |
    | SslManagement                 | Read              |
    | SslManagement                 | Modify            |
    | SystemSettings                | Read              |
    | SystemSettings                | Modify            |
    | WorkflowDefinitions           | Read              |
    | WorkflowDefinitions           | Modify            |
    | WorkflowInstances             | ReadAll           |
    | WorkflowInstances             | ReadAssignedToMe  |
    | WorkflowInstances             | ReadMy            |
    | WorkflowInstances             | Manage            |
    | WorkflowManagement            | Read              |
    | WorkflowManagement            | Modify            |
    | WorkflowManagement            | Test              |
    | WorkflowManagement            | Participate       |
    | WorkflowManagement            | Manage            |

    Args:
        id (int):
        x_keyfactor_api_version (Union[Unset, str]):  Default: '1'.
        x_keyfactor_requested_with (str):  Default: 'APIClient'.
        json_body
            (List[KeyfactorApiModelsSecurityRolesIdentitiesSecurityRolesGlobalPermissionRequest]):

    Returns:
        Response[List[KeyfactorApiModelsSecurityRolesIdentitiesSecurityRolesGlobalPermissionResponse]]
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
    json_body: List[KeyfactorApiModelsSecurityRolesIdentitiesSecurityRolesGlobalPermissionRequest],
    x_keyfactor_api_version: Union[Unset, str] = "1",
    x_keyfactor_requested_with: str = "APIClient",
) -> Response[List[KeyfactorApiModelsSecurityRolesIdentitiesSecurityRolesGlobalPermissionResponse]]:
    """Adds global permissions to the security role that matches the id.

     ### Valid Global Permissions ###
    | Area                          | Permission        |
    |-------------------------------|-------------------|
    | AdminPortal                   | Read              |
    | AgentAutoRegistration         | Read              |
    | AgentAutoRegistration         | Modify            |
    | AgentManagement               | Read              |
    | AgentManagement               | Modify            |
    | API                           | Read              |
    | ApplicationSettings           | Read              |
    | ApplicationSettings           | Modify            |
    | Auditing                      | Read              |
    | CertificateCollections        | Modify            |
    | CertificateEnrollment         | EnrollPFX         |
    | CertificateEnrollment         | EnrollCSR         |
    | CertificateEnrollment         | CsrGeneration     |
    | CertificateEnrollment         | PendingCsr        |
    | CertificateMetadataTypes      | Read              |
    | CertificateMetadataTypes      | Modify            |
    | Certificates                  | Read              |
    | Certificates                  | EditMetadata      |
    | Certificates                  | Import            |
    | Certificates                  | Recover           |
    | Certificates                  | Revoke            |
    | Certificates                  | Delete            |
    | Certificates                  | ImportPrivateKey  |
    | CertificateStoreManagement    | Read              |
    | CertificateStoreManagement    | Schedule          |
    | CertificateStoreManagement    | Modify            |
    | Dashboard                     | Read              |
    | Dashboard                     | RiskHeader        |
    | EventHandlerRegistration      | Read              |
    | EventHandlerRegistration      | Modify            |
    | MacAutoEnrollManagement       | Read              |
    | MacAutoEnrollManagement       | Modify            |
    | Monitoring                    | Read              |
    | Monitoring                    | Modify            |
    | Monitoring                    | Test              |
    | PkiManagement                 | Read              |
    | PkiManagement                 | Modify            |
    | PrivilegedAccessManagement    | Read              |
    | PrivilegedAccessManagement    | Modify            |
    | Reports                       | Read              |
    | Reports                       | Modify            |
    | SecuritySettings              | Read              |
    | SecuritySettings              | Modify            |
    | SSH                           | User              |
    | SSH                           | ServerAdmin       |
    | SSH                           | EnterpriseAdmin   |
    | SslManagement                 | Read              |
    | SslManagement                 | Modify            |
    | SystemSettings                | Read              |
    | SystemSettings                | Modify            |
    | WorkflowDefinitions           | Read              |
    | WorkflowDefinitions           | Modify            |
    | WorkflowInstances             | ReadAll           |
    | WorkflowInstances             | ReadAssignedToMe  |
    | WorkflowInstances             | ReadMy            |
    | WorkflowInstances             | Manage            |
    | WorkflowManagement            | Read              |
    | WorkflowManagement            | Modify            |
    | WorkflowManagement            | Test              |
    | WorkflowManagement            | Participate       |
    | WorkflowManagement            | Manage            |

    Args:
        id (int):
        x_keyfactor_api_version (Union[Unset, str]):  Default: '1'.
        x_keyfactor_requested_with (str):  Default: 'APIClient'.
        json_body
            (List[KeyfactorApiModelsSecurityRolesIdentitiesSecurityRolesGlobalPermissionRequest]):

    Returns:
        Response[List[KeyfactorApiModelsSecurityRolesIdentitiesSecurityRolesGlobalPermissionResponse]]
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
    json_body: List[KeyfactorApiModelsSecurityRolesIdentitiesSecurityRolesGlobalPermissionRequest],
    x_keyfactor_api_version: Union[Unset, str] = "1",
    x_keyfactor_requested_with: str = "APIClient",
) -> Optional[List[KeyfactorApiModelsSecurityRolesIdentitiesSecurityRolesGlobalPermissionResponse]]:
    """Adds global permissions to the security role that matches the id.

     ### Valid Global Permissions ###
    | Area                          | Permission        |
    |-------------------------------|-------------------|
    | AdminPortal                   | Read              |
    | AgentAutoRegistration         | Read              |
    | AgentAutoRegistration         | Modify            |
    | AgentManagement               | Read              |
    | AgentManagement               | Modify            |
    | API                           | Read              |
    | ApplicationSettings           | Read              |
    | ApplicationSettings           | Modify            |
    | Auditing                      | Read              |
    | CertificateCollections        | Modify            |
    | CertificateEnrollment         | EnrollPFX         |
    | CertificateEnrollment         | EnrollCSR         |
    | CertificateEnrollment         | CsrGeneration     |
    | CertificateEnrollment         | PendingCsr        |
    | CertificateMetadataTypes      | Read              |
    | CertificateMetadataTypes      | Modify            |
    | Certificates                  | Read              |
    | Certificates                  | EditMetadata      |
    | Certificates                  | Import            |
    | Certificates                  | Recover           |
    | Certificates                  | Revoke            |
    | Certificates                  | Delete            |
    | Certificates                  | ImportPrivateKey  |
    | CertificateStoreManagement    | Read              |
    | CertificateStoreManagement    | Schedule          |
    | CertificateStoreManagement    | Modify            |
    | Dashboard                     | Read              |
    | Dashboard                     | RiskHeader        |
    | EventHandlerRegistration      | Read              |
    | EventHandlerRegistration      | Modify            |
    | MacAutoEnrollManagement       | Read              |
    | MacAutoEnrollManagement       | Modify            |
    | Monitoring                    | Read              |
    | Monitoring                    | Modify            |
    | Monitoring                    | Test              |
    | PkiManagement                 | Read              |
    | PkiManagement                 | Modify            |
    | PrivilegedAccessManagement    | Read              |
    | PrivilegedAccessManagement    | Modify            |
    | Reports                       | Read              |
    | Reports                       | Modify            |
    | SecuritySettings              | Read              |
    | SecuritySettings              | Modify            |
    | SSH                           | User              |
    | SSH                           | ServerAdmin       |
    | SSH                           | EnterpriseAdmin   |
    | SslManagement                 | Read              |
    | SslManagement                 | Modify            |
    | SystemSettings                | Read              |
    | SystemSettings                | Modify            |
    | WorkflowDefinitions           | Read              |
    | WorkflowDefinitions           | Modify            |
    | WorkflowInstances             | ReadAll           |
    | WorkflowInstances             | ReadAssignedToMe  |
    | WorkflowInstances             | ReadMy            |
    | WorkflowInstances             | Manage            |
    | WorkflowManagement            | Read              |
    | WorkflowManagement            | Modify            |
    | WorkflowManagement            | Test              |
    | WorkflowManagement            | Participate       |
    | WorkflowManagement            | Manage            |

    Args:
        id (int):
        x_keyfactor_api_version (Union[Unset, str]):  Default: '1'.
        x_keyfactor_requested_with (str):  Default: 'APIClient'.
        json_body
            (List[KeyfactorApiModelsSecurityRolesIdentitiesSecurityRolesGlobalPermissionRequest]):

    Returns:
        Response[List[KeyfactorApiModelsSecurityRolesIdentitiesSecurityRolesGlobalPermissionResponse]]
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
