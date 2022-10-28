# Copyright 2022 Keyfactor                                                   
# Licensed under the Apache License, Version 2.0 (the "License"); you may    
# not use this file except in compliance with the License.  You may obtain a 
# copy of the License at http://www.apache.org/licenses/LICENSE-2.0.  Unless 
# required by applicable law or agreed to in writing, software distributed   
# under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES   
# OR CONDITIONS OF ANY KIND, either express or implied. See the License for  
# the specific language governing permissions and limitations under the       
# License. 
from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.keyfactor_api_models_workflows_definition_response import KeyfactorApiModelsWorkflowsDefinitionResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    definition_id: str,
    *,
    client: Client,
    definition_version: Union[Unset, None, int] = UNSET,
    exportable: Union[Unset, None, bool] = UNSET,
    x_keyfactor_api_version: Union[Unset, str] = "1",
    x_keyfactor_requested_with: str = "APIClient",
) -> Dict[str, Any]:
    url = "{}/Workflow/Definitions/{definitionId}".format(client.base_url, definitionId=definition_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    if not isinstance(x_keyfactor_api_version, Unset):
        headers["x-keyfactor-api-version"] = x_keyfactor_api_version

    headers["x-keyfactor-requested-with"] = x_keyfactor_requested_with

    params: Dict[str, Any] = {}
    params["definitionVersion"] = definition_version

    params["exportable"] = exportable

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[KeyfactorApiModelsWorkflowsDefinitionResponse]:
    if response.status_code == 200:
        response_200 = KeyfactorApiModelsWorkflowsDefinitionResponse.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[KeyfactorApiModelsWorkflowsDefinitionResponse]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    definition_id: str,
    *,
    client: Client,
    definition_version: Union[Unset, None, int] = UNSET,
    exportable: Union[Unset, None, bool] = UNSET,
    x_keyfactor_api_version: Union[Unset, str] = "1",
    x_keyfactor_requested_with: str = "APIClient",
) -> Response[KeyfactorApiModelsWorkflowsDefinitionResponse]:
    """Gets a workflow definition.

    Args:
        definition_id (str):
        definition_version (Union[Unset, None, int]):
        exportable (Union[Unset, None, bool]):
        x_keyfactor_api_version (Union[Unset, str]):  Default: '1'.
        x_keyfactor_requested_with (str):  Default: 'APIClient'.

    Returns:
        Response[KeyfactorApiModelsWorkflowsDefinitionResponse]
    """

    kwargs = _get_kwargs(
        definition_id=definition_id,
        client=client,
        definition_version=definition_version,
        exportable=exportable,
        x_keyfactor_api_version=x_keyfactor_api_version,
        x_keyfactor_requested_with=x_keyfactor_requested_with,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    definition_id: str,
    *,
    client: Client,
    definition_version: Union[Unset, None, int] = UNSET,
    exportable: Union[Unset, None, bool] = UNSET,
    x_keyfactor_api_version: Union[Unset, str] = "1",
    x_keyfactor_requested_with: str = "APIClient",
) -> Optional[KeyfactorApiModelsWorkflowsDefinitionResponse]:
    """Gets a workflow definition.

    Args:
        definition_id (str):
        definition_version (Union[Unset, None, int]):
        exportable (Union[Unset, None, bool]):
        x_keyfactor_api_version (Union[Unset, str]):  Default: '1'.
        x_keyfactor_requested_with (str):  Default: 'APIClient'.

    Returns:
        Response[KeyfactorApiModelsWorkflowsDefinitionResponse]
    """

    return sync_detailed(
        definition_id=definition_id,
        client=client,
        definition_version=definition_version,
        exportable=exportable,
        x_keyfactor_api_version=x_keyfactor_api_version,
        x_keyfactor_requested_with=x_keyfactor_requested_with,
    ).parsed


async def asyncio_detailed(
    definition_id: str,
    *,
    client: Client,
    definition_version: Union[Unset, None, int] = UNSET,
    exportable: Union[Unset, None, bool] = UNSET,
    x_keyfactor_api_version: Union[Unset, str] = "1",
    x_keyfactor_requested_with: str = "APIClient",
) -> Response[KeyfactorApiModelsWorkflowsDefinitionResponse]:
    """Gets a workflow definition.

    Args:
        definition_id (str):
        definition_version (Union[Unset, None, int]):
        exportable (Union[Unset, None, bool]):
        x_keyfactor_api_version (Union[Unset, str]):  Default: '1'.
        x_keyfactor_requested_with (str):  Default: 'APIClient'.

    Returns:
        Response[KeyfactorApiModelsWorkflowsDefinitionResponse]
    """

    kwargs = _get_kwargs(
        definition_id=definition_id,
        client=client,
        definition_version=definition_version,
        exportable=exportable,
        x_keyfactor_api_version=x_keyfactor_api_version,
        x_keyfactor_requested_with=x_keyfactor_requested_with,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    definition_id: str,
    *,
    client: Client,
    definition_version: Union[Unset, None, int] = UNSET,
    exportable: Union[Unset, None, bool] = UNSET,
    x_keyfactor_api_version: Union[Unset, str] = "1",
    x_keyfactor_requested_with: str = "APIClient",
) -> Optional[KeyfactorApiModelsWorkflowsDefinitionResponse]:
    """Gets a workflow definition.

    Args:
        definition_id (str):
        definition_version (Union[Unset, None, int]):
        exportable (Union[Unset, None, bool]):
        x_keyfactor_api_version (Union[Unset, str]):  Default: '1'.
        x_keyfactor_requested_with (str):  Default: 'APIClient'.

    Returns:
        Response[KeyfactorApiModelsWorkflowsDefinitionResponse]
    """

    return (
        await asyncio_detailed(
            definition_id=definition_id,
            client=client,
            definition_version=definition_version,
            exportable=exportable,
            x_keyfactor_api_version=x_keyfactor_api_version,
            x_keyfactor_requested_with=x_keyfactor_requested_with,
        )
    ).parsed
