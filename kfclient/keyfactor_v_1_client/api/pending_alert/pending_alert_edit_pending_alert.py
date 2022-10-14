from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.keyfactor_api_models_alerts_pending_pending_alert_definition_response import (
    KeyfactorApiModelsAlertsPendingPendingAlertDefinitionResponse,
)
from ...models.keyfactor_api_models_alerts_pending_pending_alert_update_request import (
    KeyfactorApiModelsAlertsPendingPendingAlertUpdateRequest,
)
from ...types import Response, Unset


def _get_kwargs(
    *,
    client: Client,
    form_data: KeyfactorApiModelsAlertsPendingPendingAlertUpdateRequest,
    json_body: KeyfactorApiModelsAlertsPendingPendingAlertUpdateRequest,
    x_keyfactor_api_version: Union[Unset, str] = "1",
    x_keyfactor_requested_with: str = "APIClient",
) -> Dict[str, Any]:
    url = "{}/Alerts/Pending".format(client.base_url)

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


def _parse_response(
    *, response: httpx.Response
) -> Optional[KeyfactorApiModelsAlertsPendingPendingAlertDefinitionResponse]:
    if response.status_code == 200:
        response_200 = KeyfactorApiModelsAlertsPendingPendingAlertDefinitionResponse.from_dict(response.json())

        return response_200
    return None


def _build_response(
    *, response: httpx.Response
) -> Response[KeyfactorApiModelsAlertsPendingPendingAlertDefinitionResponse]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    form_data: KeyfactorApiModelsAlertsPendingPendingAlertUpdateRequest,
    json_body: KeyfactorApiModelsAlertsPendingPendingAlertUpdateRequest,
    x_keyfactor_api_version: Union[Unset, str] = "1",
    x_keyfactor_requested_with: str = "APIClient",
) -> Response[KeyfactorApiModelsAlertsPendingPendingAlertDefinitionResponse]:
    """Edit a pending alert

    Args:
        x_keyfactor_api_version (Union[Unset, str]):  Default: '1'.
        x_keyfactor_requested_with (str):  Default: 'APIClient'.
        json_body (KeyfactorApiModelsAlertsPendingPendingAlertUpdateRequest):

    Returns:
        Response[KeyfactorApiModelsAlertsPendingPendingAlertDefinitionResponse]
    """

    kwargs = _get_kwargs(
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
    *,
    client: Client,
    form_data: KeyfactorApiModelsAlertsPendingPendingAlertUpdateRequest,
    json_body: KeyfactorApiModelsAlertsPendingPendingAlertUpdateRequest,
    x_keyfactor_api_version: Union[Unset, str] = "1",
    x_keyfactor_requested_with: str = "APIClient",
) -> Optional[KeyfactorApiModelsAlertsPendingPendingAlertDefinitionResponse]:
    """Edit a pending alert

    Args:
        x_keyfactor_api_version (Union[Unset, str]):  Default: '1'.
        x_keyfactor_requested_with (str):  Default: 'APIClient'.
        json_body (KeyfactorApiModelsAlertsPendingPendingAlertUpdateRequest):

    Returns:
        Response[KeyfactorApiModelsAlertsPendingPendingAlertDefinitionResponse]
    """

    return sync_detailed(
        client=client,
        form_data=form_data,
        json_body=json_body,
        x_keyfactor_api_version=x_keyfactor_api_version,
        x_keyfactor_requested_with=x_keyfactor_requested_with,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    form_data: KeyfactorApiModelsAlertsPendingPendingAlertUpdateRequest,
    json_body: KeyfactorApiModelsAlertsPendingPendingAlertUpdateRequest,
    x_keyfactor_api_version: Union[Unset, str] = "1",
    x_keyfactor_requested_with: str = "APIClient",
) -> Response[KeyfactorApiModelsAlertsPendingPendingAlertDefinitionResponse]:
    """Edit a pending alert

    Args:
        x_keyfactor_api_version (Union[Unset, str]):  Default: '1'.
        x_keyfactor_requested_with (str):  Default: 'APIClient'.
        json_body (KeyfactorApiModelsAlertsPendingPendingAlertUpdateRequest):

    Returns:
        Response[KeyfactorApiModelsAlertsPendingPendingAlertDefinitionResponse]
    """

    kwargs = _get_kwargs(
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
    *,
    client: Client,
    form_data: KeyfactorApiModelsAlertsPendingPendingAlertUpdateRequest,
    json_body: KeyfactorApiModelsAlertsPendingPendingAlertUpdateRequest,
    x_keyfactor_api_version: Union[Unset, str] = "1",
    x_keyfactor_requested_with: str = "APIClient",
) -> Optional[KeyfactorApiModelsAlertsPendingPendingAlertDefinitionResponse]:
    """Edit a pending alert

    Args:
        x_keyfactor_api_version (Union[Unset, str]):  Default: '1'.
        x_keyfactor_requested_with (str):  Default: 'APIClient'.
        json_body (KeyfactorApiModelsAlertsPendingPendingAlertUpdateRequest):

    Returns:
        Response[KeyfactorApiModelsAlertsPendingPendingAlertDefinitionResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            form_data=form_data,
            json_body=json_body,
            x_keyfactor_api_version=x_keyfactor_api_version,
            x_keyfactor_requested_with=x_keyfactor_requested_with,
        )
    ).parsed
