from typing import Any, Dict, List, Optional, Union

import httpx

from ...client import Client
from ...models.keyfactor_api_models_workflows_definition_response import KeyfactorApiModelsWorkflowsDefinitionResponse
from ...models.keyfactor_api_models_workflows_definition_step_request import (
    KeyfactorApiModelsWorkflowsDefinitionStepRequest,
)
from ...types import Response, Unset


def _get_kwargs(
    definition_id: str,
    *,
    client: Client,
    form_data: List[KeyfactorApiModelsWorkflowsDefinitionStepRequest],
    json_body: List[KeyfactorApiModelsWorkflowsDefinitionStepRequest],
    x_keyfactor_api_version: Union[Unset, str] = "1",
    x_keyfactor_requested_with: str = "APIClient",
) -> Dict[str, Any]:
    url = "{}/Workflow/Definitions/{definitionId}/Steps".format(client.base_url, definitionId=definition_id)

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
    form_data: List[KeyfactorApiModelsWorkflowsDefinitionStepRequest],
    json_body: List[KeyfactorApiModelsWorkflowsDefinitionStepRequest],
    x_keyfactor_api_version: Union[Unset, str] = "1",
    x_keyfactor_requested_with: str = "APIClient",
) -> Response[KeyfactorApiModelsWorkflowsDefinitionResponse]:
    """Sets the provided steps on the latest version of the definition.

     If the latest version is also the published version, a new version will be created and the steps
    will be set on that new version.

    Args:
        definition_id (str):
        x_keyfactor_api_version (Union[Unset, str]):  Default: '1'.
        x_keyfactor_requested_with (str):  Default: 'APIClient'.
        json_body (List[KeyfactorApiModelsWorkflowsDefinitionStepRequest]):

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
    form_data: List[KeyfactorApiModelsWorkflowsDefinitionStepRequest],
    json_body: List[KeyfactorApiModelsWorkflowsDefinitionStepRequest],
    x_keyfactor_api_version: Union[Unset, str] = "1",
    x_keyfactor_requested_with: str = "APIClient",
) -> Optional[KeyfactorApiModelsWorkflowsDefinitionResponse]:
    """Sets the provided steps on the latest version of the definition.

     If the latest version is also the published version, a new version will be created and the steps
    will be set on that new version.

    Args:
        definition_id (str):
        x_keyfactor_api_version (Union[Unset, str]):  Default: '1'.
        x_keyfactor_requested_with (str):  Default: 'APIClient'.
        json_body (List[KeyfactorApiModelsWorkflowsDefinitionStepRequest]):

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
    form_data: List[KeyfactorApiModelsWorkflowsDefinitionStepRequest],
    json_body: List[KeyfactorApiModelsWorkflowsDefinitionStepRequest],
    x_keyfactor_api_version: Union[Unset, str] = "1",
    x_keyfactor_requested_with: str = "APIClient",
) -> Response[KeyfactorApiModelsWorkflowsDefinitionResponse]:
    """Sets the provided steps on the latest version of the definition.

     If the latest version is also the published version, a new version will be created and the steps
    will be set on that new version.

    Args:
        definition_id (str):
        x_keyfactor_api_version (Union[Unset, str]):  Default: '1'.
        x_keyfactor_requested_with (str):  Default: 'APIClient'.
        json_body (List[KeyfactorApiModelsWorkflowsDefinitionStepRequest]):

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
    form_data: List[KeyfactorApiModelsWorkflowsDefinitionStepRequest],
    json_body: List[KeyfactorApiModelsWorkflowsDefinitionStepRequest],
    x_keyfactor_api_version: Union[Unset, str] = "1",
    x_keyfactor_requested_with: str = "APIClient",
) -> Optional[KeyfactorApiModelsWorkflowsDefinitionResponse]:
    """Sets the provided steps on the latest version of the definition.

     If the latest version is also the published version, a new version will be created and the steps
    will be set on that new version.

    Args:
        definition_id (str):
        x_keyfactor_api_version (Union[Unset, str]):  Default: '1'.
        x_keyfactor_requested_with (str):  Default: 'APIClient'.
        json_body (List[KeyfactorApiModelsWorkflowsDefinitionStepRequest]):

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
