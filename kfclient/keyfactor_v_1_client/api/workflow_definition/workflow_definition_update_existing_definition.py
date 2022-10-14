from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.keyfactor_api_models_workflows_definition_response import KeyfactorApiModelsWorkflowsDefinitionResponse
from ...models.keyfactor_api_models_workflows_definition_update_request import (
    KeyfactorApiModelsWorkflowsDefinitionUpdateRequest,
)
from ...types import Response, Unset


def _get_kwargs(
    definition_id: str,
    *,
    client: Client,
    form_data: KeyfactorApiModelsWorkflowsDefinitionUpdateRequest,
    json_body: KeyfactorApiModelsWorkflowsDefinitionUpdateRequest,
    x_keyfactor_api_version: Union[Unset, str] = "1",
    x_keyfactor_requested_with: str = "APIClient",
) -> Dict[str, Any]:
    url = "{}/Workflow/Definitions/{definitionId}".format(client.base_url, definitionId=definition_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    if not isinstance(x_keyfactor_api_version, Unset):
        headers["x-keyfactor-api-version"] = x_keyfactor_api_version

    headers["x-keyfactor-requested-with"] = x_keyfactor_requested_with

    json_body.to_dict()

    return {
        "method": "put",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "data": form_data.to_dict(),
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
    form_data: KeyfactorApiModelsWorkflowsDefinitionUpdateRequest,
    json_body: KeyfactorApiModelsWorkflowsDefinitionUpdateRequest,
    x_keyfactor_api_version: Union[Unset, str] = "1",
    x_keyfactor_requested_with: str = "APIClient",
) -> Response[KeyfactorApiModelsWorkflowsDefinitionResponse]:
    """Updates the existing definition's DisplayName and Description.

    Args:
        definition_id (str):
        x_keyfactor_api_version (Union[Unset, str]):  Default: '1'.
        x_keyfactor_requested_with (str):  Default: 'APIClient'.
        json_body (KeyfactorApiModelsWorkflowsDefinitionUpdateRequest):  Example: {'DisplayName':
            '<Updated workflow name>', 'Description': '<Updated workflow description>'}.

    Returns:
        Response[KeyfactorApiModelsWorkflowsDefinitionResponse]
    """

    kwargs = _get_kwargs(
        definition_id=definition_id,
        client=client,
        form_data=form_data,
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
    definition_id: str,
    *,
    client: Client,
    form_data: KeyfactorApiModelsWorkflowsDefinitionUpdateRequest,
    json_body: KeyfactorApiModelsWorkflowsDefinitionUpdateRequest,
    x_keyfactor_api_version: Union[Unset, str] = "1",
    x_keyfactor_requested_with: str = "APIClient",
) -> Optional[KeyfactorApiModelsWorkflowsDefinitionResponse]:
    """Updates the existing definition's DisplayName and Description.

    Args:
        definition_id (str):
        x_keyfactor_api_version (Union[Unset, str]):  Default: '1'.
        x_keyfactor_requested_with (str):  Default: 'APIClient'.
        json_body (KeyfactorApiModelsWorkflowsDefinitionUpdateRequest):  Example: {'DisplayName':
            '<Updated workflow name>', 'Description': '<Updated workflow description>'}.

    Returns:
        Response[KeyfactorApiModelsWorkflowsDefinitionResponse]
    """

    return sync_detailed(
        definition_id=definition_id,
        client=client,
        form_data=form_data,
        json_body=json_body,
        x_keyfactor_api_version=x_keyfactor_api_version,
        x_keyfactor_requested_with=x_keyfactor_requested_with,
    ).parsed


async def asyncio_detailed(
    definition_id: str,
    *,
    client: Client,
    form_data: KeyfactorApiModelsWorkflowsDefinitionUpdateRequest,
    json_body: KeyfactorApiModelsWorkflowsDefinitionUpdateRequest,
    x_keyfactor_api_version: Union[Unset, str] = "1",
    x_keyfactor_requested_with: str = "APIClient",
) -> Response[KeyfactorApiModelsWorkflowsDefinitionResponse]:
    """Updates the existing definition's DisplayName and Description.

    Args:
        definition_id (str):
        x_keyfactor_api_version (Union[Unset, str]):  Default: '1'.
        x_keyfactor_requested_with (str):  Default: 'APIClient'.
        json_body (KeyfactorApiModelsWorkflowsDefinitionUpdateRequest):  Example: {'DisplayName':
            '<Updated workflow name>', 'Description': '<Updated workflow description>'}.

    Returns:
        Response[KeyfactorApiModelsWorkflowsDefinitionResponse]
    """

    kwargs = _get_kwargs(
        definition_id=definition_id,
        client=client,
        form_data=form_data,
        json_body=json_body,
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
    form_data: KeyfactorApiModelsWorkflowsDefinitionUpdateRequest,
    json_body: KeyfactorApiModelsWorkflowsDefinitionUpdateRequest,
    x_keyfactor_api_version: Union[Unset, str] = "1",
    x_keyfactor_requested_with: str = "APIClient",
) -> Optional[KeyfactorApiModelsWorkflowsDefinitionResponse]:
    """Updates the existing definition's DisplayName and Description.

    Args:
        definition_id (str):
        x_keyfactor_api_version (Union[Unset, str]):  Default: '1'.
        x_keyfactor_requested_with (str):  Default: 'APIClient'.
        json_body (KeyfactorApiModelsWorkflowsDefinitionUpdateRequest):  Example: {'DisplayName':
            '<Updated workflow name>', 'Description': '<Updated workflow description>'}.

    Returns:
        Response[KeyfactorApiModelsWorkflowsDefinitionResponse]
    """

    return (
        await asyncio_detailed(
            definition_id=definition_id,
            client=client,
            form_data=form_data,
            json_body=json_body,
            x_keyfactor_api_version=x_keyfactor_api_version,
            x_keyfactor_requested_with=x_keyfactor_requested_with,
        )
    ).parsed
